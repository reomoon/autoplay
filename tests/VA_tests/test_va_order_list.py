import pytest
from playwright.async_api import async_playwright
from Pages.VA_Pages.va_order_list import va_order_list_page
from test_va_login import login_fixture

@pytest.mark.asyncio
async def test_va_login(login_fixture):
    page = login_fixture    # 로그인된 페이지 사용
    await va_order_list_page(page)    # order_openpack 실행
    # 브라우저 닫기 (pytest fixture에서 자동으로 닫기 처리)

   
