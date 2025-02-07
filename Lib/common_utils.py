import os
from dotenv import load_dotenv
from Pages.FR_Pages.login_page import login

# .env 파일 로드
load_dotenv()

# 공통 환경 변수(전역 변수로 정의)
LOGIN_CREDENTIALS = {
    "fr_username": os.getenv("Dev_fr_username"),
    "fr_password": os.getenv("Dev_fr_password"),
    "va_username" : os.getenv("Dev_va_username"),
    "va_password" : os.getenv("Dev_va_password"),
}

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
    if page.locator('h2.order-title').count() > 0:  # h2 태그의 order-title 클래스가 1개 이상 있으면 성공
        print("Order successful! Test passed.")
    else:
        print("Order not found! Test failed.")

def checkout_promotion(page):
    """
    Cart 부터 시작
    """
    # Shopping BAG 클릭 후 URL 검증
    expected_url = 'https://dev-www.fashiongo.net/cart'
    page.wait_for_url(expected_url)

    assert page.url == expected_url, f"Fail: Expected URL {expected_url}, but got {page.url}." # assert를 사용하여 실패 시 메시지 출력
    print(f"Success: {expected_url} matched the expected value!")

    # Cart > Select Vendor Promotions 버튼 클릭(Vendor ID 16502 Allium)
    page.click_locator('button.btn-vendor.size-medium_blue[data-nclick-extra*="vid=16502"]')
    # 60% Off & Free Shipping $50.00+ Orders
    apply_button = page.locator('button.btn-apply.nclick', has_text="Apply").nth(0) # 첫 번째 버튼 클릭
    apply_button.click()

    # Cart > Proceed To Checkout 버튼 클릭
    page.click_locator('.btn-dark_grey.btn-checkoutAll.nclick')

    # You Have Promotions! 팝업
    # page.locator('button.btn-sure', has_text="Continue To Checkout").click()

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
    if page.getByText("Thank you for your order!").count() > 0:  # h2 태그의 order-title 클래스 1개 이상 있으면 성공
        print("Order successful! Test passed.")
    else:
        print("Order not found! Test failed.")