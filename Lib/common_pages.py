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

# url
dev_front_url = 'https://dev-www.fashiongo.net'

# Item
## Dev Openpack
dev_openpack1_url = 'https://dev-www.fashiongo.net/Item/14221067?paKey=20241030c8eff5ffeb173f7b81e9d6d8da034739'
dev_openpack2_url = 'https://dev-www.fashiongo.net/Item/14221066?paKey=20241030ec7ab07500df119f54af0a10f64dbbd1'

## Dev Prepack
dev_prepack1_url = 'https://dev-www.fashiongo.net/Item/14221424?paKey=2024103050f1197905054a61997f9bbbd7bfb9e8'
dev_prepack2_url = 'https://dev-www.fashiongo.net/Item/14221068?paKey=20241030db81ab0a5e72a3fcc9309fbffed4ee23'

