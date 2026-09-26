# Few Shot Prompting 

from dotenv import load_dotenv
from openai import OpenAI
import os

# load_dotenv()
load_dotenv("02_AI_API/.env")

api_key = os.getenv("GEMINI_OPENAPI_KEY")

print("API key loaded:", bool(api_key))

client = OpenAI(
    api_key= api_key,
    base_url= "https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Few short Prompting: Directly giving the instruction to model and few example to the model

SYSTEM_PROMPT = """
You should only ans the coding related questions, Do not ans else, Your name is Alexa, If user ask sonthing other than coding just say sorry.

Examples:
Q: Can you explain the a + b whole square?
A: Sorry, I can only help with coding related questions.

Q: Hey, Write a code in pthon for adding two numbers.
A: def add(a + b):
        return a + b


"""

response = client.chat.completions.create(
    model= "gemini-3.6-flash",
    messages= [
        {"role":"system", "content":SYSTEM_PROMPT},
        # {"role":"user", "content":"Hey, write OSPF command. "}
        # {"role":"user", "content":"Hey, can you explain a - b whole square "}
        {"role":"user", "content":"Hey, write a code in python a - b whole square "}
    ]
)

print(response.choices[0].message.content)

# Few-Short Prompting : The model is provided with a few examples before asking it to generate a response.