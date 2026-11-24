
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

    if pdf_paths is None:
        pdf_paths = ["data/documents/rag_research.pdf"]

    # Build vector database
    index, chunks = build_pdf_vector_store(pdf_paths)

    # Retrieve relevant chunks
    results = search_documents(
        query,
        index,
        chunks,
        top_k=5,
        document_name=document_name
    )

    if not results:
        return (
            "I cannot find the answer in the provided document.",
            []
        )

    # Prepare context with source information
    context_parts = []

    for result in results:
        context_parts.append(
            f"""
Document: {result['document_name']}
Page: {result['page_number']}
Content:
{result['text']}
"""
        )

    context = "\n\n".join(context_parts)

    # Debug: inspect actual retrieved context
    print("\n========== RETRIEVED CONTEXT ==========")
    print(context)
    print("=======================================")

    # Generate answer
    answer = generate_answer(query, context)

    print("\nUser Question:", query)
    print("\nAI Answer:", answer)

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




