from openai import OpenAI
from dotenv import load_dotenv
import os
import requests

load_dotenv()

api_key = os.getenv("GEMINI_OPENAPI_KEY")

client = OpenAI(
    api_key= api_key,
    base_url= "https://generativelanguage.googleapis.com/v1beta/openai/"
)

def get_weather(city:str):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)

    if response.status_code == 200:
        return f"Ther weather in {city} is {response.text}"

    return f"Something went wrong"



def main():
    user_query = input("> ")
    response = client.chat.completions.create(
        model= "gemini-3.8-flash",
        messages= [
            {"role":"user", "content": user_query}
        ]
    )
    print(response.choices[0].message.content)

print(get_weather("Delhi"))