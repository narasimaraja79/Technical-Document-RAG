
import faiss
import numpy as np
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from text_chunker import create_document_chunks
from embeddings import generate_embeddings


def create_vector_store(embeddings):

    embeddings = np.array(embeddings).astype("float32")

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    return index


def build_pdf_vector_store(pdf_paths):

    all_chunks = []

    # Process multiple PDF documents
    for pdf_path in pdf_paths:

        chunks = create_document_chunks(pdf_path)

        all_chunks.extend(chunks)

    if not all_chunks:
        raise ValueError("No readable text found in the uploaded PDFs.")

    # Generate embeddings
    texts = [chunk["text"] for chunk in all_chunks]

    embeddings = generate_embeddings(texts)

    # Create FAISS vector database
    index = create_vector_store(embeddings)

    # Save vector database
    os.makedirs("vectorstore", exist_ok=True)

    faiss.write_index(index, "vectorstore/document.index")

    print("PDF embeddings stored successfully!")
    print("Total documents:", len(pdf_paths))
    print("Total chunks:", len(all_chunks))
    print("Total vectors:", index.ntotal)

    return index, all_chunks


if __name__ == "__main__":

    pdf_paths = ["data/documents/rag_research.pdf"]

    build_pdf_vector_store(pdf_paths)

