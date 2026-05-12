
from src.embeddings import MockTextEmbeddingModel

def test_embedding_shape():

    model = MockTextEmbeddingModel()

    vectors = model.get_embeddings(["hello world", "peak load"])

    assert vectors.shape[0] == 2