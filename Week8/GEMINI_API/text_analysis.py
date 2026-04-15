from google import genai
from dotenv import load_dotenv
import os
import json

# Loading the environment variables from the .env file
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Initializing the gemini client with the API key
client = genai.Client(api_key=API_KEY)

# Creating the instruction for the Gemini API
instruction = f"""
I want you to analyze the given text and give me the following information in a structured format and I don't want any explanation, just the output:
Analyze the given text and respond ONLY with valid JSON.
Required format:
{{
    "Main Topic": "",
    "Sentiment": "",
    "Key Facts": ["", "", ""]
}}

Do not include any explanation, markdown, or extra text.

To make it easier for you, I will provide you with an example of the expected output format:
Paragraph 01:
Artificial Intelligence is rapidly changing the way businesses operate. 
Companies are using AI to automate repetitive tasks and improve efficiency. 
However, there are concerns about job losses and ethical implications.

Output:
{{
    "Main Topic": "Artificial Intelligence in business",
    "Sentiment": "Neutral",
    "Key Facts":["1. AI is automating repetitive tasks",
                "2. Businesses use AI to improve efficiency",
                "3. There are concerns about job loss and ethics"]
}}


Paragraph 02:
Electric vehicles are becoming more popular due to rising fuel costs and environmental concerns.
Governments are offering incentives to encourage adoption. Charging infrastructure is still 
developing in many regions.

Output:
{{
    "Main Topic": "Growth of electric vehicles",
    "Sentiment": "Positive",
    "Key Facts": ["1. EVs are gaining popularity",
                "2. Governments offer incentives",
                "3. Charging infrastructure is still developing"]
}}

Paragraph 03:
Online education has expanded significantly in recent years. 
It provides flexibility and accessibility to students worldwide. 
However, some learners face challenges such as lack of interaction and self-discipline.

Output:
{{
    "Main Topic": "Online education",
    "Sentiment": "Neutral",
    "Key Facts": ["1. Online education is growing rapidly",
                "2. It offers flexibility and accessibility",
                "3. Students face challenges like low interaction and discipline"]
}}

Now, please analyze the following text and provide the output in the same format as the examples above:
Paragraph 04:

"""

while True:
    # Taking user_input for the prompt
    text = input("Enter the text you want to analyze (or 'exit' to quit): ")

    # Checking if the user wants to exit the program
    if text.lower() == "exit":
        print("Exiting the program. Goodbye!")
        break

    # Crearing the prompt by appending the user input to the instruction
    prompt = instruction + text

    # Creating a request to the Gemini API with the user input
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    # Printing the response from the Gemini API
    try:
        output = response.text.strip()
        output = output[output.find("{") : output.rfind("}") + 1]
        output_json = json.loads(output)
        print(output_json)
    except json.JSONDecodeError:
        print("Error: The response is not in the expected JSON format.")
        print("Raw response:", response.text)
