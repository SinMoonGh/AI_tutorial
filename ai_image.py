from dotenv import load_dotenv
from openai import OpenAI
import os
import requests
from PIL import Image

# .env 파일에서 환경 변수를 로드합니다.
load_dotenv()

# 환경 변수를 사용하여 API 키를 불러옵니다.
openai_api_key = os.getenv("NEW_API_KEY")

# API 키를 출력하여 확인합니다. 실제 사용시에는 출력하지 않도록 주의하세요.
# print(openai_api_key)

# 이 API 키를 사용하여 OpenAI API 등에 요청을 보낼 수 있습니다.

client = OpenAI(api_key=openai_api_key)

response = client.images.generate(
  model="dall-e-3",
  prompt="토끼를 잡아먹을까 말까 고민하는 곰",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url


# 이미지 웹 주소
url = image_url

# 이미지 파일 저장 경로
filename = "example.jpg"

# 이미지 데이터 요청
create_img_response = requests.get(url)

# 이미지 파일 저장
with open(filename, "wb") as f:
    f.write(create_img_response.content)

# 이미지 열기
Image.open(filename)

