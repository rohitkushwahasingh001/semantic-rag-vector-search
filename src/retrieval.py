import faiss
import numpy as np
import os


class Retriever:
    def __init__(
        self,
        documents,
        embeddings,
        index_path="faiss_index.index"
    ):
        self.documents = documents
        self.embeddings = embeddings.astype("float32")

        faiss.normalize_L2(self.embeddings)

        dimension = self.embeddings.shape[1]

        self.index_path = index_path

        # load existing index if available
        if os.path.exists(index_path):
            self.index = faiss.read_index(index_path)

        else:
            self.index = faiss.IndexFlatIP(dimension)
            self.index.add(self.embeddings)

            # save index
            faiss.write_index(self.index, index_path)

    def search(self, query_embedding, top_k=3):
        query_vector = np.array([query_embedding]).astype("float32")

        faiss.normalize_L2(query_vector)

        scores, indices = self.index.search(query_vector, top_k)

        results = []

        for score, idx in zip(scores[0], indices[0]):
            results.append({
                "score": float(score),
                "document": self.documents[idx]
            })

        return results