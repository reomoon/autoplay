import os
from dotenv import load_dotenv

# Pages/front login
def login(page):
    # 환경변수 .env에서 로그인 정보 읽기
    def_front_username = os.getenv("dev_front_username")
    dev_front_password = os.getenv("dev_front_password")

    # 로그인 요소 정의 및 동작
    cookies = page.locator('#onetrust-accept-btn-handler')
    cookies.click()

    signin_link = page.locator('a.header_signIn')
    signin_link.click()
    
    username_input = page.locator('input[name="userName"]')
    password_input = page.locator('input[name="password"]')
    username_input.fill(def_front_username)
    password_input.fill(dev_front_password)

    signin_button = page.locator('.signin_btn')
    signin_button.click()
