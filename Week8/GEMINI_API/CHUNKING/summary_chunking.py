import os
from google import genai

# Gemini setup

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
MODEL_NAME = "gemini-2.5-flash"

history = []
summary_memory = ""
KEEP_RECENT = 4


def format_history(messages):
    lines = []
    for msg in messages:
        lines.append(f'{msg["role"].upper()}: {msg["content"]}')
    return "\n".join(lines)


def summarize_old_messages(old_messages):
    if not old_messages:
        return ""

    prompt = f"""
Summarize this conversation briefly.
Keep:
- user goal
- important facts
- decisions already made

Conversation:
{format_history(old_messages)}
"""

    response = client.models.generate_content(model=MODEL_NAME, contents=prompt)

    return response.text


while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    history.append({"role": "user", "content": user_input})

    if len(history) > KEEP_RECENT:
        old_messages = history[:-KEEP_RECENT]
        recent_messages = history[-KEEP_RECENT:]

        new_summary = summarize_old_messages(old_messages)

        if summary_memory.strip():
            summary_memory = summary_memory + "\n" + new_summary
        else:
            summary_memory = new_summary
    else:
        recent_messages = history

    prompt = f"""
You are continuing a conversation.

Summary of older conversation:
{summary_memory if summary_memory else "No summary yet."}

Recent conversation:
{format_history(recent_messages)}

ASSISTANT:
"""

    response = client.models.generate_content(model=MODEL_NAME, contents=prompt)

    reply = response.text
    print("Gemini:", reply)

    history.append({"role": "assistant", "content": reply})
