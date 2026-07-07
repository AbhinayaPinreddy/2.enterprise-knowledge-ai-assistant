import os
import faiss
import numpy as np

INDEX_PATH = "vector_db/faiss_index/index.faiss"

os.makedirs("vector_db/faiss_index", exist_ok=True)


class VectorStore:

    def __init__(self):

        self.dimension = 384

        if os.path.exists(INDEX_PATH):

            self.index = faiss.read_index(INDEX_PATH)

        else:

            self.index = faiss.IndexFlatL2(self.dimension)

    def add_documents(self, processed_chunks):

        embedding_vectors = np.array(
            [chunk["embedding"] for chunk in processed_chunks],
            dtype=np.float32
        )

        self.index.add(embedding_vectors)

    def save(self):

        faiss.write_index(
            self.index,
            INDEX_PATH
        )

    def search(self, query_embedding, top_k=5):

        distances, indices = self.index.search(
            query_embedding,
            top_k
        )

        return distances, indices

    def total_vectors(self):

        return self.index.ntotal

    def current_size(self):
        return self.index.ntotal