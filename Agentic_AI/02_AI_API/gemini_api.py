
# from google import genai

# client = genai.Client(
#     # api_key= "Enter api key here"
# )

# interaction = client.interactions.create(
#     model="gemini-3.8-flash",
#     input="Explain how AI works in a few words"
# )
# # print(interaction.output_text)


# # **********************************************

# from google import genai

# client = genai.Client(
#     # api_key= "Enter api key here"
# )


# response = client.models.generate_content(
#     model= "gemini-3.8-flash",
#     contents= "Hey there, Raunak here, How are you"
# )

# print(response.text)


# Direct use of automatic function calling (AFC) in Models.generate_content is not recommended. Instead, we recommend to use AFC in Chat.send_message. Similarly, direct use of AFC in Models.generate_content_stream is not recommended. Instead, we recommend to use AFC in Chat.send_message_stream.


# *************** below code, for .gitignore **************


# import os
# from dotenv import load_dotenv
# from google import genai

# load_dotenv("02_AI_API/.env")

# client = genai.Client(
#     api_key=os.getenv("GEMINI_API_KEY")
# )

# response = client.models.generate_content(
#     model="gemini-3.8-flash",
#     contents="Hey there, how are you?"
# )

# print(response.text)




import os
from dotenv import load_dotenv
from google import genai

load_dotenv("02_AI_API/.env")

api_key = os.getenv("GEMINI_API_KEY")

print("API key loaded:", bool(api_key))

client = genai.Client(
    api_key=api_key
)

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Hey there, how are you?"
)

print(response.text)