from playwright.sync_api import sync_playwright

# Lib/env 크롬 브라우저 런처

def lunch_browser():
    # Playwright 컨텍스트를 반환
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False) # headless 여부
    return p, browser

def close_browser(p, browser): # browser 객체가 위에 외부로 있기 떄문에 close 내부 객체를 전달
    browser.close() # 전달된 브라우저 객체를 닫음
    p.stop()

class HighlightPageWrapper:
    """
    locator Highlight 표시
    """ 
    def __init__(self, page):
        self._page = page  # 원래 Playwright의 page 객체를 저장

    def locator(self, selector, *args, **kwargs):
        """
        locator 호출 시 자동으로 하이라이트
        """
        locator = self._page.locator(selector, *args, **kwargs)
        self._page.evaluate("""
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
        return locator
    
    def __getattr__(self, name):
        """
        원래 Playwright의 page 메서드 및 속성에 접근 가능하도록 래핑
        __getattr__의 역할: HighlightPageWrapper가 가진 속성이나 메서드가 아닌 경우, Playwright의 원래 page 객체의 속성이나 메서드를 반환합니다.
        이를 통해 page.goto()와 같은 호출이 직접적으로 가능해집니다.
        """
        return getattr(self._page, name)