import numpy as np

def cosine_similarity(query_vector, document_vectors):

    query_norm = np.linalg.norm(query_vector)

    document_norms = np.linalg.norm(
        document_vectors,
        axis =1
    )

    scores=np.dot(
        document_vectors,
        query_vector
    ) / (
        document_norms * query_norm
    )

    return scores