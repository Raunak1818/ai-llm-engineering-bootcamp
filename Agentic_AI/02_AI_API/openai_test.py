from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

response = client.chat.completions.create(
    model = "gpt-6-astra",
    messages = [
        { "role": "user", "content": "Write a short bedtime story about a unicorn."}
    ]
)

print(response.choices[0].message.content)