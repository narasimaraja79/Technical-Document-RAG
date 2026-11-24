
# RAG System Evaluation Report

## 1. Project Overview

The Technical Document Question Answering System uses
Retrieval-Augmented Generation (RAG) to answer questions
from multiple PDF documents.

## 2. Technologies Used

- Python
- PyMuPDF
- Sentence Transformers
- all-MiniLM-L6-v2
- FAISS Vector Database
- Ollama
- Qwen2.5 0.5B
- Streamlit

## 3. Evaluation Test Cases

| Test | Evaluation Type | Expected Result |
|---|---|---|
| 1 | Single PDF question | Relevant answer |
| 2 | Second PDF question | Relevant answer |
| 3 | Cross-document question | Information from both PDFs |
| 4 | Document-specific search | Correct PDF source |
| 5 | Out-of-document question | Refusal or no relevant information |

## 4. Evaluation Observations

- Multiple PDF uploads are supported.
- PDF text is extracted using PyMuPDF.
- Text is divided into chunks.
- Sentence embeddings are generated.
- FAISS retrieves relevant document chunks.
- Ollama generates answers using retrieved context.
- Source filenames and page numbers are displayed.
- Document-specific retrieval is implemented.
- A similarity threshold is used to filter distant results.

## 5. Limitations

- Small language models may generate inaccurate answers.
- Retrieval quality depends on chunking and embedding quality.
- Similarity threshold requires further evaluation.
- Complex questions involving multiple documents may need better retrieval.

## 6. Future Improvements

- Improve retrieval accuracy.
- Experiment with different embedding models.
- Add reranking.
- Improve answer grounding.
- Optimize vector database storage.
- Add automated evaluation metrics.

## 7. Conclusion

The project demonstrates a multi-document RAG-based
question-answering system using open-source technologies.
It retrieves information from uploaded PDF documents
and generates answers with source references.
