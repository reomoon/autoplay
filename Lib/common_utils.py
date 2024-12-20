import os
from dotenv import load_dotenv
from Pages.login_page import login

# .env 파일 로드
load_dotenv()

# 공통 환경 변수(전역 변수로 정의)
LOGIN_CREDENTIALS = {
    "username": os.getenv("dev_front_username"),
    "password": os.getenv("dev_front_password"),
}

def navigate_to(page, url):
    """
    지정된 URL로 페이지를 이동하는 함수
    """
    page.goto(url)
    print(f"Navigated to {url}")

def checkout_process(page):
    """
    Cart 부터 시작
    """
    # Shopping BAG 클릭 후 URL 검증
    expected_url = 'https://dev-www.fashiongo.net/cart'
    page.wait_for_url(expected_url)

    assert page.url == expected_url, f"Fail: Expected URL {expected_url}, but got {page.url}." # assert를 사용하여 실패 시 메시지 출력
    print(f"Success: {expected_url} matched the expected value!")

    # Cart > Proceed To Checkout 버튼 클릭
    page.click_locator('.btn-dark_grey.btn-checkoutAll.nclick')

    # You Have Promotions! 팝업
    page.locator('button.btn-sure', has_text="Continue To Checkout").click()

    '''
    Checkout Step1_Shipping
    '''
    # Save & Continue 버튼 클릭
    page.locator('.btn-dark_grey.btn-goToPayment').click()

    ## Verify Your Address 팝업
    page.locator('.common-btn.c-black', has_text="Keep This Address").click()

    '''
    Checkout Step2_Payment
    '''
    # Save & Continue 버튼 클릭
    page.click_locator('.btn-dark_grey.btn-goToReview')

    '''
    Checkout Step3_Order Review
    '''
    # Submit Order 버튼 클릭
    page.click_locator('.btn-dark_grey.btn-checkout')

    # 잠시 대기 (3초 대기)
    page.wait_for_timeout(3000)

    # 주문 완료 후 Thank you for your order! 텍스트가 포함된 h2 요소 확인
    page.wait_for_load_state()  # 페이지가 완전히 로드될 때까지 기다리기
    if page.locator('h2.order-title').is_visible():  # h2 태그의 order-title 클래스가 있으면 성공
        print("Order successful! Test passed.")
    else:
        print("Order not found! Test failed.")