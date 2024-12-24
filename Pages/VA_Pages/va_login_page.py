from playwright.async_api import async_playwright
from Lib.browser_utils import HighlightPageWrapper

# Pages/front login
async def va_login(page):
    from Lib.common_utils import LOGIN_CREDENTIALS # 함수 내부에서 임포트

    # 로그인 정보 가져오기 (전역 변수 LOGIN_CREDENTIALS 사용)
    dev_va_username = LOGIN_CREDENTIALS["va_username"]
    dev_va_password = LOGIN_CREDENTIALS["va_password"]

    # 로그인 요소 정의 및 동작
    username_input = page.locator('input[formcontrolname="userName"]')
    await page.wait_for_timeout(1000)
    await username_input.type(dev_va_username, delay = 100) # 키 입력 시 100ms 지연

    password_input = page.locator('input[formcontrolname="password"]')
    await page.wait_for_timeout(1000)
    await password_input.type(dev_va_password, delay = 100)

    # SECURE LOGIN
    await page.click_locator('.btn.btn-blue.width-100p.btn-login')

    # 3초간 대기
    await page.wait_for_timeout(3000)

    # 로딩 상태가 완료될 때까지 기다림
    # page.wait_for_load_state()

    # 또는 특정 URL을 기다릴 수도 있습니다
    # page.wait_for_url('https://dev-vendoradmin.fashiongo.net/#/home/')

    # FG Free Shipping 팝업 x버튼
    FreeShipping_popup = page.locator('.modal-dialog .modal-close-btn')
    await FreeShipping_popup.click().nth(0)
    FreeShipping_popup3 = page.locator('.modal-dialog.w-900').locator('i.modal-close-btn')
    await FreeShipping_popup3.click().nth(1)
    


    

    
