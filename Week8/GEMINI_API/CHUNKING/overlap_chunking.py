import os
from google import genai


# Gemini setup

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
MODEL_NAME = "gemini-2.5-flash"


# Chunking with overlap
def chunk_text_with_overlap(text, chunk_size=1000, overlap=200):
    chunks = []
    step = chunk_size - overlap

    for i in range(0, len(text), step):
        chunk = text[i:i + chunk_size]
        if chunk:
            chunks.append(chunk)

        if i + chunk_size >= len(text):
            break

    return chunks


# Gemini processing
def process_long_text(text):
    chunks = chunk_text_with_overlap(text, chunk_size=1000, overlap=200)
    partial_results = []

    for index, chunk in enumerate(chunks, start=1):
        prompt = f"""
Read this text chunk and summarize the important points.

Chunk {index}:
{chunk}
"""
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )
        partial_results.append(response.text)

    final_prompt = "Combine these summaries into one final summary:\n\n" + "\n\n".join(partial_results)

    final_response = client.models.generate_content(
        model=MODEL_NAME,
        contents=final_prompt
    )

    return final_response.text

# Example
if __name__ == "__main__":
    long_text = """
    Artificial intelligence is changing many industries. It is used in healthcare,
    education, finance, cybersecurity, robotics, and automation. Large language models
    have context limits, so chunking becomes important when processing long documents.
    """ * 20

    result = process_long_text(long_text)
    print(result)
