
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from document_loader import load_pdf



def chunk_text(text, chunk_size=500, overlap=100):
    import re

    sentences = re.split(r'(?<=[.!?])\s+', text)

    chunks = []
    current_chunk = ""

    for sentence in sentences:
        if len(current_chunk) + len(sentence) <= chunk_size:
            current_chunk += sentence + " "
        else:
            if current_chunk.strip():
                chunks.append(current_chunk.strip())

            overlap_text = current_chunk[-overlap:] if overlap else ""
            current_chunk = overlap_text + sentence + " "

    if current_chunk.strip():
        chunks.append(current_chunk.strip())

    return chunks



def create_document_chunks(file_path):
    pages = load_pdf(file_path)
    all_chunks = []

    for page in pages:
        page_chunks = chunk_text(page["text"])

        for chunk in page_chunks:
            all_chunks.append({
                "document_name": page["document_name"],
                "page_number": page["page_number"],
                "text": chunk
            })

    return all_chunks


if __name__ == "__main__":
    pdf_path = "data/documents/rag_research.pdf"

    document_chunks = create_document_chunks(pdf_path)

    print("Total chunks created:", len(document_chunks))

    for i, chunk in enumerate(document_chunks[:3]):
        print(f"\nChunk {i + 1}")
        print("Document:", chunk["document_name"])
        print("Page:", chunk["page_number"])
        print("Text:", chunk["text"][:200])
