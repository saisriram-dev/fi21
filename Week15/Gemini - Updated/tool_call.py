import google.generativeai as genai

# 1. Define the tool
tools = [
    {
        "function_declarations": [
            {
                "name": "calculate",
                "description": "Evaluates a mathematical expression and returns the result",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "expression": {
                            "type": "string",
                            "description": "The math expression to evaluate, e.g. '(12 * 4) + 7'"
                        }
                    },
                    "required": ["expression"]
                }
            }
        ]
    }
]

# 2. Send a message — Gemini decides to call the tool
model = genai.GenerativeModel("gemini-1.5-pro", tools=tools)
response = model.generate_content("What is (144 / 12) * 7 + 3?")

# 3. Check if Gemini wants to call a function
part = response.candidates[0].content.parts[0]
if part.function_call:
    fn = part.function_call
    print(fn.name)        # → "calculate"
    print(fn.args)        # → {"expression": "(144 / 12) * 7 + 3"}

    # Execute the function yourself
    result = eval(fn.args["expression"])  # → 87

    # Send the result back
    final = model.generate_content([
        {"role": "user", "parts": ["What is (144 / 12) * 7 + 3?"]},
        {"role": "model", "parts": [part]},
        {"role": "function", "parts": [{"function_response": {"name": "calculate", "response": {"result": result}}}]}
    ])
    print(final.text)  # → "The answer is 87."
