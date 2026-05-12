from embeddings import MockTextEmbeddingModel
from retrieval import Retriever
from query_expansion import MockGenerativeModel


class RAGPipeline:
    def __init__(self, documents):
        self.documents = documents

        self.embedder = MockTextEmbeddingModel()
        self.generator = MockGenerativeModel()

        self.doc_embeddings = self.embedder.get_embeddings(documents)
        self.retriever = Retriever(documents, self.doc_embeddings)

    def strategy_a(self, query, top_k=3):
        query_embedding = self.embedder.get_embeddings([query])[0]
        return self.retriever.search(query_embedding, top_k)

    def strategy_b(self, query, top_k=3):
        expanded_query = self.generator.expand_query(query)
        query_embedding = self.embedder.get_embeddings([expanded_query])[0]

        results = self.retriever.search(query_embedding, top_k)

        return expanded_query, results