**RAG** stands for **Retrieval-Augmented Generation**. It's a technique that makes large language models (LLMs) more accurate by allowing them to retrieve relevant information from external sources before generating a response.

Here's the basic workflow:

1. **User asks a question**
   - Example: "What is our company's vacation policy?"

2. **Retrieve relevant information**
   - Instead of relying only on what the model learned during training, a retrieval system searches a knowledge source (such as documents, PDFs, a database, or a wiki) for the most relevant content.

3. **Augment the prompt**
   - The retrieved passages are added to the model's prompt as context.

4. **Generate an answer**
   - The LLM answers using both its general knowledge and the retrieved information.

### Simple example

Without RAG:

> User: "What's the warranty period for Product X?"

The model may guess or admit it doesn't know.

With RAG:

- Search finds the warranty document.
- The document states: "Product X includes a 3-year limited warranty."
- The model answers:

  > "According to the product documentation, Product X includes a 3-year limited warranty."

### Why use RAG?

RAG offers several advantages:

- **More accurate**: Answers are grounded in actual documents.
- **Up-to-date**: You can update the knowledge base without retraining the model.
- **Reduced hallucinations**: The model is less likely to invent facts.
- **Private knowledge**: The model can answer questions about internal company documents, customer data, or proprietary manuals.

### Typical RAG architecture

```text
                User Query
                     │
                     ▼
           Convert query to embedding
                     │
                     ▼
            Vector database search
      (find the most relevant documents)
                     │
                     ▼
        Retrieved documents + User query
                     │
                     ▼
               Large Language Model
                     │
                     ▼
               Final grounded answer
```

### Common components

- **Embedding model**: Converts text into numerical vectors.
- **Vector database**: Stores document embeddings for similarity search (e.g., Pinecone, Weaviate, Milvus, or Qdrant).
- **Retriever**: Finds the most relevant documents based on the query.
- **LLM**: Generates the final answer using the retrieved context.

### Where RAG is used

RAG is widely used for:

- AI chatbots that answer questions from company documentation
- Customer support assistants
- Legal and financial document search
- Medical knowledge assistants
- Enterprise search across internal knowledge bases
- Code assistants that search documentation and repositories before answering

In short, **RAG combines search with generative AI**. Rather than depending solely on what the model memorized during training, it first looks up relevant information and then uses that information to produce a more reliable, context-aware response.
