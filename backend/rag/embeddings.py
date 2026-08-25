_model = None


def get_model():
    global _model

    if _model is None:
        print("Loading lightweight embedding model...")

        from fastembed import TextEmbedding

        _model = TextEmbedding(
            model_name="BAAI/bge-small-en-v1.5"
        )

        print("Embedding model loaded.")

    return _model


def generate_embeddings(chunks):

    model = get_model()

    texts = [chunk["text"] for chunk in chunks]

    embeddings = list(model.embed(texts))

    return embeddings