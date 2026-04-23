# pdf_qa.py — AI-powered PDF Question Answering
# Extracts text from any PDF, injects it as context,
# then lets the user ask questions about it using Gemini.

from google import genai
from google.genai import types
from dotenv import load_dotenv
import pypdf
import os
import sys

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)

MAX_CHUNK_CHARS = 400_000  # Gemini 1.5 Flash handles ~1M tokens; this is safe


def extract_text_from_pdf(filepath: str) -> str:
    """Extract all text from a PDF file using pypdf."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"No file found at: {filepath}")

    reader = pypdf.PdfReader(filepath)
    pages = []

    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            pages.append(f"[Page {i + 1}]\n{text}")

    if not pages:
        raise ValueError("No readable text found in this PDF.")

    return "\n\n".join(pages)


def chunk_text(text: str, max_chars: int = MAX_CHUNK_CHARS) -> list[str]:
    """Split text into chunks if it exceeds the safe context size."""
    if len(text) <= max_chars:
        return [text]

    chunks = []
    while text:
        chunks.append(text[:max_chars])
        text = text[max_chars:]
    return chunks


def build_system_prompt(document_text: str) -> str:
    """Build a system prompt that injects the document as context."""
    return f"""You are a precise document assistant. 
You have been given the following document to answer questions about.
Only answer based on what is in the document.
If the answer is not in the document, say "I could not find that in the document."
If you are quoting, mention the page number.

--- DOCUMENT START ---
{document_text}
--- DOCUMENT END ---
"""


def answer_question(question: str, system_prompt: str) -> str:
    """Send a question to Gemini with the document as context."""
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[{"role": "user", "parts": [{"text": question}]}],
        config=types.GenerateContentConfig(system_instruction=system_prompt),
    )
    return response.text


def main():
    # Get PDF path from command line or prompt user
    if len(sys.argv) > 1:
        pdf_path = sys.argv[1]
    else:
        pdf_path = input("Enter path to your PDF file: ").strip()

    print(f"\nLoading PDF: {pdf_path}")

    try:
        full_text = extract_text_from_pdf(pdf_path)
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
        sys.exit(1)

    chunks = chunk_text(full_text)
    total_chars = len(full_text)

    print(f"Loaded {total_chars:,} characters across {len(chunks)} chunk(s).")
    print("If your document is large, answers will use the first chunk only.\n")

    # Use only the first chunk for now (covers 99% of real-world PDFs)
    system_prompt = build_system_prompt(chunks[0])

    print("PDF loaded. Ask anything about it. Type 'quit' to exit.\n")
    print("-" * 50)

    while True:
        question = input("Your question: ").strip()

        if not question:
            print("Please enter a question.\n")
            continue

        if question.lower() in ["quit", "exit"]:
            print("Goodbye!")
            break

        if question.lower() == "info":
            print(f"Document size: {total_chars:,} characters")
            print(f"Chunks: {len(chunks)}")
            print(f"Pages: approx {full_text.count('[Page ')}\n")
            continue

        try:
            print("\nAnswering...")
            answer = answer_question(question, system_prompt)
            print(f"\nAnswer: {answer}\n")
            print("-" * 50)
        except Exception as e:
            print(f"API error: {e}\n")


if __name__ == "__main__":
    main()
