# NumPy Vector Search: Important Dimensions

Shape reasoning is one of the most important skills in NumPy vector search.

Always write down the shapes before writing the operation.

---

## 1. Corpus Matrix

    X.shape == (N, d)

Where:

    N = number of vectors/documents
    d = number of dimensions in each vector

Example:

    X.shape == (10000, 768)

means:

    10,000 vectors
    768 dimensions per vector

Think:

              dimensions
             ←──────────→
    vector 1  [ . . . . ]
    vector 2  [ . . . . ]
    vector 3  [ . . . . ]
       ...
    vector N  [ . . . . ]

---

## 2. Query Vector

A single query vector has shape:

    q.shape == (d,)

Example:

    q.shape == (768,)

It contains 768 numbers.

Important:

    (768,)

is a 1-D NumPy array.

It is NOT:

    (1, 768)

Those two shapes behave differently in some operations.

---

## 3. Row Norms

We need one norm for each corpus vector.

Corpus:

    X.shape == (N, d)

We reduce across the dimensions of each row:

    np.linalg.norm(X, axis=1)

Result:

    (N,)

If we use:

    keepdims=True

then:

    np.linalg.norm(
        X,
        axis=1,
        keepdims=True
    )

has shape:

    (N, 1)

The `(N, 1)` shape is useful for broadcasting.

---

## 4. Why axis=1?

Remember the actual question:

    "Which dimension am I reducing?"

For:

    X.shape == (N, d)

each row is one vector.

To calculate one norm per vector, we combine its d dimensions.

Therefore:

    axis=1

produces:

    (N, d)
       ↓
    (N, 1)

Do NOT memorize "axis=1 means rows."

Instead ask:

    "Which dimension do I want to collapse?"

---

## 5. Normalized Corpus

We have:

    X          → (N, d)
    norms      → (N, 1)

Then:

    X / norms

produces:

    (N, d)

Broadcasting lets each row be divided by its own norm.

So:

    X_normalized.shape == (N, d)

---

## 6. Normalized Query

The query starts as:

    q.shape == (d,)

After normalization:

    q_normalized.shape == (d,)

Normalizing does not change its shape.

---

## 7. Similarity Scores

The main vector-search operation is:

    scores = X_normalized @ q_normalized

Shapes:

    (N, d) @ (d,) → (N,)

This means:

    every corpus vector
        ×
    the query vector
        ↓
    one score per corpus vector

Therefore:

    scores.shape == (N,)

If N = 10,000:

    scores.shape == (10000,)

There are 10,000 similarity scores.

---

## 8. Top-k Result

We do not need all N results.

Suppose:

    k = 5

Then the selected indices have shape:

    (5,)

and the selected scores have shape:

    (5,)

Example:

    indices.shape == (5,)
    scores.shape  == (5,)

These represent the 5 most similar vectors.

---

## 9. The Shape Pipeline

Memorize this pipeline:

    Corpus
    (N, d)
       ↓
    row norms
    (N, 1)
       ↓
    normalized corpus
    (N, d)

    Query
    (d,)
       ↓
    normalized query
    (d,)

    Similarity
    (N, d) @ (d,)
       ↓
    (N,)

    Top-k
    (N,)
       ↓
    (k,)

---

## 10. Most Important Shapes to Remember

    Corpus             → (N, d)
    Query              → (d,)
    Row norms          → (N, 1)
    Normalized corpus  → (N, d)
    Normalized query   → (d,)
    All scores         → (N,)
    Top-k indices      → (k,)
    Top-k scores       → (k,)

---

## 11. The Golden Rule

Whenever confused about axis or shapes:

    STOP.

Write down:

    What is the current shape?
    What should the output shape be?
    Which dimension am I reducing?

Do not guess axis=0 or axis=1.

Reason from the shapes.
