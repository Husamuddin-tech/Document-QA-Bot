# from dotenv import load_dotenv
# import os

# load_dotenv()

# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# if not GEMINI_API_KEY:
#     raise ValueError(
#         "GEMINI_API_KEY not found in .env file"
#     )


COLLECTION_NAME = "document_qa"

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

EMBEDDING_MODEL = "all-MiniLM-L6-v2"

DB_PATH = "db"
DATA_PATH = "data"