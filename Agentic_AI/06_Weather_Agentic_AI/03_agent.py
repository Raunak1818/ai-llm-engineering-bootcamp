# Coding My First AI Agent

from dotenv import load_dotenv
from openai import OpenAI
import os
import json
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

available_tools = {
    "get_weather": get_weather
}

SYSTEM_PROMPT = """
    You're an expert Assistant in resolving user queries using chan of thought.You work on START, PLAN and OUTPUT steps.
    You need to first PLAN what need to be done. The PLAN can be multiple steps. 
    Once you think enough PLAN has been done, finally you can give an OUTPUT.
    You can also a tool if required from the list of available tools.
    for every tool call wait for the observe step wich is the output from the called tools.


    Rules:
    - Strictly Follow the given JSON output format
    - Only run one step at a time.
    - The sequence of steps is START (where user gives an input), PLAN (That can be multiple times) and finally OUTPUT (which is going to the displayed to the user).

    Ouput JSON Format:
    {"step": "Start" | "PLAN" | "OUTPUT" | "TOOL", "content": "string","tool": "string", "input": "string"}

    Available Tools:
    - get_weather(city: str): Takes city name as an input and string and weather info about the city

    Example 1:
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


    Example 2:
    START: What is the weather of Delhi?
    PLAN: {"step": "PLAN", "content": "Seems like user is interest in getting weather of Delhi in India"}
    PLAN: {"step": "PLAN", "content": "Lets see if we have any available tools from the list of available tools"}
    PLAN: {"step": "PLAN", "content": "Greet, we have weather tool available for this query."}
    PLAN: {"step": "PLAN", "content": "I need to call get_weather tool for delhi as input for delhi"}
    PLAN: {"step": "Tool", "tool": "get_weather", "input": "delhi"}
    PLAN: {"step": "OBSERVE", "tool": "get_weather", "content": "The temperature of delhi is cloudy with 20 C"}
    PLAN: {"step": "PLAN", "content": "Great I got the weather info about delhi."}

    PLAN: {"step": "OUTPUT", "content": "the current weather of delhi is 20 C with some cloudy sky. "}


"""

print("\n\n\n")

message_history = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

user_query = input("👉 ")
message_history.append({"role":"user", "content": user_query})

while True:
    response = client.chat.completions.create(
        model= "gemini-3.8-flash",
        response_format= {"type": "json_object"},
        messages= message_history
    )

    raw_result = (response.choices[0].message.content)
    message_history.append({"role": "assistant", "content": raw_result})

    parsed_result = json.loads(raw_result)

    if parsed_result.get("step") == "START":
        print("🔥", parsed_result.get("content"))
        message_history.append({"role": "user", "content": "Continue to the next step."})
        continue

    if parsed_result.get("step") == "TOOL":
        tool_to_call = parsed_result.get("tool")
        tool_input = parsed_result.get("input")
        print(f"⚒️: {tool_to_call} ({tool_input})")

        tool_response = available_tools[tool_to_call](tool_input)
        print(f"⚒️: {tool_to_call} ({tool_input}) = {tool_response}")
        message_history.append({"role":"user", "content": json.dumps(
            {"step": "OBSERVE", "tool": tool_to_call, "input": tool_input, "output": tool_response}
        )})
        continue

    if parsed_result.get("step") == "PLAN":
        print("🧠", parsed_result.get("content"))
        message_history.append({"role": "user", "content": "Continue to the next step."})
        continue

    if parsed_result.get("step") == "OUTPUT":
        print("🤖", parsed_result.get("content"))
        break


print("\n\n\n")