_model = None

def get_model():
    global _model

    if _model is None:
        print("Loading embedding model...")

        from sentence_transformers import SentenceTransformer

        _model = SentenceTransformer(
            "all-MiniLM-L6-v2",
            device="cpu"
        )

        print("Embedding model loaded.")

    return _model


def generate_embeddings(chunks):

    model = get_model()

    texts = [chunk["text"] for chunk in chunks]

    embeddings = model.encode(
        texts,
        convert_to_numpy=True,
        show_progress_bar=False,
        batch_size=8
    )

    return embeddings