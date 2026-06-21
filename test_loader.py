from src.loader import DocumentLoader

loader = DocumentLoader("data")

documents = loader.load_documents()

print(f"\nLoaded {len(documents)} documents/pages\n")

for doc in documents[:5]:
    print("=" * 60)
    print(doc["metadata"])
    print(doc["text"][:300])