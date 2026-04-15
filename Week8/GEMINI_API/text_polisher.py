from google import genai
import os
from dotenv import load_dotenv

# Loading the environment variables from the .env file
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)


while True:
    # Getting user input for the text and the mode of cleaning
    text = input("Enter the text you want to clean:")

    # Creating an exit condition for the loop
    if text.lower() == "exit":
        print("Exiting the program.")
        break

    # Getting user input for the mode
    mode = input("Enter the mode (1. Formal, 2. Friendly, 3. Concise): ")

    # Setting up the system prompt based on the selected mode
    if mode == "1":
        instruction = "Rewrite the text in a formal and professional tone."
    elif mode == "2":
        instruction = "Rewrite the text in a friendly and warm tone."
    elif mode == "3":
        instruction = "Rewrite the text concisely with minimal words."
    else:
        instruction = "Rewrite the text clearly."

    system_prompt = f"{instruction}\n\nOriginal Text:\n{text}\n\nCleaned Text:\n"

    # Getting the response for the cleaned text from the API
    res = client.models.generate_content_stream(
        model="gemini-2.0-flash",
        contents=system_prompt,
        config={
            "temperature": 0.7,
        },
    )

    print("Cleaned Text:\n")
    for stream in res:
        print(stream.text, end="")
    print("\n")  # Print a newline after the cleaned text
