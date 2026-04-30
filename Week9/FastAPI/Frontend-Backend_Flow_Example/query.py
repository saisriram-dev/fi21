from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

class Query(BaseModel):
    text: str

@app.post("/query")
def process_query(query: Query):
    response = client.models.generate_content(
        model="gemini-2.0",
        contents=query.text
    )
    return {"result": response.text}
