from playwright.async_api import async_playwright
import asyncio

# Lib/browser_util.py 크롬 브라우저 런처

async def launch_browser():
    p = await async_playwright().start()
    browser = await p.chromium.launch(headless=False, args=["--kiosk"])
    return p, browser  # p와 browser를 튜플로 반환

async def close_browser(p, browser):
    await browser.close()  # 비동기적으로 브라우저 종료
    await p.stop()  # 비동기적으로 Playwright 종료

class HighlightPageWrapper:
    """
    locator Highlight 표시
    """ 
    def __init__(self, page):
        self._page = page  # 원래 Playwright의 page 객체를 저장

    async def locator(self, selector, *args, **kwargs):
        """
        locator 호출 시 자동으로 하이라이트
        *args는 주로 인수가 여러 개일 수 있는 경우에 사용, 
        **kwargs는 키워드 인수로 전달된 값을 받아서 유연하게 처리
        """
        locator = self._page.locator(selector, *args, **kwargs)
        await self._page.evaluate("""
        (selector) => {
            const element = document.querySelector(selector);
            if (element) {
                element.style.border = '2px solid red';  // 빨간색 테두리 추가
                setTimeout(() => {
                    element.style.border = '';  // 일정 시간 후 테두리 제거
                }, 1000);
            }
        }
    """, selector)
        
        # 요소가 DOM에 존재하는지 체크 (is_visible 대신 사용)
        if await locator.count() > 0:
            print(f"{selector} found")
        else:
            print(f"{selector} not found")
        return locator
    
    async def click_locator(self, selector, *args, **kwargs):
        """
        지정된 selector로 클릭 동작을 수행하고, 하이라이트 추가
        요소가 없으면 스킵
        """
        await self._page.wait_for_load_state() # 페이지 로드 될 때까지 기다리기

        try:
            locator = self.locator(selector, *args, **kwargs)  # 하이라이트 추가 후 locator 반환
            if await locator.is_visible() and await locator.count() > 0: # 요소 존재하는지 확인
                await locator.click()  # 클릭 수행
                print(f"{selector} Clicked")
            else:
                print(f"{selector} Not found. Skipping.")
        except Exception as e:
            print(f"Error: Failed to click on {selector}. Exception: {e}")
            # raise  # 필요하면 예외를 다시 발생시켜 호출자에게 알림 raise 주석처리로 예외 발생하더라고 중단되지 않도록 처리

    async def wait_for_load_state(self, *args, **kwargs):
        """
        페이지의 로딩 상태가 완료될 때까지 기다립니다.
        """
        return await self._page.wait_for_load_state(*args, **kwargs)
    
    async def wait_for_element(self, selector, timeout=5000):
        """
        지정된 selector가 페이지에 로드될 때까지 기다립니다.
        """
        await self._page.wait_for_selector(selector, timeout=timeout)
        return self._page.locator(selector)
    
    async def __getattr__(self, name):
        """
        원래 Playwright의 page 메서드 및 속성에 접근 가능하도록 래핑
        """
        attr = getattr(self._page, name)
        
        # 페이지의 goto 같은 메서드도 잘 호출되도록 보장
        if callable(attr):
            async def wrapped(*args, **kwargs):
                return await attr(*args, **kwargs)
            return wrapped
        
        return attr