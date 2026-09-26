from dotenv import load_dotenv
from openai import OpenAI
import os
import json

load_dotenv()

api_key = os.getenv("GEMINI_OPENAPI_KEY")

print("API key loaded:", bool(api_key))

client = OpenAI(
    api_key= api_key,
    base_url= "https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """
    You're an expert Assistant in resolving user queries using chan of thought.You work on START, PLAN and OUTPUT steps.
    You need to first PLAN what need to be done. The PLAN can be multiple steps. 
    Once you think enough PLAN has been done, finally you can give an OUTPUT.

    Rules:
    - Strictly Follow the given JSON output format
    - Only run one step at a time.
    - The sequence of steps is START (where user gives an input), PLAN (That can be multiple times) and finally OUTPUT (which is going to the displayed to the user).

    Ouput JSON Format:
    {"step": "Start" | "PLAN" | "OUTPUT", "content": "string"}

    Example:
    START: Hey, can you solve 2 + 3 * 5 / 10
    PLAN: {"step": "PLAN", "content": "Seems like user is interest in math problems"}
    PLAN: {"step": "PLAN", "content": "looking at the problem, we should solve this using BODMAS method"}
    PLAN: {"step": "PLAN", "content": "first we must multiply 3 * 5 which is 15"}
    PLAN: {"step": "PLAN", "content": "Now the new equation is 2 + 15 / 10"}
    PLAN: {"step": "PLAN", "content": "We must perform divide that is 15 / 10 = 1.5"}
    PLAN: {"step": "PLAN", "content": "Now the new equation is 2 + 1.5"}
    PLAN: {"step": "PLAN", "content": "Now finally lets perform the add"}
    PLAN: {"step": "PLAN", "content": "Great, We have solved and finally left 3.5 as ans "}
    PLAN: {"step": "OUTPUT", "content": "3.5 "}


"""

response = client.chat.completions.create(
    model= "gemini-3.8-flash",
    response_format={ "type": "json_object" },
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Hey, write a code to add n number in js"},
        # Manually keep adding messages to history
        {"role":"assistant", "content": json.dumps({"step": "PLAN", "content": "The user wants a JavaScript code snippet to sum 'n' numbers."})},
        # {"role": "user","content": "Continue to the next step."}
        {"role":"assistant", "content": json.dumps({"step": "PLAN", "content": "There are multiple ways to interpret adding 'n' numbers: summing numbers from 1 to n, summing an array of n numbers, or using rest parameters (...numbers) to sum arbitrary arguments. Providing a versatile solution using rest parameters along with an array reduce approach is usually the cleanest and most common idiom in modern JavaScript."})},
        {"role": "user","content": "Continue to the next step."}

    ]
)

print(response.choices[0].message.content)