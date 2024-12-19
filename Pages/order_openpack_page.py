from Lib.browser_utils import HighlightPageWrapper
from Lib.common_pages import navigate_to, dev_openpack1_url

# Pages/front openpack order
def order_openpack(page):

    # openpack item url 이동
    navigate_to(page, dev_openpack1_url)

    # 1번째칸 수량 
    item_input1 = page.locator('#openPackEachSizePc00')
    item_input1.type('2')

    # Add To Shopping BAG 버튼 클릭
    page.click_locator('//*[@id="content"]/div/div[1]/div[2]/div[10]/span/button')

    