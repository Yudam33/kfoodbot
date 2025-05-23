# app/services/image_recognition.py
from openai import OpenAI
import config
import base64

client = OpenAI(
    base_url="https://api.studio.nebius.ai/v1/",
    api_key=config.NEBIUS_API_KEY,
)

def predict_food_name(image_path: str) -> str:
    print(f"[DEBUG] 이미지 경로: {image_path}")
    image_data = encode_image(image_path)
    # 이미지 분석 API 호출 코드 구현
    # image_path 에서 이미지 읽고, API 호출 후 음식명 반환
    
    response = client.chat.completions.create(
        model="google/gemma-3-27b-it",
        messages=[
            {"role": "system", "content": "You are an image recognition assistant."},
            {
                "role": "user",
                "content": f"Analyze this Korean food image and tell me only the food name in 1-2 words, in Korean, within following examples - 떡볶이, 계란탕, 삼겹살: {image_data}"
            },
        ],
    )

    food_name = response.choices[0].message.content.strip()
    print(f"[DEBUG] 추론된 음식 이름: {food_name}")
    return food_name


def encode_image(image_path: str) -> str:
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


