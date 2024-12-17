import pytest
from Lib.env import lunch_browser, close_browser
from Pages.login_page import Login

def test_login():
    browser = lunch_browser()
    page = browser.new_page() # 새페이지 열기
    page.goto('https://dev-www.fashiongo.net')

    # Login 클래스 인스턴스화
    login_page = Login(page)
    
    # 로그인 수행 (실제 사용자 이름과 비밀번호를 전달)
    login_page.login('fgautoqa1@yopmail.com', '789456123qQ!')

    # 로그인 후 검증 코드 추가 (예: 로그인 성공 여부 확인)
    # 예시: 페이지 URL 확인
    assert page.url == 'https://dev-www.fashiongo.net'

    close_browser(browser)