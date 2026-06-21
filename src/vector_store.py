from chromadb import PersistentClient

from src.config import DB_PATH


class VectorStore:

    def __init__(self):
        self.client = PersistentClient(
            path=DB_PATH
        )

    def get_or_create_collection(
        self,
        name: str
    ):
        return self.client.get_or_create_collection(
            name=name
        )