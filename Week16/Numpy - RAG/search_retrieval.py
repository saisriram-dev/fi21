import numpy as np

def build_index(X):
    """
    Prepares a dataset of vectors (the 'corpus') for fast similarity search.
    It normalizes all vectors so that later we can use a simple dot product 
    to calculate Cosine Similarity.
    
    Args:
        X (list or np.ndarray): A 2D array where each row is a vector.
    Returns:
        np.ndarray: A 2D array of L2-normalized vectors.
    """
    # 1. Standardize the data type to 32-bit floats. 
    # This is standard for machine learning vectors to save memory and speed up compute.
    X = np.asarray(X, dtype=np.float32)

    # 2. Defensive check: Ensure the data is a 2D matrix (Rows = items, Columns = dimensions)
    if X.ndim != 2:
        raise ValueError("Corpus must have shape (N, d).")

    # 3. Defensive check: Ensure there are no missing (NaN) or infinite values,
    # which would break the math in later steps.
    if not np.isfinite(X).all():
        raise ValueError("Corpus contains NaN or inf.")

    # 4. Handle the edge case of an empty dataset gracefully.
    if X.shape[0] == 0:
        return X

    # 5. Calculate the L2 norm (the geometric length or magnitude) of every vector.
    # axis=1 means we calculate it across the rows.
    # keepdims=True ensures the shape remains (N, 1) instead of flat (N,), 
    # which is required for broadcasting the division in the next step.
    norms = np.linalg.norm(X, axis=1, keepdims=True)

    # 6. Defensive check: A vector of all zeros has a norm of 0. 
    # We cannot divide by zero in the next step, and a zero vector has no direction.
    if np.any(norms == 0):
        raise ValueError("Corpus contains zero vectors.")

    # 7. L2 Normalization: Divide every vector by its own length.
    # Now, every vector in the index has a length of exactly 1.0.
    # This transforms them into "unit vectors" pointing to the surface of a hypersphere.
    return X / norms


def search(index, query, k):
    """
    Searches the index for the 'k' vectors that are most similar to the query.
    Because the index is pre-normalized, we calculate Cosine Similarity 
    using a fast dot product.
    
    Args:
        index (np.ndarray): The normalized dataset returned by build_index().
        query (list or np.ndarray): The vector we want to find matches for.
        k (int): The number of top results to return.
    Returns:
        tuple: (Array of indices of the top-k vectors, Array of their similarity scores)
    """
    # 1. Edge case: If the database is empty, return empty arrays immediately.
    if index.shape[0] == 0:
        return (
            np.empty(0, dtype=np.int64),
            np.empty(0, dtype=np.float32),
        )

    # 2. Standardize the query to 32-bit floats to match the index.
    query = np.asarray(query, dtype=np.float32)

    # 3. Defensive checks on the query data.
    if not np.isfinite(query).all():
        raise ValueError("Query contains NaN or inf.")

    # 4. Calculate the length (magnitude) of the single query vector.
    query_norm = np.linalg.norm(query)

    # 5. Prevent division by zero. A query of all zeros has no direction to compare.
    if query_norm == 0:
        raise ValueError("Query cannot be a zero vector.")

    # 6. Edge case: If the user asks for 0 or negative results, return nothing.
    if k <= 0:
        return (
            np.empty(0, dtype=np.int64),
            np.empty(0, dtype=np.float32),
        )

    # 7. Bound 'k': You can't return more results than there are items in the database.
    k = min(k, index.shape[0])

    # 8. Normalize the query vector to a length of 1.0, just like we did for the index.
    query = query / query_norm

    # 9. The core algorithm: Calculate Cosine Similarity.
    # Because both the index and query are normalized, the Matrix Multiplication (@)
    # performs a dot product. The result is a 1D array of scores between -1 and 1.
    # 1 = perfect match, 0 = orthogonal (unrelated), -1 = exact opposite.
    scores = index @ query

    # 10. Optimization: Find the top 'k' scores without sorting the entire array.
    # argpartition splits the array: everything right of the split is the top 'k',
    # but they are NOT in order yet. This is much faster than np.argsort() for large datasets.
    candidates = np.argpartition(scores, -k)[-k:]

    # 11. Sort ONLY those top 'k' candidates from highest to lowest score.
    # scores[candidates] gets the values. argsort sorts them ascending.
    # [::-1] reverses the array so the highest score is first.
    ordering = np.argsort(scores[candidates])[::-1]
    
    # 12. Apply that sorted ordering to our original candidate indices.
    indices = candidates[ordering]

    # Return the indices of the original dataset, and their exact similarity scores.
    return indices, scores[indices]
