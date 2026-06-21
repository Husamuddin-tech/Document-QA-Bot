from typing import List, Dict, Any

from langchain_text_splitters import RecursiveCharacterTextSplitter


class DocumentChunker:
    """
    Splits loaded documents into chunks
    while preserving metadata.
    """

    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 200
    ):

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ]
        )

    def chunk_documents(
        self,
        documents: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:

        chunks = []
        chunk_id = 0

        for document in documents:

            text = document["text"]
            metadata = document["metadata"]

            split_chunks = self.splitter.split_text(text)

            for chunk in split_chunks:

                chunk_id += 1

                chunks.append(
                    {
                        "text": chunk,
                        "metadata": {
                            **metadata,
                            "chunk_id": chunk_id
                        }
                    }
                )

        return chunks