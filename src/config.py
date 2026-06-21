import os
from dotenv import load_dotenv

load_dotenv()

# ChromaDB
COLLECTION_NAME = "document_qa"
DB_PATH = "db"

# Data
DATA_PATH = "data"

# Chunking
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# Embeddings
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# Retrieval
TOP_K = 5
DISTANCE_THRESHOLD = 1.2

# Gemini
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Development
DEBUG = False