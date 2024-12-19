import pytest
from Pages.order_openpack_page import order_openpack
from test_login import login_fixture

def test_order_openpack(login_fixture):
    # 로그인된 페이지 사용
    page = login_fixture

    # order_openpack 실행
    order_openpack(page)

    # 브라우저 닫기 (pytest fixture에서 자동으로 닫기 처리)
