from src.retriever import Retriever
from src.generator import AnswerGenerator

from src.config import (
    TOP_K,
    DISTANCE_THRESHOLD,
    DEBUG,
)


class RAGPipeline:

    def __init__(self):

        self.retriever = Retriever()
        self.generator = AnswerGenerator()

    def ask(
        self,
        question: str,
        top_k: int = TOP_K
    ) -> dict:

        results = self.retriever.search(
            question,
            top_k=top_k
        )

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]
        distances = results["distances"][0]

        if not distances:
            return {
                "answer": "No documents have been indexed yet.",
                "sources": []
            }

        best_distance = min(distances)

        

        if DEBUG:
            print(
                f"\nBest Distance: "
                f"{best_distance:.4f}"
            )

        # Retrieval confidence check
        if best_distance > DISTANCE_THRESHOLD:

            return {
                "answer": (
                    "I could not find relevant "
                    "information in the provided documents."
                ),
                "sources": []
            }

        context = "\n\n".join(
            documents
        )

        answer = self.generator.generate_answer(
            question,
            context
        )

        # Gemini itself rejected answering
        if (
            answer.strip()
            .lower()
            .startswith(
                "i could not find relevant information"
            )
        ):
            return {
                "answer": answer,
                "sources": []
            }

        # Remove duplicate citations
        unique_sources = []
        seen = set()

        for metadata in metadatas:

            key = (
                metadata["source"],
                metadata["page"]
            )

            if key not in seen:

                seen.add(key)

                unique_sources.append(
                    metadata
                )

        return {
            "answer": answer,
            "sources": unique_sources
        }