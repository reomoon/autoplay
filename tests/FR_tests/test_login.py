import pytest
import pytest_asyncio
from playwright.async_api import async_playwright
from Lib.browser_utils import launch_browser, close_browser, HighlightPageWrapper
from Pages.FR_Pages.login_page import login
from Lib.common_pages import dev_front_url

@pytest_asyncio.fixture(scope="module")
async def login_fixture():
    # Playwright 컨텍스트와 브라우저를 초기화
    p, browser = await launch_browser()
    page = HighlightPageWrapper(await browser.new_page())  # 래핑된 페이지 사용
    
    await page.goto(dev_front_url)
    # 페이지 뷰포트를 최대화 크기로 설정
    page.set_viewport_size({"width": 1680, "height": 900})

    # 로그인 함수 호출
    await login(page)

    # 로그인 후 URL 검증
    expected_url = 'https://dev-www.fashiongo.net/'
    
    # assert를 사용하여 성공 시 메시지 출력
    assert page.url == expected_url, f"Fail: Expected URL {expected_url}, but got {page.url}."
    
    # 성공적으로 통과하면 출력
    print("Success: Login successful, URL matches expected.")

    yield page #로그인된 페이지를 반환    
    await close_browser(p, browser) # Playwright 컨텍스트와 브라우저 닫기