import openai
import os
from dotenv import load_dotenv

# Load the .env file where your API key is stored
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to send a message to GPT-4o
def chat_with_gpt(message):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful and friendly chatbot."},
            {"role": "user", "content": message}
        ]
    )
    return response['choices'][0]['message']['content']

# Chat loop
print("ChatBot is ready. Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting...")
        break
    reply = chat_with_gpt(user_input)
    print("Bot:", reply)