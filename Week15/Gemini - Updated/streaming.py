from fastapi import FastAPI
from google import genai
from fastapi.responses import StreamingResponse
from google.genai import types
from dotenv import load_dotenv
import os

app = FastAPI()

load_dotenv()
client = genai.Client(api_key=os.getenve("GEMINI_API_KEY"))

def generate():
    res = client.generate_content_stream(
        model="some_model",
        config=types.GenerateConfig(system_prompt="Some system prompt", 
                                    max_output_tokens=100)
    )

    for chunk in res:
        if chunk.text:
            yield chunk.text

# StreamingResponse is used to stream the response back to the client as it is generated
@app.get("/stream")
async def stream():
    return StreamingResponse(
        generate(), 
        media_type="text/plain"
    )
