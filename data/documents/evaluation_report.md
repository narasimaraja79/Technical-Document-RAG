
Technical Document Question-Answering System using Retrieval-Augmented Generation (RAG).



| Test | Question | Result |
|---|---|---|
| 1 | What is Retrieval-Augmented Generation? | Answer generated |
| 2 | What are the two main components of RAG? | Partially correct |
| 3 | What is the role of the generator in RAG? | Partially incorrect |
| 4 | What is the role of the retrieval component in RAG? | Pending |
| 5 | Who invented the telephone? | Correctly refused |


- The system extracts PDF content successfully.
- FAISS retrieves relevant document chunks.
- The LLM generates answers using retrieved context.
- The system can refuse questions outside the knowledge base.
- Some answers need improvement in accuracy.


- Improve document chunking.
- Improve retrieval accuracy.
- Optimize the LLM prompt.
- Implement similarity thresholding.
- Improve source citation accuracy.
