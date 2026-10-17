from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_OPENAPI_KEY")

client = OpenAI(
    api_key= api_key,
    base_url= "https://generativelanguage.googleapis.com/v1beta/openai/"
)

def main():
    user_query = input("> ")
    response = client.chat.completions.create(
        model= "gemini-3.8-flash",
        messages= [
            {"role":"user", "content": user_query}
        ]
    )

    print(f"🤖: {response.choices[0].message.content}")

main() 