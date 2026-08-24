import numpy as np


def build_index(corpus):
    """
    corpus: shape (N, d)
    returns normalized corpus: shape (N, d)
    """
    norms = np.linalg.norm(
        corpus,
        axis=1,
        keepdims=True,
    )

    norms = np.maximum(norms, 1e-12)

    return corpus / norms


def search(index, query, k):
    """
    index: shape (N, d), already normalized
    query: shape (d,)
    returns:
        indices: shape (k,)
        scores:  shape (k,)
    """
    query_norm = np.linalg.norm(query)

    if query_norm == 0:
        raise ValueError("Query vector must be non-zero.")

    query_normalized = query / query_norm

    # (N, d) @ (d,) -> (N,)
    scores = index @ query_normalized

    # Find the k largest scores without fully sorting N values.
    candidate_indices = np.argpartition(
        scores,
        -k,
    )[-k:]

    # Sort only the k selected candidates.
    ordering = np.argsort(
        scores[candidate_indices]
    )[::-1]

    indices = candidate_indices[ordering]
    top_scores = scores[indices]

    return indices, top_scores
