from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from dotenv import load_dotenv
from google import genai
import os

load_dotenv()
app = FastAPI()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Add CORS middleware
"""
What each line means:
- allow_origins: List of origins that are allowed to make requests to this server
- allow_methods: List of HTTP methods that are allowed to be used
- allow_headers: List of headers that are allowed to be used
"""
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# Serve index.html at the root URL
@app.get("/")
def root():
    return FileResponse("index.html")


# Define request model
# We can now access text like an attribute of the query object
class Query(BaseModel):
    text: str


@app.post("/query")
def query(query: Query):

    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=query.text
    )

    return {"text": response.text}
