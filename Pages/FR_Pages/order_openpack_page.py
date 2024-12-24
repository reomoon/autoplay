import random # 랜덤함수 추가
from playwright.async_api import async_playwright
from Lib.browser_utils import HighlightPageWrapper
from Lib.common_utils import navigate_to, checkout_process
from Lib.common_pages import dev_openpack1_url

# Pages/front openpack order
async def order_openpack(page):

    # openpack item url 이동
    await navigate_to(page, dev_openpack1_url) # from Lib.common_utils import navigate_to 함수 호출

    # 1번째칸 수량 
    item_input1 = await page.locator('#openPackEachSizePc00')
    random_quantity = random.randint(1,3) # 1 ~ 3사이 랜덤값
    item_input1.type(str(random_quantity)) # type 랜덤값 입력

    # Add To Shopping BAG 버튼 클릭
    await page.click_locator('.btn.btn_black_v01.addCart.nclick')

    # Cart 안담기는 문제가 있어 3초 대기
    await page.wait_for_timeout(3000)

    # 헤더 /cart 아이콘 클릭
    await page.click_locator('#miniCount')

    # checkout_process 호출
    await checkout_process(page)