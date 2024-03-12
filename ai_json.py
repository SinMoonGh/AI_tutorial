from dotenv import load_dotenv
from openai import OpenAI
import os


# .env 파일에서 환경 변수를 로드합니다.
load_dotenv()

# 환경 변수를 사용하여 API 키를 불러옵니다.
openai_api_key = os.getenv("NEW_API_KEY")
client = OpenAI(api_key=openai_api_key)

# API 키를 출력하여 확인합니다. 실제 사용시에는 출력하지 않도록 주의하세요.

# 이 API 키를 사용하여 OpenAI API 등에 요청을 보낼 수 있습니다.

response = client.chat.completions.create(
  model="gpt-3.5-turbo-0125",
  response_format={ "type": "json_object" },
  messages=[
    {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
    {"role": "user", "content": "고객만족도 조사를 만들려고 하는데 어떻게 만드는 게 좋을까?"}
  ]
)
print(response.choices[0].message.content)