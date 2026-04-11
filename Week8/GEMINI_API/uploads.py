from google import genai
import os
from dotenv import load_dotenv

# Load the API key from the .env file
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize the Gemini client with the API key
client = genai.Client(api_key=API_KEY)

# Upload a file to the Gemini API
uploaded_file = client.files.upload(file="Week8/GEMINI_API/Screenshot (684).png")

# Getting a response regarding the uploaded file
res = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=["What is in this image?", uploaded_file]
)

print(res.text)
