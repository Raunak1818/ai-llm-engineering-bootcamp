# Few Shot Prompting
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
# Zero Shot Prompting: Directly giving th instruction to the model
SYSTEM_PROMPT = "You should only and only ans the coding related question, Do not ans anything else. Your name is Alexa If user ask somthing other than coding just say sorry "

response = client.chat.completions.create(
    model="gemini-3.8-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        # {"role": "user", "content": "Hey can you tell me a joke"}    
        # {"role": "user", "content": "Hey can you translate word hello to hindi"}
        {"role": "user", "content": "Hey can you write python code to translate word hello to hindi"}
    ]
)

print(response.choices[0].message.content)

