Here is your 12-week AI backend development roadmap, structured for clarity and easy reference:

- Weeks 1–2: Phase 1: The Asynchronous Backend
  **Goal:** Build a basic CRUD API with FastAPI and PostgreSQL.

**Topics to Master:**
Python async/await, Pydantic validation, FastAPI routing, PostgreSQL basics.

**Where to Learn:**

- **FastAPI:** The Official FastAPI Tutorial (read top-to-bottom).
- **Python Async:** Real Python's "Async IO in Python: A Complete Walkthrough".
- **Pydantic:** Pydantic V2 official documentation.

- Weeks 3–4: Phase 2: Core GenAI & Naive RAG
  **Goal:** Parse a document with Docling, embed the chunks, store them locally in ChromaDB, and generate an answer using Gemini.

**Topics to Master:**
`google-genai` SDK, Gemini embeddings, Docling parsing, ChromaDB, Cosine Similarity with NumPy.

**Where to Learn:**

- **Gemini API:** Google AI for Developers (new `google-genai` Python SDK documentation).
- **Docling:** The IBM Docling GitHub and official docs.
- **Vector Math:** 3Blue1Brown's YouTube series on Linear Algebra (focus on conceptually understanding embeddings and cosine similarity).

- Weeks 5–7: Phase 3: Advanced Retrieval Engine
  **Goal:** Implement a hybrid search pipeline: fetch the top 20 results from Qdrant (vector) and top 20 from BM25 (keyword), fuse them with Reciprocal Rank Fusion (RRF), and rerank the top 5 with BGE to feed to Gemini.

**Topics to Master:**
`rank_bm25`, RRF, Cross-Encoder Reranking (BGE-m3), Qdrant migration.

**Where to Learn:**

- **Hybrid Search & RRF:** Qdrant's blog for conceptual articles on implementation.
- **Reranking:** Hugging Face documentation for the `sentence-transformers` library (how to run BGE locally or via API).
- **Qdrant:** Qdrant's official Python client quickstart.

- Weeks 8–9: Phase 4: Async Processing & Observability
  **Goal:** Move document parsing to a Celery background worker, hook Langfuse into your Gemini calls for tracing, and run a RAGAS evaluation script on your retrieved contexts.

**Topics to Master:**
Redis, Celery (or RQ), Langfuse, RAGAS.

**Where to Learn:**

- **Celery & Redis:** TestDriven.io's "Asynchronous Tasks with FastAPI and Celery".
- **Observability:** Langfuse Documentation (focus on drop-in decorators for Python).
- **Evaluation:** RAGAS Documentation (start with guides on generating synthetic test datasets).

- Weeks 10–12: Phase 5: Production Infra & Monetization
  **Goal:** Containerize your FastAPI app and Celery workers, create a CI/CD pipeline that runs RAGAS evals before allowing a merge, and set up a Stripe checkout webhook.

**Topics to Master:**
Docker, GitHub Actions, Render/Oracle Cloud, Stripe API.

**Where to Learn:**

- **Docker:** Docker's official "Docker for Beginners" guide.
- **CI/CD:** GitHub Actions official quickstart.
- **Stripe:** Stripe's official API documentation for Python ("Checkout" and "Webhooks" guides).
- **Deployment:** Render's documentation for deploying FastAPI and background worker containers.
