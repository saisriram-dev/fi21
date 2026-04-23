import os
from google import genai

# Gemini setup

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
MODEL_NAME = "gemini-2.5-flash"


# Sliding window chat

history = []
MAX_HISTORY = 6  # keep only recent messages


def format_history(messages):
    formatted = []
    for msg in messages:
        role = msg["role"].upper()
        content = msg["content"]
        formatted.append(f"{role}: {content}")
    return "\n".join(formatted)


while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    history.append({"role": "user", "content": user_input})

    # Keep only recent messages
    history = history[-MAX_HISTORY:]

    prompt = f"""
Continue this conversation naturally.

{format_history(history)}

ASSISTANT:
"""

    response = client.models.generate_content(model=MODEL_NAME, contents=prompt)

    reply = response.text
    print("Gemini:", reply)

    history.append({"role": "assistant", "content": reply})
