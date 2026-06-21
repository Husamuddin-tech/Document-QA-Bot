from sentence_transformers import SentenceTransformer

from src.loader import DocumentLoader
from src.chunker import DocumentChunker
from src.vector_store import VectorStore

from src.config import (
    COLLECTION_NAME,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
)


# Load model once
embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def generate_embeddings(texts):
    """
    Generate embeddings in batches.

    Assignment Requirement:
    - Batch embeddings
    - No one-by-one embedding calls
    """

    embeddings = embedding_model.encode(
        texts,
        batch_size=32,
        show_progress_bar=True,
        convert_to_numpy=True
    )

    return embeddings.tolist()


def main():

    print("\nLoading documents...")

    loader = DocumentLoader("data")
    documents = loader.load_documents()

    print(
        f"Loaded {len(documents)} pages/documents"
    )

    print("\nChunking documents...")

    chunker = DocumentChunker(
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP
)

    chunks = chunker.chunk_documents(
        documents
    )

    print(
        f"Generated {len(chunks)} chunks"
    )

    print("\nGenerating embeddings...")

    texts = [
        chunk["text"]
        for chunk in chunks
    ]

    embeddings = generate_embeddings(
        texts
    )

    print(
        f"Generated {len(embeddings)} embeddings"
    )

    print("\nCreating vector database...")

    store = VectorStore()

    collection = (
    store.get_or_create_collection(
        COLLECTION_NAME
    )
)

    if collection.count() > 0:

        print(
            "\nCollection already contains data."
        )

        print(
            "Skipping indexing."
        )

        return

    ids = [
        str(i)
        for i in range(len(chunks))
    ]

    metadatas = [
        chunk["metadata"]
        for chunk in chunks
    ]

    collection.add(
        ids=ids,
        documents=texts,
        embeddings=embeddings,
        metadatas=metadatas
    )

    print(
        "\nIndexing completed successfully."
    )

    print(
        f"\nStored {len(chunks)} chunks in ChromaDB."
    )


if __name__ == "__main__":
    main()