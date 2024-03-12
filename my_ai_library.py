from dotenv import load_dotenv
from openai import OpenAI
import os
import requests
from PIL import Image
import random
import base64



class MyAi:
    def __init__(self) -> None:
        """openai 예제 클래스"""

        # .env 파일에서 환경 변수를 로드합니다.
        load_dotenv()

        # 환경 변수를 사용하여 API 키를 불러옵니다.
        self.openai_api_key = os.getenv("NEW_API_KEY")

        # 이 API 키를 사용하여 OpenAI API 등에 요청을 보낼 수 있습니다.
        self.client = OpenAI(api_key=self.openai_api_key)


    def make_image_file(self, image_url):
        """이미지 url을 입력받고, 파일을 만들어 저장함."""

        # 이미지 저장할 때 파일 여러개 만들기
        random_int = random.randint(1, 100)
        
        # 이미지 파일 저장 경로
        filename = f"example{random_int}.jpg"

        # 이미지 데이터 요청
        create_img_response = requests.get(image_url)

        # 이미지 파일 저장
        with open(filename, "wb") as f:
            f.write(create_img_response.content)

        # 이미지 열기
        Image.open(filename)


    def ai_re_json(self):
        """자연어를 입력받고, 인공지능의 답변을 json으로 반환함"""

        user_input = input("무엇을 도와드릴까요? : ")
        response = self.client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
            {"role": "user", "content": user_input}
        ]
        )
        return response.choices[0].message.content


    def ai_text(self):
        """자연어를 입력받고, 인공지능의 답변을 반환함."""

        user_input = input("무엇을 도와드릴까요? : ")
        response = self.client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input},
            {"role": "assistant", "content": "최대한 자세히 대답해줘."},
            {"role": "assistant", "content": "네가 사람이라고 생각하고 대답해줘."},
            {"role": "assistant", "content": "질문의 의도를 잘 파악해서 그에 맞게 대답해 줘."},
            # {"role": "user", "content": "오늘은 따뜻한게 마시고 싶네"}
        ]
        )

        print(response.choices[0].message.content)


    def ai_image(self):
        """
        자연어를 입력받고, 인공지능이 만든 이미지의 url을 반환.
        """

        user_input = input("원하시는 이미지가 있으신가요? 말씀해 주세요. : ")
        response = self.client.images.generate(
        model = "dall-e-3", # 모델명도 바꿔도 될 것 같다.
        prompt = user_input,
        size = '1024x1024',
        quality="standard",
        n=1,
        )

        # 이미지 웹 주소
        image_url = response.data[0].url
        return image_url


    def vision_many_image(self, image_1_url):
        """이미지 url을 입력하면
        두 개의 이미지를 분석하여 결과를 반환합니다."""

        response = self.client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
            "role": "user",
            "content": [
                {
                "type": "text",
                "text": "What are in these images? Is there any difference between them?",
                },
                {
                "type": "image_url",
                "image_url": {
                    "url": image_1_url,
                },
                },
                {
                "type": "image_url",
                "image_url": {
                    "url": image_1_url,
                },
                },
            ],
            }
        ],
        max_tokens=300,
        )
        print(response.choices[0])

    # Function to encode the image
    def encode_image(self, image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
        

    def vision_local(self, image_path):
        """
        이미지 파일을 넣으면, 이미지에 대해서 인공지능이 답변.
        이미지 파일 : str
        """

        # Path to your image
        

        # Getting the base64 string
        base64_image = self.encode_image(image_path)

        headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {self.openai_api_key}"
        }

        payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
            "role": "user",
            "content": [
                {
                "type": "text",
                "text": "What’s in this image?"
                },
                {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_image}"
                }
                }
            ]
            }
        ],
        "max_tokens": 300
        }

        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

        response_json_data = response.json()

        print(response_json_data['choices'][0]['message']['content'])


    def vision_resolution(self, image_url):
        """이미지 url주소를 넣으면 인공지능이 답변"""

        response = self.client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
            "role": "user",
            "content": [
                {"type": "text", "text": "What’s in this image?"},
                {
                "type": "image_url",
                "image_url": {
                    "url": image_url,
                    "detail": "high" # or low
                },
                },
            ],
            }
        ],
        max_tokens=300,
        )

        print(response.choices[0].message.content)


    def vision_web(self, image_url):
        """이미지 url 주소를 넣으면 인공지능이 답변"""
        # 이미지 웹 주소

        response = self.client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
            "role": "user",
            "content": [
                {"type": "text", "text": "What’s in this image?"},
                {
                "type": "image_url",
                "image_url": {
                    "url": image_url,
                },
                },
            ],
            }
        ],
        max_tokens=300,
        )

        print(response.choices[0])