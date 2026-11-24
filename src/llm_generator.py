


import ollama


def generate_answer(query, context):

    if not context or not context.strip():
        return "I cannot find the answer in the provided document."

    prompt = f"""
You are a reliable technical document question-answering assistant.

STRICT RULES:
1. Answer the question using only the information in the context.
2. Carefully read all context passages before answering.
3. Identify the exact facts that answer the question.
4. Do not use your own outside knowledge.
5. Do not introduce unrelated topics, datasets, or tasks.
6. If the context does not contain enough information,
   respond exactly:
   I cannot find the answer in the provided document.
7. Keep the answer clear, accurate, and concise.
8. Do not guess or make assumptions.

CONTEXT:
{context}

QUESTION:
{query}

ANSWER:
"""

    response = ollama.chat(
        model="qwen2.5:0.5b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        options={
            "temperature": 0
        }
    )

    return response["message"]["content"].strip()


if __name__ == "__main__":

    sample_context = """
    BERT uses two pre-training tasks:
    Masked Language Modeling (MLM) and
    Next Sentence Prediction (NSP).
    """

    question = "What are the two pre-training tasks used in BERT?"

    answer = generate_answer(question, sample_context)

    print("Question:", question)
    print("AI Answer:", answer)

