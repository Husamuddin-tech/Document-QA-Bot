from chromadb import PersistentClient


class VectorStore:

    def __init__(self, db_path: str = "db"):
        self.client = PersistentClient(
            path=db_path
        )

    def get_or_create_collection(
        self,
        name: str
    ):
        return self.client.get_or_create_collection(
            name=name
        )