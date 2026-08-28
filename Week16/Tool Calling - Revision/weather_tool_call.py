from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def get_weather(location: str) -> dict:
    """Return current weather."""
    return {"temp": 22, "location": location}

decl = types.FunctionDeclaration(
    name="get_weather",
    description="Get weather for a city",
    parameters_json_schema={
        "type": "object",
        "properties": {"location": {"type": "string"}},
        "required": ["location"],
    },
)
tools = [types.Tool(function_declarations=[decl])]

contents = [
    types.Content(role="user", parts=[types.Part.from_text(text="Weather in Paris?")])
]

while True:
    resp = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=contents,
        config=types.GenerateContentConfig(
            tools=tools,
            automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True),
        ),
    )

    if not resp.function_calls:
        print(resp.text)
        break

    contents.append(resp.candidates[0].content)

    for fc in resp.function_calls:
        result = get_weather(**dict(fc.args))
        contents.append(
            types.Content(
                role="user",
                parts=[types.Part.from_function_response(name=fc.name, response=result)],
            )
        )
