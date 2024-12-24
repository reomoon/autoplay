import pytest
from playwright.async_api import async_playwright
from Pages.FR_Pages.order_openpack_page import order_openpack
from Pages.FR_Pages.order_prepack_page import order_prepack
from Pages.FR_Pages.order_promotion_page import order_promotion
from test_login import login_fixture

@pytest.mark.asyncio
async def test_order_openpack(login_fixture):
    page = login_fixture    # 로그인된 페이지 사용
    await order_openpack(page)    # order_openpack 실행
    # 브라우저 닫기 (pytest fixture에서 자동으로 닫기 처리)

def test_order_prepack(login_fixture):
    page = login_fixture    # 로그인된 페이지 사용
    order_prepack(page)     # order_prepack 실행

def test_order_promotion(login_fixture):
    page = login_fixture
    order_promotion(page)

   
