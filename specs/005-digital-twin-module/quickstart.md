# Quickstart Guide for AI-Native Textbook

**Purpose**: This guide provides instructions for setting up the local development environment for the AI-Native Textbook project.

## Prerequisites

- Node.js (v18 or later)
- Python (v3.11 or later)
- Docker and Docker Compose
- `pnpm` (or `npm`/`yarn`)

## 1. Backend Setup (FastAPI & RAG)

The backend service handles the RAG chatbot, content management, and user authentication.

```bash
# 1. Navigate to the backend directory
cd backend

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate

# 3. Install Python dependencies
pip install -r requirements.txt

# 4. Set up environment variables
# Copy the example file and fill in your details
cp .env.example .env
# You will need to add credentials for Neon, Qdrant, and any LLM APIs.

# 5. Run database migrations (if applicable)
# alembic upgrade head

# 6. Run the FastAPI server
uvicorn src.main:app --reload
```

The backend server will be running at `http://127.0.0.1:8000`.

## 2. Frontend Setup (Docusaurus)

The frontend is the Docusaurus website that presents the textbook content.

```bash
# 1. Navigate to the website directory
cd website

# 2. Install Node.js dependencies
pnpm install

# 3. Run the Docusaurus development server
pnpm start
```

The website will be available at `http://localhost:3000`.

## 3. Data Ingestion (Populating the RAG System)

To make the chatbot work, you need to process the Markdown content and load it into the Qdrant vector database.

```bash
# 1. Navigate to the rag directory
cd rag

# 2. Ensure your virtual environment from the backend setup is active
source ../backend/venv/bin/activate

# 3. Run the ingestion script
# This script will read from ../website/docs, chunk the files,
# generate embeddings, and upload them to Qdrant.
python src/ingest.py
```

## 4. Running the Full System with Docker Compose

For a more integrated setup, you can use Docker Compose to run the backend, databases, and potentially the frontend.

```bash
# From the project root
docker-compose up --build
```
This will start:
- The FastAPI backend service.
- A Qdrant container.
- A Neon PostgreSQL container (or connect to the cloud instance).
- The Docusaurus frontend dev server.
