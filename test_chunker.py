from src.loader import DocumentLoader
from src.chunker import DocumentChunker

loader = DocumentLoader("data")

documents = loader.load_documents()

print(f"\nLoaded Documents: {len(documents)}")

chunker = DocumentChunker(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = chunker.chunk_documents(documents)

print(f"\nGenerated Chunks: {len(chunks)}")

print("\nSample Chunks:\n")

for chunk in chunks[:3]:

    print("=" * 80)

    print(chunk["metadata"])

    print(chunk["text"][:300])

    print()