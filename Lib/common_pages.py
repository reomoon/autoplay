import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# 공통 환경 변수
LOGIN_CREDENTIALS = {
    "username": os.getenv("dev_front_username"),
    "password": os.getenv("dev_front_password"),
}
