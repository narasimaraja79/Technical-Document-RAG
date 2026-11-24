
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
    top_k=5,
    document_name=None
):
    query_embedding = generate_embeddings([query])
    query_embedding = np.array(
        query_embedding
    ).astype("float32")

    # Search a limited number of nearest chunks
    search_k = min(index.ntotal, 20)

    distances, indices = index.search(
        query_embedding,
        search_k
    )

    results = []

    for rank, i in enumerate(indices[0]):

        if i == -1:
            continue

        chunk = chunks[i]

        # Filter by selected PDF
        if document_name is not None:
            if chunk["document_name"] != document_name:
                continue

        results.append(chunk)

        print(
            f"Rank: {rank + 1}, "
            f"Distance: {distances[0][rank]:.4f}, "
            f"Document: {chunk['document_name']}, "
            f"Page: {chunk['page_number']}"
        )

        if len(results) >= top_k:
            break

    print("Retrieved documents:", len(results))

    return results



