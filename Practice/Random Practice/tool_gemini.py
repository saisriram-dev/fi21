from google import genai
from google.genai import types
import json

# Initialize Gemini
client = genai.Client(api_key="YOUR_GEMINI_API_KEY")


def get_weather(city: str):
    return {"city": city, "temperature": "30°C", "condition": "Sunny"}


weather_tool = types.Tool(
    function_declarations=[
        types.FunctionDeclaration(
            name="get_weather",
            description="Get the current weather of a city.",
            parameters={
                "type": "OBJECT",
                "properties": {"city": {"type": "STRING", "description": "City name"}},
                "required": ["city"],
            },
        )
    ]
)


response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="What's the weather in Tokyo?",
    config=types.GenerateContentConfig(tools=[weather_tool]),
)


part = response.candidates[0].content.parts[0]

if hasattr(part, "function_call") and part.function_call:

    function_name = part.function_call.name
    args = dict(part.function_call.args)

    print("Gemini called:", function_name)
    print("Arguments:", args)

    # Execute the function
    if function_name == "get_weather":
        result = get_weather(**args)

    # Send function result back
    response2 = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            response.candidates[0].content,
            types.Content(
                role="user",
                parts=[
                    types.Part.from_function_response(
                        name=function_name,
                        response=result,
                    )
                ],
            ),
        ],
        config=types.GenerateContentConfig(tools=[weather_tool]),
    )

    print(response2.text)

else:
    print(response.text)
