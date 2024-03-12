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
MODEL = "gpt-3.5-turbo-1106"
want_to="""너는 아래 내용을 기반으로 질의응답을 하는 로봇이야.
content
{}"""
content = "멋사 파이썬 백엔드 9기에는 세계 최고의 인재가 모여있다. 그리고 비가 매우 많이 내린다. 그리고 사람처럼 말하는 인공지능을 원한다."

# GPT에게 질문하고 응답 받는 함수
def ask_to_gpt(messages):
    # response = client.chat.completions.create(
    #     model=MODEL,
    #     top_p=0.1,
    #     temperature=0.1,
    #     messages=messages,
    # )
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
    )

    print(response.choices[0].message.content)


messages=[
        {'role': 'system', 'content': want_to.format(content)},
    ]

user_input = input('You: ')

messages.append(
    {'role': 'user', 'content': user_input},
)

response = ask_to_gpt(messages)

print(response)