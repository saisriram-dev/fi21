from google import genai
import os
from dotenv import load_dotenv

# Load the API key from the .env file
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize the Gemini client with the API key
client = genai.Client(api_key=API_KEY)

# To create a chat, we need to use the chat endpoint. 
# The chat endpoint allows us to have a conversation with the model.
#  We can send messages to the model and it will respond accordingly.
chat = client.chats.create(model="gemini-2.5-flash")

# Getting the mode
mode = input("Choose the mode (1 for single message, 2 for streaming): ")

# Final chat code

while True:
    message = input("You: ")

    # End the chat if the user types 'exit'
    if message.lower() == "exit":
        print("Chat ended.")
        break

    if mode == "1":
        res = chat.send_message(message)
        print("Gemini: " + res.text)

    elif mode == "2":
        res = chat.send_message_stream(message)

        print("Gemini: ", end="")
        for stream_response in res:
            print(stream_response.text, end="")

"""
    while True:
    message = input("You: ")

    # End the chat if the user types 'exit'
    if message.lower() == "exit":
        print("Chat ended.")
        break

    res = client.models.generate_content_stream(
        model="gemini-2.5-flash",
        contents=message,
    )

    for stream_response in res:
        print("Gemini: " + stream_response.text)
    
The above method is not recommended as it does not maintain the context of the conversation.
It basically does not remember the previous messages in the conversation and treats each 
message as a separate input.
"""
