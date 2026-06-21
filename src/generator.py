from google import genai

from src.config import GEMINI_API_KEY


class AnswerGenerator:

    def __init__(self):

        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )

    def generate_answer(
        self,
        question: str,
        context: str
    ):

        prompt = f"""
You are a Retrieval-Augmented Generation assistant.

Rules:
1. Answer ONLY using the provided context.
2. If the answer is not in the context, say:
   "I could not find relevant information in the provided documents."
3. Do not make up facts.
4. Keep answers concise and accurate.

Context:
{context}

Question:
{question}

Answer:
"""

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text