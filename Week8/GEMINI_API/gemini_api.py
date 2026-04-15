from google import genai
import os
from dotenv import load_dotenv

# Load the API key from the .env file
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize the Gemini client with the API key
client = genai.Client(api_key=API_KEY)

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="When can I achieve pure happiness?"
)

# We will get the response after the whole content is generated.
print(response.text)

response2 = client.models.generate_content_stream(
    model="gemini-2.5-flash", contents="When can I become a billionaire?"
)

# We will get the response in a stream as it is being generated.
for stream_response in response2:
    print(stream_response.text)
