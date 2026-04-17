# musi_disc.py — AI-powered Music Teacher Chatbot
# Uses Google Gemini API to simulate a knowledgeable music
# teacher that helps users learn instruments and clarify
# music-related doubts.

from google import genai
from dotenv import load_dotenv
from google.genai import types
import os
import json
from datetime import datetime

# Load environment variables from the .env file
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize the Gemini API client with the loaded API key
client = genai.Client(api_key=API_KEY)

# System Prompt
# Defines the persona and behavior of the AI model.
# This is passed with every request to keep the model
# consistently in character as a music teacher.
system_instruction = """
You are a very proficient music teacher with extensive knowledge of various instruments.
Be friendly, professional, and helpful.
Help users learn instruments and clarify any doubts they have regarding music or instruments.
"""

# Conversation State
history = []  # Stores the full conversation turn-by-turn
MAX_TURNS = 20  # Rolling window limit to avoid exceeding context limits

# Main Conversation Loop
while True:

    # Trim history to the last MAX_TURNS messages to stay within context limits
    if len(history) > MAX_TURNS:
        history = history[-MAX_TURNS:]

    user_input = input("Enter any query regarding music: ")

    # Exit Command
    # Gracefully end the session when the user types 'quit' or 'exit'
    if user_input.lower() in ["quit", "exit"]:
        print("Be in tune. Bye!!!")
        break

    # Reset Command
    # Clears conversation history to start a fresh session
    elif user_input.lower() == "reset":
        history = []
        continue

    # Summarize Command
    # Sends the current history plus a summarization prompt to the model
    # and prints a concise recap — does NOT append this to history
    elif user_input.lower() == "summarize":
        summary_prompt = {
            "role": "user",
            "parts": [
                {"text": "Summarize the conversation so far in a concise manner."}
            ],
        }
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=history + [summary_prompt],
            config=types.GenerateContentConfig(system_instruction=system_instruction),
        )
        print("Music Teacher:", response.text, "\n")
        continue

    # Save Command
    # Serializes the conversation history to a timestamped JSON file
    elif user_input.lower() == "save":
        filename = f"music_discussion_{datetime.now().strftime('%d%m%Y_%H%M%S')}.json"
        with open(filename, "w") as f:
            json.dump(history, f, indent=4)
        print(f"Conversation saved to {filename}.\n")

    # Normal Query
    # Appends the user message to history and sends the full
    # conversation context to the model for a response
    else:
        prompt = {"role": "user", "parts": [{"text": user_input}]}
        history.append(prompt)

        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=history,
            config=types.GenerateContentConfig(system_instruction=system_instruction),
        )

    # Extract the model's response text
    musi_disc_res = response.text

    # Append the model's response to history to maintain conversation context
    history.append({"role": "model", "parts": [{"text": musi_disc_res}]})

    print("Music Teacher:", musi_disc_res, "\n")
