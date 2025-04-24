import os

import google.generativeai as genai
# import the API key from the env file

from dotenv import load_dotenv#

#  load the env
load_dotenv()

api_key = os.getenv("API_KEY")
if api_key is None:
    raise ValueError("API_KEY not found in environment variables.")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

print("Chat with Gemini! Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    response = chat.send_message(user_input)
    print("Patrick's AI: ", response.text)
