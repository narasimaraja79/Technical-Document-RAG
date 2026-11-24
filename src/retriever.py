
import faiss
import numpy as np
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from embeddings import generate_embeddings


def search_documents(
    query,
    index,
    chunks,
    top_k=3,
    document_name=None
):

    query_embedding = generate_embeddings([query])
    query_embedding = np.array(query_embedding).astype("float32")

    # Search all available vectors
    distances, indices = index.search(
        query_embedding,
        index.ntotal
    )

    print("Retrieval distances:", distances[0][:3])

    results = []

    for rank, i in enumerate(indices[0]):

        if i == -1:
            continue

        distance = distances[0][rank]

        # Similarity threshold
        if distance > 1.2:
            continue

        chunk = chunks[i]

        # Filter by selected PDF
        if document_name is not None:
            if chunk["document_name"] != document_name:
                continue

        results.append(chunk)

        if len(results) >= top_k:
            break

    print("Retrieved documents:", len(results))

    return results


