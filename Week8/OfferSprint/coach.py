from google import genai
import os
from dotenv import load_dotenv
from prompts import (
    SYSTEM_PROMPT,
    QUESTION_PROMPT,
    EVALUATION_PROMPT,
    TOTAL_EVALUATION_PROMPT,
    FEEDBACK_PROMPT,
)

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)
history = []


def greet():
    name = input("What's your name? ")
    print(f"""
            Hello {name}! I'm your AI interviewer. Let's begin the interview.
            You are free to ask any doubts about the questions you have.
            When you have completed your solution, please type "next" to move to the next question.
            """)


def convo():
    while True:

        response = client.models.generate_content(
            model="gemini-2.0-flash-exp",
            contents=f"Interviewer: {QUESTION_PROMPT}",
            config=types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT)
        )

        print(response.text)
        history.append({"role": "model", "content": response.text})

        user_input = input("You: ")
        history.append({"role": "user", "content": user_input})

        if user_input.lower() == "exit":
            break

        elif user_input.lower() == "next":
            print("Generating feedback...")
            eval = history[len(history)-1]['content']
            response = client.models.generate_content(
                model="gemini-2.0-flash-exp",
                contents=f"Feedback: {FEEDBACK_PROMPT}\n\n{eval}",
                config=types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT)
            )
            print(response.text)
            history.append({"role": "model", "content": response.text})

        elif user_input.lower() == "eval":
            print("Generating evaluation...")
            eval = history[len(history)-1]['content']
            response = client.models.generate_content(
                model="gemini-2.0-flash-exp",
                contents=f"Evaluation: {TOTAL_EVALUATION_PROMPT}\n\n{eval}",
                config=types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT)
            )
            print(response.text)
            history.append({"role": "model", "content": response.text})

        
        
