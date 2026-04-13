from google import genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)


# 🎯 Core function (reusable engine)
def clean_text(text: str, mode: str) -> str:
    mode_map = {
        "formal": "Rewrite the text in a formal and professional tone.",
        "friendly": "Rewrite the text in a friendly and warm tone.",
        "concise": "Rewrite the text concisely with minimal words."
    }

    instruction = mode_map.get(mode.lower(), "Rewrite the text clearly.")

    prompt = f"""
{instruction}

Original Text:
{text}

Return only the rewritten text. Do not include labels or explanations.
"""

    response = client.models.generate_content_stream(
        model="gemini-2.0-flash",
        contents=prompt,
        config={
            "temperature": 0.7
        }
    )

    result = ""
    for chunk in response:
        if chunk.text:
            print(chunk.text, end="", flush=True)
            result += chunk.text

    print("\n")
    return result


# 🎛️ Input parser (supports "mode: text")
def parse_input(user_input: str):
    if ":" in user_input:
        mode, text = user_input.split(":", 1)
        return mode.strip(), text.strip()
    else:
        return None, user_input.strip()


# 🧠 Main loop
def main():
    print("✨ AI Text Cleaner")
    print("Type 'exit' to quit")
    print("Use format: formal: your text OR just type text\n")

    while True:
        user_input = input(">> ")

        if user_input.lower() == "exit":
            print("👋 Exiting. Stay sharp.")
            break

        mode, text = parse_input(user_input)

        # Ask mode if not provided inline
        if mode is None:
            mode = input("Mode (formal/friendly/concise): ").strip()

        print("\n✨ Cleaned Text:\n")
        clean_text(text, mode)


if __name__ == "__main__":
    main()
