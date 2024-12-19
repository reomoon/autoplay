import random # 랜덤함수 추가
from Lib.browser_utils import HighlightPageWrapper
from Lib.common_utils import navigate_to, checkout_process
from Lib.common_pages import dev_openpack1_url

# Pages/front openpack order
def order_openpack(page):

    # openpack item url 이동
    navigate_to(page, dev_openpack1_url) # from Lib.common_utils import navigate_to 함수 호출

    # 1번째칸 수량 
    item_input1 = page.locator('#openPackEachSizePc00')
    random_quantity = random.randint(1,3) # 1 ~ 3사이 랜덤값
    item_input1.type(str(random_quantity)) # type 랜덤값 입력

    # Add To Shopping BAG 버튼 클릭
    page.click_locator('.btn.btn_black_v01.addCart.nclick')

    # 헤더 /cart 아이콘 클릭
    page.click_locator('#miniCount')
    
    # Shopping BAG 클릭 후 URL 검증
    expected_url = 'https://dev-www.fashiongo.net/cart'
    page.wait_for_url(expected_url)

    assert page.url == expected_url, f"Fail: Expected URL {expected_url}, but got {page.url}." # assert를 사용하여 성공 시 메시지 출력

    # checkout_process 호출
    checkout_process(page)