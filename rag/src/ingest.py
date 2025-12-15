# rag/src/ingest.py - Minimal RAG Ingestion Script

import os
import sys
import glob
import markdown
from bs4 import BeautifulSoup
from qdrant_client import QdrantClient, models
from dotenv import load_dotenv

# Add the current directory (rag/src) to sys.path
# This allows absolute imports like 'from settings import ...'
# when running ingest.py directly.
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from settings import QDRANT_HOST, QDRANT_API_KEY, QDRANT_PATH, COLLECTION_NAME, EMBEDDING_MODEL_DIM, EMBEDDING_MODEL

# Load environment variables
load_dotenv()

class MarkdownProcessor:
    def __init__(self, docs_path="humanoid-ai-textbook/docs/"):
        self.docs_path = docs_path

    def load_markdown_files(self):
        """Loads all markdown files from the docs_path."""
        md_files = glob.glob(os.path.join(self.docs_path, '**', '*.md'), recursive=True)
        md_files.extend(glob.glob(os.path.join(self.docs_path, '**', '*.mdx'), recursive=True))
        return md_files

    def chunk_content(self, file_path):
        """
        Chunks markdown content by sections (headings) and extracts metadata.
        Returns a list of dictionaries, each representing a chunk.
        """
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        html = markdown.markdown(content)
        soup = BeautifulSoup(html, 'html.parser')

        chunks = []
        current_chunk_text = []
        current_metadata = {
            "source_file": file_path,
            "module": "general", # Default module
            "chapter": "general", # Default chapter
            "section_title": "Introduction",
            "section_number": 0
        }

        # Extract module and chapter from path
        # Example path: humanoid-ai-textbook/docs/001-ros2-module-spec/ch1-core-concepts/01-what-is-ros2.md
        path_parts = file_path.replace(self.docs_path, '').split(os.sep)
        
        # Determine module
        if len(path_parts) > 0 and path_parts[0]:
            if path_parts[0].startswith("0"): # Heuristic for module folders
                current_metadata["module"] = path_parts[0]
            else: # top-level docs like intro.md
                current_metadata["module"] = "general"

        # Determine chapter
        if len(path_parts) > 1 and path_parts[1]:
            if path_parts[1].startswith("ch"): # Heuristic for chapter folders
                current_metadata["chapter"] = path_parts[1]
            else:
                current_metadata["chapter"] = path_parts[1].split('.')[0] # Use filename as chapter if not in a chapter folder

        section_counter = 0

        for element in soup.children:
            # Only consider actual HTML tags that contain text, ignore NavigableString
            if element.name and element.name.startswith('h'):
                if current_chunk_text:
                    chunks.append({
                        "text": "\n".join(current_chunk_text).strip(),
                        "metadata": current_metadata.copy()
                    })
                    current_chunk_text = []

                # Ensure section title is clean text
                section_title = element.get_text(strip=True)
                current_metadata["section_title"] = section_title if section_title else "Unnamed Section"
                section_counter += 1
                current_metadata["section_number"] = section_counter
            elif element.name: # Process other tags like p, li, etc.
                text = element.get_text(separator=' ', strip=True)
                if text:
                    current_chunk_text.append(text)
            elif isinstance(element, str): # Handle NavigableString (text directly under body/div etc.)
                text = element.strip()
                if text:
                    current_chunk_text.append(text)
        
        if current_chunk_text:
            chunks.append({
                "text": "\n".join(current_chunk_text).strip(),
                "metadata": current_metadata.copy()
            })
            
        return chunks

class EmbeddingGenerator:
    def __init__(self, model=EMBEDDING_MODEL):
        self.model = model
        # In a real scenario, initialize an LLM client here (e.g., GeminiEmbeddings)
        # print(f"Using abstract embedding model: {self.model}") # Suppress for cleaner output

    def generate_embedding(self, text: str):
        """
        Generates a dummy embedding for the given text.
        In a real application, this would call an actual embedding model API.
        """
        # Replace with actual LLM embedding call (e.g., from Gemini API)
        # For a minimal example, we'll return a vector of zeros.
        # Ensure the dimension matches EMBEDDING_MODEL_DIM
        return [0.0] * EMBEDDING_MODEL_DIM

class QdrantManager:
    def __init__(self, host=QDRANT_HOST, api_key=QDRANT_API_KEY, path=QDRANT_PATH, collection_name=COLLECTION_NAME, vector_size=EMBEDDING_MODEL_DIM):
        if host:
            self.client = QdrantClient(host=host, api_key=api_key)
            print(f"Initialized QdrantClient in remote mode for host: {host}")
        else:
            # Initialize Qdrant client in embedded mode
            self.client = QdrantClient(path=path)
            print(f"Initialized QdrantClient in embedded mode for path: {path}")

        self.collection_name = collection_name
        self.vector_size = vector_size
        self._ensure_collection_exists()

    def _ensure_collection_exists(self):
        """Ensures the Qdrant collection exists, creates it if not."""
        if self.client.collection_exists(collection_name=self.collection_name):
            print(f"Collection '{self.collection_name}' already exists. Deleting and recreating for fresh ingestion.")
            self.client.delete_collection(collection_name=self.collection_name)
        
        print(f"Creating collection '{self.collection_name}'.")
        self.client.create_collection(
            collection_name=self.collection_name,
            vectors_config=models.VectorParams(size=self.vector_size, distance=models.Distance.COSINE),
        )
        print(f"Collection '{self.collection_name}' created.")

    def upsert_vectors(self, chunks_with_embeddings):
        """
        Upserts (inserts or updates) vectors and their payloads into Qdrant.
        """
        points = []
        for i, chunk_data in enumerate(chunks_with_embeddings):
            # Ensure payload has only basic types (dict, list, str, int, float, bool)
            # Remove the 'text' key from metadata as it can be large
            payload = chunk_data["metadata"].copy()
            payload["text_content"] = chunk_data["text"] # Store original text in payload
            
            # Convert UUID-like strings to actual strings if not already
            for key in ["module", "chapter"]: # Add other keys if they might be UUIDs
                 if isinstance(payload.get(key), (bytes, bytearray)):
                     payload[key] = payload[key].decode('utf-8')
                 elif not isinstance(payload.get(key), (str, int, float, bool, list, dict, type(None))):
                     payload[key] = str(payload[key]) # Ensure it's a string

            points.append(models.PointStruct(
                id=i, # Use a proper ID generation in production (e.g., UUIDs for each chunk)
                vector=chunk_data["embedding"],
                payload=payload
            ))
        
        if points:
            # Qdrant upsert needs list of PointStruct
            self.client.upsert(
                collection_name=self.collection_name,
                wait=True,
                points=points,
            )
            print(f"Upserted {len(points)} points into collection '{self.collection_name}'.")

def ingest_documents():
    processor = MarkdownProcessor()
    embedder = EmbeddingGenerator()
    qdrant_manager = QdrantManager()

    all_markdown_files = processor.load_markdown_files()
    print(f"Found {len(all_markdown_files)} markdown files.")

    all_chunks = []
    for md_file in all_markdown_files:
        print(f"Processing: {md_file}")
        chunks = processor.chunk_content(md_file)
        for chunk in chunks:
            chunk["embedding"] = embedder.generate_embedding(chunk["text"])
            all_chunks.append(chunk)

    print(f"Generated {len(all_chunks)} chunks with embeddings.")
    qdrant_manager.upsert_vectors(all_chunks)
    print("Ingestion complete.")

if __name__ == "__main__":
    ingest_documents()
