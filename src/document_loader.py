import pymupdf
import os

def load_pdf(file_path):

    documents = []

    pdf_document = pymupdf.open(file_path)

    for page_number, page in enumerate(pdf_document):

        text = page.get_text()

        if text.strip():

            documents.append({
                "document_name": os.path.basename(file_path),
                "page_number": page_number + 1,
                "text": text
            })

    pdf_document.close()

    return documents


if __name__ == "__main__":

    pdf_path = "data/documents/rag_research.pdf"

    pages = load_pdf(pdf_path)
    import os

    print("Current directory:", os.getcwd())
    print("PDF exists:", os.path.exists(pdf_path))

    print("Total pages extracted:", len(pages))

    for page in pages[:2]:

        print("\nDocument:", page["document_name"])
        print("Page:", page["page_number"])
        print("Text:", page["text"][:500])
