# Index-Time vs Query-Time

Vector search has two phases:

1. Index time — prepare the corpus once.
2. Query time — search the prepared corpus for each user query.

---

## 1. Index Time

Index time happens when we build our vector index.

Suppose our corpus has:

- N = number of documents/vectors
- d = embedding dimension

Our corpus matrix is:

    X.shape == (N, d)

Example:

    X.shape == (10000, 768)

This means:

- 10,000 document vectors
- each vector has 768 dimensions

### What do we do at index time?

We normalize every corpus vector:

    norms = np.linalg.norm(
        X,
        axis=1,
        keepdims=True
    )

    X_normalized = X / norms

The result is still:

    X_normalized.shape == (N, d)

But every row now has approximately unit length:

    ||X_normalized[i]|| ≈ 1

### Why do this at index time?

The norm of a corpus vector does not depend on the query.

If we have 10,000 documents and receive 1,000 queries, we do NOT want to
recalculate the 10,000 corpus norms for every query.

Instead:

    INDEX TIME
    corpus
      ↓
    embeddings
      ↓
    normalize rows
      ↓
    store normalized vectors

The expensive reusable work is done once.

---

## 2. Query Time

Query time happens whenever a user searches.

First we create a query embedding:

    q.shape == (d,)

Then normalize the query:

    q_normalized = q / np.linalg.norm(q)

Now calculate similarities against the entire normalized corpus:

    scores = X_normalized @ q_normalized

Shapes:

    (N, d) @ (d,) → (N,)

So we get one similarity score for every document.

Example:

    X_normalized.shape = (10000, 768)
    q_normalized.shape = (768,)

    scores.shape = (10000,)

Then we select the top-k scores.

---

## 3. Why This Separation Matters

The important idea is:

    INDEX TIME
    Do reusable work once.

    QUERY TIME
    Do only the work that depends on the current query.

Corpus normalization depends only on the corpus,
so it belongs at index time.

Query normalization depends on the current query,
so it belongs at query time.

---

## 4. Mental Model

Think of it like this:

    INDEX TIME

    Documents
        ↓
    Embeddings
        ↓
    Row normalization
        ↓
    Normalized index


    QUERY TIME

    User query
        ↓
    Query embedding
        ↓
    Query normalization
        ↓
    Matrix multiplication
        ↓
    Similarity scores
        ↓
    Top-k documents

---

## 5. Key Principle

Move computation from query time to index time whenever:

    1. the computation is expensive
    2. the result can be reused
    3. the computation does not depend on the query

This is one of the first important performance ideas in
vector retrieval and RAG systems.
