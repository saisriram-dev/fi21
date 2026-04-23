from google import genai
from google.genai import types
from dotenv import load_dotenv
from interview import InterviewSession
from prompts import get_sys, get_eval
import os

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

role = input("Enter the role you want to be interviewed for: ")

session = InterviewSession(role)
session.add_message(
    "user", f"I am applying for the role of {role}. Please start the interview."
)

system = get_sys(role)
eval_system = get_eval(role)

while True:
    if session.is_complete():
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash-lite",
                contents=session.history,
                config=types.GenerateContentConfig(system_instruction=eval_system),
            )
        except Exception as e:
            print(f"API Error: {e}. Please try again after some time.")
            break

        if not response.text:
            print("Evaluation failed: no response received from model.")
            break

        print("\n" + response.text)
        break

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=session.history,
            config=types.GenerateContentConfig(system_instruction=system),
        )
    except Exception as e:
        print(f"API Error: {e}. Please try again after some time.")
        break

    if not response.text:
        print("Interviewer: [No response received - model may have been filtered. Retrying is recommended.]")
        continue

    print("\n" + "Interviewer: " + response.text + "\n")
    session.add_message("model", response.text)

    user_input = input("Candidate: ")
    session.add_message("user", user_input)
    session.increment_count()
