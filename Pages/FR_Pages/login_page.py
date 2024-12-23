from Lib.browser_utils import HighlightPageWrapper

# Pages/front login
def login(page):
    from Lib.common_utils import LOGIN_CREDENTIALS # 함수 내부에서 임포트

    # 로그인 정보 가져오기 (전역 변수 LOGIN_CREDENTIALS 사용)
    def_front_username = LOGIN_CREDENTIALS["username"]
    dev_front_password = LOGIN_CREDENTIALS["password"]

    # 로그인 요소 정의 및 동작
    page.click_locator('#onetrust-accept-btn-handler')
    page.click_locator('a.header_signIn')
    
    username_input = page.locator('input[name="userName"]') # fill은 채우기만 해서 이벤트가 트리거가 안됨
    username_input.type(def_front_username)
    password_input = page.locator('input[name="password"]')
    password_input.type(dev_front_password)
    
    page.click_locator('.signin_btn')

    # 또는 특정 URL을 기다릴 수도 있습니다
    page.wait_for_url('https://dev-www.fashiongo.net/')

    # 로딩 상태가 완료될 때까지 기다림
    # page.wait_for_load_state()
