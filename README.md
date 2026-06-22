# 📚 Document Q&A Bot using RAG (Retrieval-Augmented Generation)

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.58.0-FF4B4B.svg)
![ChromaDB](https://img.shields.io/badge/Vector%20DB-ChromaDB-5C2D91.svg)
![Gemini](https://img.shields.io/badge/LLM-Gemini%202.5%20Flash-4285F4.svg)
![Sentence Transformers](https://img.shields.io/badge/Embeddings-all--MiniLM--L6--v2-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## Overview

Document Q&A Bot is a Retrieval-Augmented Generation (RAG) application that enables users to ask natural language questions over a collection of documents and receive accurate, context-aware answers with source citations.

The system performs document ingestion, chunking, embedding generation, vector storage, semantic retrieval, and answer generation using Gemini 2.5 Flash. Answers are grounded in retrieved document content and include references to the source documents.

---

## Features

* Document ingestion from PDF, DOCX, and TXT files
* Recursive text chunking with overlap
* Semantic embeddings using Sentence Transformers
* Persistent vector storage using ChromaDB
* Similarity-based retrieval
* Answer generation using Gemini 2.5 Flash
* Source citations with document and page references
* Hallucination prevention using retrieval confidence threshold
* Interactive Command-Line Interface (CLI)
* Streamlit Web Interface
* Question history tracking
* Persistent vector database (no re-indexing required)

---

## Tech Stack

| Component              | Technology               | Version |
| ---------------------- | ------------------------ | ------- |
| Language               | Python                   | 3.11+   |
| LLM                    | Gemini 2.5 Flash         | Latest  |
| Embeddings             | all-MiniLM-L6-v2         | Latest  |
| Vector Database        | ChromaDB                 | 1.5.9   |
| UI                     | Streamlit                | 1.58.0  |
| PDF Parsing            | PyPDF                    | 6.13.3  |
| DOCX Parsing           | python-docx              | 1.2.0   |
| Chunking               | LangChain Text Splitters | 1.1.2   |
| Environment Management | python-dotenv            | 1.2.2   |

---

## Architecture Overview

```text
Documents
(PDF / DOCX / TXT)
        │
        ▼
Document Loader
        │
        ▼
Text Chunking
(1000 chars, 200 overlap)
        │
        ▼
Embeddings
(all-MiniLM-L6-v2)
        │
        ▼
ChromaDB
(Vector Store)
        │
        ▼
User Question
        │
        ▼
Query Embedding
        │
        ▼
Top-K Retrieval
        │
        ▼
Context Builder
        │
        ▼
Gemini 2.5 Flash
        │
        ▼
Grounded Answer
+ Source Citations
```

---

## Project Structure

```text
document-qa-bot/
│
├── app.py
├── cli_app.py
│
├── src/
│   ├── __init__.py
│   ├── chunker.py
│   ├── config.py
│   ├── generator.py
│   ├── ingest.py
│   ├── loader.py
│   ├── rag_pipeline.py
│   ├── retriever.py
│   └── vector_store.py
│
├── data/
│   ├── ai_cybersecurity.pdf
│   ├── ai-overview.txt
│   ├── cloud_computing.pdf
│   ├── gen_ai.pdf
│   └── llm.pdf
│
├── db/
│
├── test_loader.py
├── test_chunker.py
├── test_retriever.py
├── test_rag.py
│
├── requirements.txt
├── README.md
├── .env
└── .gitignore
```

---

## Chunking Strategy

The system uses Recursive Character-Based Chunking.

### Configuration

```python
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
```

### Why?

* Preserves semantic context
* Reduces context loss between chunks
* Improves retrieval quality
* Works well for research papers and technical documents

---

## Embedding Model

### Model

```text
all-MiniLM-L6-v2
```

### Why?

* Fast inference
* High-quality semantic embeddings
* Lightweight
* Suitable for local execution
* Widely used in production RAG systems

---

## Vector Database

### Chosen Database

```text
ChromaDB
```

### Why?

* Easy setup
* Persistent storage
* Fast similarity search
* No external infrastructure required
* Ideal for beginner and intermediate RAG applications

---

## Setup Instructions

### Clone Repository

```bash
git clone <repository-url>
cd document-qa-bot
```

### Create Virtual Environment

```bash
python3.11 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=your_api_key_here
```

Get your Gemini API key from:

https://aistudio.google.com/

---

## Build the Vector Database

Run the ingestion pipeline:

```bash
python -m src.ingest
```

Expected Output:

```text
Loading documents...
Chunking documents...
Generating embeddings...
Creating vector database...
Indexing completed successfully.
```

---

## Running the CLI Application

```bash
python cli_app.py
```

Example:

```text
Question:
What is cloud computing?

Answer:
Cloud computing is...
```

---

## Running the Streamlit Application

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## Example Queries

### Cloud Computing

```text
What is cloud computing?
```

### Generative AI

```text
What is Generative AI?
```

### Cybersecurity

```text
How is AI used in cybersecurity?
```

### Large Language Models

```text
What are Large Language Models?
```

### Cross-Document Query

```text
How are Generative AI and Large Language Models related?
```

### Unanswerable Query

```text
Who won the FIFA World Cup in 1998?
```

Expected:

```text
I could not find relevant information in the provided documents.
```

---

## Hallucination Prevention

The system implements retrieval confidence validation.

```python
DISTANCE_THRESHOLD = 1.2
```

If retrieved chunks are not sufficiently relevant, the model refuses to answer rather than generating unsupported information.

---

## Known Limitations

* Retrieval quality depends on chunk quality.
* Currently optimized for English documents.
* Does not perform OCR on scanned PDFs.
* Cross-document reasoning is limited by retrieved context.
* Uses a fixed retrieval threshold.

---

## Future Improvements

* Hybrid Search (BM25 + Vector Search)
* Query Expansion
* Reranking Models
* Multi-Vector Retrieval
* OCR Support for Scanned PDFs
* Docker Deployment
* User Authentication
* Multi-User Support
* Document Upload Interface

---

## Testing

The project includes:

```bash
python test_loader.py
python test_chunker.py
python test_retriever.py
python test_rag.py
```

for validating each stage of the RAG pipeline independently.

---

## Author

**Syed Husamuddin**

Bachelor of Engineering (Computer Science & Engineering – AI & Data Science)

AI Engineering Intern Assignment – Basic Document Q&A Bot using RAG

---
