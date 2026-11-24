# BEIR SciFact Evaluation Report

## 1. Objective

The objective of this evaluation is to measure the document retrieval performance of the Technical Document Question Answering System using the BEIR SciFact benchmark dataset.

## 2. Dataset Details

- Dataset: BEIR SciFact
- Corpus documents: 5,183
- Evaluated queries: 300
- Embedding model: all-MiniLM-L6-v2
- Embedding dimension: 384
- Retrieval method: Dense vector retrieval using cosine similarity
- Top-K: 10

## 3. Evaluation Metrics

The following metrics were used:

| Metric | Result |
|---|---:|
| NDCG@10 | 0.6451 |
| MAP@10 | 0.5959 |
| Recall@10 | 0.7833 |
| Precision@10 | 0.0883 |
| MRR@10 | 0.6047 |

## 4. Results and Observations

- NDCG@10 of 0.6451 indicates the ranking of relevant documents has measurable effectiveness.
- MAP@10 of 0.5959 measures the average precision across the evaluated queries.
- Recall@10 of 0.7833 indicates that the retrieval system found a substantial proportion of relevant documents within the top 10 results.
- Precision@10 of 0.0883 indicates that the average proportion of relevant documents among the 10 retrieved results was relatively low.
- MRR@10 of 0.6047 measures how highly the first relevant result appeared in the rankings.

## 5. Conclusion

The all-MiniLM-L6-v2 embedding model demonstrated useful semantic retrieval performance on the BEIR SciFact dataset.

The results show relatively strong recall, while precision can be improved through better ranking, filtering, and retrieval techniques.

This evaluation provides a quantitative baseline for improving the document retrieval component of the RAG system.

## 6. Limitations

- The evaluation measures document retrieval performance, not the factual correctness of generated answers.
- The experiment uses the SciFact benchmark and does not establish performance on every type of technical document.
- Further evaluation is needed to measure end-to-end answer quality, source accuracy, and hallucination resistance.

## 7. Future Improvements

- Experiment with different embedding models.
- Apply reranking to improve the relevance of retrieved documents.
- Tune the retrieval threshold and top-K value.
- Evaluate generated answers for factual accuracy and context relevance.
