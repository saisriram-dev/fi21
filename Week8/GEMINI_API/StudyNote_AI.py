from google import genai
from dotenv import load_dotenv
import os
import json
import time

# Load the API key from the .env file and initialize the Gemini client
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)

# Setting up the system instruction for the Gemini model
instruction = f"""
For any text given to you, please provide a concise summary in 2-3 sentences. 
The summary should capture the main points and key information from the text.
After that I want you to provide a 5 bullet point list of the most important information from the text.
And at the end I want you to give 3 hard questions that could be asked about the text, along with their answers.
All the output should be in JSON format with the following structure:

{{
    "summary": "Your concise summary here",
    "key_points": [
        "First key point",
        "Second key point",
        "Third key point",
        "Fourth key point",
        "Fifth key point"
    ],
    "questions_and_answers": [
        {{
        "question": "First hard question?",
        "answer": "Answer to the first hard question."
        }},
        {{
        "question": "Second hard question?",
        "answer": "Answer to the second hard question."
        }},
        {{
        "question": "Third hard question?",
        "answer": "Answer to the third hard question."
        }}
    ]
}}

Example 01:
Text: Artificial Intelligence (AI) is rapidly advancing and is being adopted across various 
    industries such as healthcare, finance, and transportation. It helps automate repetitive tasks, 
    improves accuracy in decision-making, and enables predictive analysis using large datasets. 
    However, concerns remain about job displacement, data privacy, and 
    ethical implications of AI systems.

OUTPUT:
{{
    "summary": "Artificial Intelligence is widely used across industries to automate tasks and enhance decision-making. While it improves efficiency and enables predictive analysis, it also raises concerns about job displacement, data privacy, and ethical issues.",
    "key_points": [
        "AI is adopted in industries like healthcare, finance, and transportation",
        "It automates repetitive tasks to improve efficiency",
        "AI enhances decision-making accuracy using data analysis",
        "It enables predictive insights from large datasets",
        "Concerns include job loss, data privacy, and ethical implications"
    ],
"questions_and_answers": [
            {{
            "question": "How does AI contribute to predictive analysis?",
            "answer": "AI uses large datasets and machine learning algorithms to identify patterns and forecast future outcomes."
            }},
            {{
            "question": "What are the risks of AI in terms of employment?",
            "answer": "AI can automate human tasks, reducing the need for certain jobs and potentially causing unemployment in some sectors."
            }},
            {{
            "question": "Why are ethical concerns significant in AI systems?",
            "answer": "Ethical concerns arise due to potential bias, lack of transparency, misuse of data, and unintended consequences of autonomous decisions."
            }}
        ]
}}

"""


# Function to stream the response character by character with a delay
def stream(text, delay=0.01):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


while True:
    # Get user input
    text = input("Enter text: ")

    # Exit the loop if the user types 'exit'
    if text.lower() == "exit":
        print("Keep studying and have a great day!")
        break

    # Prepare the prompt for the Gemini model
    prompt = instruction + "\n\nText: " + text

    # Generate a response from the Gemini model
    response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)

    try:
        data = response.text[response.text.find("{") : response.text.rfind("}") + 1]
        json_data = json.loads(data)

    except json.JSONDecodeError:
        print("Failed to parse JSON response.")

    # Print the response in a streaming manner
    print("-" * 100)
    stream("\nSUMMARY: \n")
    stream(json_data.get("summary", "No summary available."), delay=0.02)
    print("-" * 100)
    print()

    print("-" * 100)
    stream("\nKEY POINTS: \n")
    for point in json_data.get("key_points", []):
        stream(f"-> {point}", delay=0.02)
    print("-" * 100)
    print()

    print("-" * 100)
    stream("\nQUESTIONS AND ANSWERS: \n")
    for qa in json_data.get("questions_and_answers", []):
        stream(f"Q: {qa.get('question', 'No question available.')}", delay=0.02)
        stream(f"A: {qa.get('answer', 'No answer available.')}\n", delay=0.02)
    print()
