from src.retriever import Retriever

retriever = Retriever()

query = "What is cloud computing?"

results = retriever.search(
    query=query,
    top_k=5,
)

print("\nQUESTION:")
print(query)

print("\nTOP RESULTS:\n")

documents = results["documents"][0]
metadatas = results["metadatas"][0]
distances = results["distances"][0]

for idx, (doc, meta, distance) in enumerate(
    zip(documents, metadatas, distances),
    start=1,
):
    print("=" * 80)

    print(f"Result {idx}")
    print(f"Source: {meta['source']}")
    print(f"Page: {meta['page']}")
    print(f"Distance: {distance:.4f}")

    print("\nContent:\n")
    print(doc[:500])
    print()