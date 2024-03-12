from dotenv import load_dotenv
from openai import OpenAI
import os
# .env 파일에서 환경 변수를 로드합니다.
load_dotenv()

# 환경 변수를 사용하여 API 키를 불러옵니다.
openai_api_key = os.getenv("NEW_API_KEY")
client = OpenAI(api_key=openai_api_key)

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "커피를 추천해줘"},
    # {"role": "assistant", "content": "너는 답을 간단하게 알려주는 인공지능이야"},
    # {"role": "user", "content": "오늘은 따뜻한게 마시고 싶네"}
  ]
)

print(response.choices[0].message.content)