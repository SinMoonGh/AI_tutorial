from dotenv import load_dotenv
from openai import OpenAI
import os
from PIL import Image
import requests

# .env 파일에서 환경 변수를 로드합니다.
load_dotenv()

# 환경 변수를 사용하여 API 키를 불러옵니다.
openai_api_key = os.getenv("NEW_API_KEY")
client = OpenAI(api_key=openai_api_key)

# API 키를 출력하여 확인합니다. 실제 사용시에는 출력하지 않도록 주의하세요.

# 이 API 키를 사용하여 OpenAI API 등에 요청을 보낼 수 있습니다.

# 이미지 웹 주소
url = "https://s2.paultan.org/image/2013/05/Lamborghini_Egoista_Concept_07.jpg"

# 이미지 파일 저장 경로
filename = "example.jpg"

# 이미지 데이터 요청
response = requests.get(url)

# 이미지 파일 저장
with open(filename, "wb") as f:
    f.write(response.content)

# 이미지 열기
Image.open(filename)
