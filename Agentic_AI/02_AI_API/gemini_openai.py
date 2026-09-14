
# from dotenv import load_dotenv
# from openai import OpenAI

# load_dotenv()

# client = OpenAI(
#     api_key= "Enter api key here",
#     base_url= "https://generativelanguage.googleapis.com/v1beta/openai/"
# )

# response = client.chat.completions.create(
#     model = "gemini-3.6-flash",
#     messages = [
#         { "role": "user", "content": "Hey, I am Raunak! Nice to meet you. Who are you?"}
#     ]
# )

# print(response.choices[0].message.content)


# ************* this for .gitignore************


from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv("02_AI_API/.env")

api_key = os.getenv("GEMINI_OPENAPI_KEY")

print("API key loaded:", bool(api_key))

client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-3.6-flash",
    messages=[
        {
            "role": "user",
            "content": "Hey, I am Raunak! Nice to meet you. Who are you?"
        }
    ]
)

print(response.choices[0].message.content)

