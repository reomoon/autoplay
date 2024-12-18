import os
from Lib.browser_utils import HighlightPageWrapper
from Lib.common_pages import *

# Pages/front login
def login(page):
    # 로그인 정보 가져오기
    def_front_username = LOGIN_CREDENTIALS["username"]
    dev_front_password = LOGIN_CREDENTIALS["password"]

    # 로그인 요소 정의 및 동작
    page.click_locator('#onetrust-accept-btn-handler')

    page.click_locator('a.header_signIn')
    
    username_input = page.locator('input[name="userName"]')
    password_input = page.locator('input[name="password"]')
    username_input.fill(def_front_username)
    password_input.fill(dev_front_password)

    page.click_locator('.signin_btn')
