from sentence_transformers import SentenceTransformer

from src.vector_store import VectorStore
from src.config import (
    COLLECTION_NAME,
    EMBEDDING_MODEL,
    TOP_K,
)


class Retriever:

    def __init__(self):

        self.embedding_model = SentenceTransformer(
            EMBEDDING_MODEL
        )

        self.store = VectorStore()

        self.collection = (
            self.store.get_or_create_collection(
                COLLECTION_NAME
            )
        )

    def search(
        self,
        query: str,
        top_k: int = TOP_K
    ) -> dict:

        query_embedding = (
            self.embedding_model.encode(
                query,
                convert_to_numpy=True
            ).tolist()
        )

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
            include=[
                "documents",
                "metadatas",
                "distances"
            ]
        )

        return results