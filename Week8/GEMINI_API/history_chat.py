from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

history = []

print("Type 'exit' to stop.\n")

while True:
    user_text = input("You: ").strip()

    if user_text.lower() in {"exit", "quit"}:
        print("Ending chat.")
        break

    if not user_text:
        continue

    # 1) Add user message to history
    history.append({
        "role": "user",
        "parts": [{"text": user_text}]
    })

    # 2) Send the FULL history every time
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=history
    )

    ai_text = response.text
    print("AI:", ai_text, "\n")

    # 3) Add model response to history
    history.append({
        "role": "model",
        "parts": [{"text": ai_text}]
    })
