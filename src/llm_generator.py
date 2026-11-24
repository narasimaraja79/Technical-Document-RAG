

import ollama


def generate_answer(query, context):

    prompt = f"""
You are an accurate technical document question-answering assistant.

Instructions:
1. Answer using ONLY the provided context.
2. Give a clear and technically correct answer.
3. Do not invent information.
4. If the answer is unavailable, respond exactly:
"I cannot find the answer in the provided document."
5. Keep the answer simple and concise.

Context:
{context}

Question:
{query}

Answer:
"""

    response = ollama.chat(
        model="qwen2.5:0.5b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


if __name__ == "__main__":

    sample_context = """
    RAG combines information retrieval with text generation.
    The retriever finds relevant documents.
    The generator uses retrieved information to generate answers.
    """

    question = "What is the role of the generator in RAG?"

    answer = generate_answer(question, sample_context)

    print("Question:", question)
    print("AI Answer:", answer)
