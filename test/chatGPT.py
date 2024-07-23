# python3
# Please install OpenAI SDK first：`pip3 install openai`
from openai import OpenAI

client = OpenAI(api_key="sk-a707aa3c7d5d4916bc57bb65acaed7b0", base_url="https://api.deepseek.com/v1")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    stream=False
)

print(response.choices[0].message.content)