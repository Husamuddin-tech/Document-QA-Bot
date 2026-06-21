from pathlib import Path
from typing import List, Dict, Any

from pypdf import PdfReader
from docx import Document


class DocumentLoader:
    """
    Loads PDF, DOCX, and TXT documents
    and returns standardized document objects.
    """

    SUPPORTED_EXTENSIONS = [".pdf", ".docx", ".txt"]

    def __init__(self, data_dir: str):
        self.data_dir = Path(data_dir)

    def load_documents(self) -> List[Dict[str, Any]]:
        documents = []

        if not self.data_dir.exists():
            raise FileNotFoundError(
                f"Data directory not found: {self.data_dir}"
            )

        for file_path in self.data_dir.iterdir():

            if not file_path.is_file():
                continue

            extension = file_path.suffix.lower()

            if extension == ".pdf":
                documents.extend(self._load_pdf(file_path))

            elif extension == ".docx":
                documents.extend(self._load_docx(file_path))

            elif extension == ".txt":
                documents.extend(self._load_txt(file_path))

            else:
                print(f"[WARNING] Unsupported file: {file_path.name}")

        return documents

    def _load_pdf(self, file_path: Path) -> List[Dict[str, Any]]:
        docs = []

        try:
            reader = PdfReader(str(file_path))

            for page_num, page in enumerate(reader.pages, start=1):

                text = page.extract_text()

                if not text or not text.strip():
                    continue

                docs.append(
                    {
                        "text": text.strip(),
                        "metadata": {
                            "source": file_path.name,
                            "page": page_num,
                            "doc_type": "pdf",
                        },
                    }
                )

        except Exception as e:
            print(f"[ERROR] PDF: {file_path.name} -> {e}")

        return docs

    def _load_docx(self, file_path: Path) -> List[Dict[str, Any]]:
        docs = []

        try:
            document = Document(str(file_path))

            text = "\n".join(
                paragraph.text.strip()
                for paragraph in document.paragraphs
                if paragraph.text.strip()
            )

            if text:
                docs.append(
                    {
                        "text": text,
                        "metadata": {
                            "source": file_path.name,
                            "page": 1,
                            "doc_type": "docx",
                        },
                    }
                )

        except Exception as e:
            print(
                f"[ERROR] DOCX: {file_path.name} -> {e}\n"
                f"Make sure it is a real .docx file and not a renamed PDF/TXT."
            )

        return docs

    def _load_txt(self, file_path: Path) -> List[Dict[str, Any]]:
        docs = []

        try:

            text = None

            # Try UTF-8 first
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    text = file.read()

            except UnicodeDecodeError:
                # Fallback encoding
                with open(file_path, "r", encoding="latin-1") as file:
                    text = file.read()

            if text and text.strip():
                docs.append(
                    {
                        "text": text.strip(),
                        "metadata": {
                            "source": file_path.name,
                            "page": 1,
                            "doc_type": "txt",
                        },
                    }
                )

        except Exception as e:
            print(f"[ERROR] TXT: {file_path.name} -> {e}")

        return docs