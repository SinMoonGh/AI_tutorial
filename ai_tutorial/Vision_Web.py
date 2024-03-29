from dotenv import load_dotenv
from openai import OpenAI
import os

# .env 파일에서 환경 변수를 로드합니다.
load_dotenv()

# 환경 변수를 사용하여 API 키를 불러옵니다.
openai_api_key = os.getenv("NEW_API_KEY")

# API 키를 출력하여 확인합니다. 실제 사용시에는 출력하지 않도록 주의하세요.
# print(openai_api_key)

# 이 API 키를 사용하여 OpenAI API 등에 요청을 보낼 수 있습니다.

client = OpenAI(api_key=openai_api_key)

response_img = client.images.generate(
  model="dall-e-3",
  prompt="가방 안으로 들어간 노인",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response_img.data[0].url


# 이미지 웹 주소
url = image_url

response = client.chat.completions.create(
  model="gpt-4-vision-preview",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "What’s in this image?"},
        {
          "type": "image_url",
          "image_url": {
            "url": url,
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

print(response.choices[0])