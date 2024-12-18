import pytest
from Lib.env import lunch_browser, close_browser, HighlightPageWrapper
from Pages.login_page import Login

def test_login():
    # Playwright 컨텍스트와 브라우저를 초기화
    p, browser = lunch_browser()
    page = HighlightPageWrapper(browser.new_page())  # 래핑된 페이지 사용
    page.goto('https://dev-www.fashiongo.net')

    # Login 클래스 인스턴스화
    login_page = Login(page)
    
    # 로그인 수행 (실제 사용자 이름과 비밀번호를 전달)
    login_page.login('fgautoqa1@yopmail.com', '789456123qQ!')

    # 로그인 후 검증 코드 추가 (예: 로그인 성공 여부 확인)
    assert page.url == 'https://dev-www.fashiongo.net/login?returnUrl=%2F'

    # Playwright 컨텍스트와 브라우저 닫기
    close_browser(p, browser)