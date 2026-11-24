
# 📚 Technical Document Question Answering System Using RAG

## 1. Project Overview

This project implements a Retrieval-Augmented Generation (RAG)
based question-answering system that allows users to ask
questions from multiple PDF documents.

The system extracts text from PDF files, splits the text
into smaller chunks, generates embeddings, retrieves relevant
information using FAISS, and generates answers using a
locally running Large Language Model (LLM).

The application also displays source document names and
page numbers for reference.

## 2. Objectives

- Build a question-answering system for technical documents.
- Support multiple PDF document uploads.
- Retrieve relevant information using semantic search.
- Generate answers using an open-source LLM.
- Display source references for generated answers.
- Reduce unsupported answers through context-based generation.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend development |
| PyMuPDF | PDF text extraction |
| Sentence Transformers | Text embeddings |
| all-MiniLM-L6-v2 | Embedding model |
| FAISS | Vector database and similarity search |
| Ollama | Local LLM execution |
| Qwen2.5 0.5B | Answer generation |
| Streamlit | User interface |
| NumPy | Numerical operations |

## 4. System Architecture

User uploads PDF documents
        ↓
PDF Text Extraction (PyMuPDF)
        ↓
Text Chunking
        ↓
Embedding Generation
        ↓
FAISS Vector Database
        ↓
User Question
        ↓
Question Embedding
        ↓
Semantic Retrieval
        ↓
Relevant Context
        ↓
Ollama LLM (Qwen2.5 0.5B)
        ↓
Generated Answer
        ↓
Source References

## 5. Methodology

### Step 1: Document Loading

PyMuPDF extracts text from uploaded PDF documents.
Document names and page numbers are stored as metadata.

### Step 2: Text Chunking

Extracted text is divided into smaller chunks.

Current parameters:
- Chunk size: 500 characters
- Chunk overlap: 100 characters

### Step 3: Embedding Generation

The Sentence Transformers model
all-MiniLM-L6-v2 converts text chunks into numerical
vector representations.

Embedding dimension: 384.

### Step 4: Vector Database

FAISS stores the generated embeddings and performs
similarity searches to retrieve relevant chunks.

### Step 5: Answer Generation

Ollama runs the Qwen2.5 0.5B model locally.
The retrieved context and user question are passed
to the model to generate an answer.

### Step 6: Source References

The application displays:
- Source PDF filename
- Page number
- Retrieved text evidence

## 6. Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Navigate into the project:

```bash
cd Technical-Document-RAG
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install and start Ollama separately, then download the model:

```bash
ollama pull qwen2.5:0.5b
```

## 7. Run the Application

```bash
streamlit run app.py
```

Upload PDF documents, select a document or all documents,
enter a question and click Ask.

## 8. Evaluation

The system is tested using:

- Single-document questions.
- Multiple-document questions.
- Cross-document comparison questions.
- Document-specific retrieval.
- Questions outside the uploaded documents.

Actual test results should be recorded in
evaluation_report.md.

### BEIR SciFact Benchmark Results

The retrieval component was evaluated using the BEIR SciFact dataset.

| Metric | Score |
|---|---:|
| NDCG@10 | 0.6451 |
| MAP@10 | 0.5959 |
| Recall@10 | 0.7833 |
| Precision@10 | 0.0883 |
| MRR@10 | 0.6047 |

**Evaluation details:**
- Dataset: BEIR SciFact
- Corpus documents: 5,183
- Evaluated queries: 300
- Embedding model: all-MiniLM-L6-v2
- Retrieval method: Dense vector retrieval using cosine similarity
- Top-K: 10

These results provide a baseline for measuring semantic document retrieval performance. They do not measure the factual accuracy of generated answers.


## 9. Limitations

- Small language models can generate inaccurate answers.
- Retrieval performance depends on document chunking
  and embedding quality.
- The similarity threshold requires dataset-specific tuning.
- Complex questions may require improved retrieval methods.

## 10. Future Enhancements

- Add reranking for improved retrieval.
- Improve hallucination detection.
- Support additional document formats.
- Add automated retrieval evaluation metrics.
- Optimize vector database persistence.

## 11. Conclusion

This project demonstrates a local, multi-document
question-answering system using Retrieval-Augmented
Generation and open-source tools.

It combines semantic search with LLM-based generation
to answer questions from technical PDF documents
while providing source references.

## BEIR Benchmark Evaluation

The retrieval component was evaluated using the BEIR SciFact dataset.

| Metric | Score |
|---|---:|
| NDCG@10 | 0.6451 |
| MAP@10 | 0.5959 |
| Recall@10 | 0.7833 |
| Precision@10 | 0.0883 |
| MRR@10 | 0.6047 |

**Evaluation details:**
- Dataset: BEIR SciFact
- Corpus documents: 5,183
- Evaluated queries: 300
- Embedding model: all-MiniLM-L6-v2
- Retrieval method: Dense vector retrieval using cosine similarity
- Top-K: 10

The results provide a baseline for measuring semantic document retrieval performance. They do not measure the factual accuracy of generated answers.
