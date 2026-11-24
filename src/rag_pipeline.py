

import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from vector_store import build_pdf_vector_store
from retriever import search_documents
from llm_generator import generate_answer


def run_rag_pipeline(
    query,
    pdf_paths=None,
    document_name=None
):

    # Step 1: Select PDF documents
    if pdf_paths is None:
        pdf_paths = ["data/documents/rag_research.pdf"]

    # Step 2: Build vector database
    index, chunks = build_pdf_vector_store(pdf_paths)

    # Step 3: Retrieve relevant chunks
    results = search_documents(
        query,
        index,
        chunks,
        top_k=3,
        document_name=document_name
    )

    if not results:
        return "No relevant information found in the selected document.", []

    # Step 4: Prepare context
    context = "\n\n".join(
        [result["text"] for result in results]
    )

    # Step 5: Generate answer
    answer = generate_answer(query, context)

    print("\nUser Question:", query)
    print("\nAI Answer:", answer)

    # Step 6: Return answer and sources
    return answer, results


if __name__ == "__main__":

    question = input("Ask a question about the PDFs: ")

    answer, sources = run_rag_pipeline(question)

    print("\nAnswer:", answer)

    for source in sources:
        print(
            "Document:", source["document_name"],
            "| Page:", source["page_number"]
        )



