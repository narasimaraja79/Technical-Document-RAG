from sentence_transformers import SentenceTransformer

# Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


def generate_embeddings(text_chunks):
    embeddings = model.encode(text_chunks)

    return embeddings


if __name__ == "__main__":
    sample_texts = [
        "Artificial Intelligence is transforming the world.",
        "Machine learning helps computers learn from data."
    ]

    embeddings = generate_embeddings(sample_texts)

    print("Embeddings generated successfully!")
    print("Shape:", embeddings.shape)