
import os
import json
import numpy as np
from datasets import load_dataset

# Add src folder to Python path
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from embeddings import model


def run_beir_evaluation():

    print("Loading SciFact dataset from Hugging Face...")

    # Load corpus and queries
    corpus_data = load_dataset(
        "BeIR/scifact",
        "corpus",
        split="corpus"
    )

    queries_data = load_dataset(
        "BeIR/scifact",
        "queries",
        split="queries"
    )

    qrels_data = load_dataset(
        "BeIR/scifact-qrels",
        split="test"
    )

    # Prepare corpus
    document_ids = [str(item["_id"]) for item in corpus_data]

    document_texts = [
        (item.get("title", "") + " " + item.get("text", "")).strip()
        for item in corpus_data
    ]

    # Prepare queries
    queries = {
        str(item["_id"]): item.get("text", "")
        for item in queries_data
    }

    # Prepare relevance judgments
    qrels = {}

    for item in qrels_data:
        query_id = str(item["query-id"])
        doc_id = str(item["corpus-id"])

        if int(item["score"]) > 0:
            qrels.setdefault(query_id, set()).add(doc_id)

    print("Documents:", len(document_ids))
    print("Queries:", len(queries))
    print("Generating document embeddings...")

    document_embeddings = model.encode(
        document_texts,
        batch_size=32,
        show_progress_bar=True,
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    # Evaluate retrieval
    metric_totals = {
        "NDCG@10": 0,
        "MAP@10": 0,
        "Recall@10": 0,
        "Precision@10": 0,
        "MRR@10": 0
    }

    evaluated = 0

    for query_id, relevant_docs in qrels.items():

        if query_id not in queries:
            continue

        query_embedding = model.encode(
            [queries[query_id]],
            convert_to_numpy=True,
            normalize_embeddings=True
        )[0]

        scores = np.dot(document_embeddings, query_embedding)

        top_indices = np.argsort(scores)[::-1][:10]

        retrieved = [
            document_ids[index] for index in top_indices
        ]

        hits = [
            1 if doc_id in relevant_docs else 0
            for doc_id in retrieved
        ]

        precision = sum(hits) / 10
        recall = sum(hits) / len(relevant_docs)

        # Average precision
        hit_count = 0
        precision_sum = 0

        for rank, hit in enumerate(hits, start=1):
            if hit:
                hit_count += 1
                precision_sum += hit_count / rank

        average_precision = precision_sum / len(relevant_docs)

        # Reciprocal rank
        reciprocal_rank = 0

        for rank, hit in enumerate(hits, start=1):
            if hit:
                reciprocal_rank = 1 / rank
                break

        # NDCG
        dcg = sum(
            hit / np.log2(rank + 1)
            for rank, hit in enumerate(hits, start=1)
        )

        ideal_count = min(len(relevant_docs), 10)

        idcg = sum(
            1 / np.log2(rank + 1)
            for rank in range(1, ideal_count + 1)
        )

        ndcg = dcg / idcg if idcg else 0

        metric_totals["NDCG@10"] += ndcg
        metric_totals["MAP@10"] += average_precision
        metric_totals["Recall@10"] += recall
        metric_totals["Precision@10"] += precision
        metric_totals["MRR@10"] += reciprocal_rank

        evaluated += 1

    if evaluated == 0:
        raise ValueError("No evaluation queries matched the relevance data.")

    results = {
        metric: round(value / evaluated, 4)
        for metric, value in metric_totals.items()
    }

    results["Dataset"] = "BEIR SciFact"
    results["Evaluated Queries"] = evaluated
    results["Corpus Documents"] = len(document_ids)
    results["Embedding Model"] = "all-MiniLM-L6-v2"

    os.makedirs("results", exist_ok=True)

    with open(
        "results/beir_evaluation.json",
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(results, file, indent=4)

    print("\nBEIR SCIFACT EVALUATION RESULTS")

    for key, value in results.items():
        print(f"{key}: {value}")

    print("\nResults saved to results/beir_evaluation.json")


if __name__ == "__main__":
    run_beir_evaluation()
