from fastapi import FastAPI
from pydantic import BaseModel
# from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

# Mount the static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# # List of allowed origins for CORS
# origins = ["http://127.0.0.1:5500", "http://localhost:5500", "http://127.0.0.1:8000"]

# # Add CORS middleware to allow requests from the frontend
# # This is required to allow the frontend to make requests to the backend
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


# Define the request model
# If we get a JSON object with a "text" field, we can use this model
# Eg. {"text": "Hello"} is Query(text="Hello") and we can access it as Query.text
class Query(BaseModel):
    text: str


# Serving the UI
@app.get("/")
def serve_ui():
    return FileResponse("static/index.html")

@app.post("/query")
def process_query(query: Query):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=f"""
            Answer clearly using markdown.
            Use headings, bullet points, and spacing.

            {query.text}
            """,
        )

        return {"result": response.text}

    except Exception as e:
        return {"Error": str(e)}
