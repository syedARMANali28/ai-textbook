# rag/src/retriever.py - Minimal RAG Retriever

import os
import sys
from qdrant_client import QdrantClient, models
from dotenv import load_dotenv

# Add the current directory (rag/src) to sys.path
# This allows absolute imports like 'from settings import ...'
# when running retriever.py directly.
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from settings import QDRANT_HOST, QDRANT_API_KEY, QDRANT_PATH, COLLECTION_NAME, EMBEDDING_MODEL_DIM, EMBEDDING_MODEL

# Load environment variables
load_dotenv()

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

class RAGRetriever:
    def __init__(self, host=QDRANT_HOST, api_key=QDRANT_API_KEY, path=QDRANT_PATH, collection_name=COLLECTION_NAME, vector_size=EMBEDDING_MODEL_DIM):
        if host:
            self.client = QdrantClient(host=host, api_key=api_key)
            print(f"Initialized QdrantClient in remote mode for host: {host}")
        else:
            self.client = QdrantClient(path=path)
            print(f"Initialized QdrantClient in embedded mode for path: {path}")
        
        self.collection_name = collection_name
        self.embedder = EmbeddingGenerator()
        
        # Check if collection exists, if not, it means no data has been ingested yet.
        try:
            self.client.get_collection(collection_name=self.collection_name)
        except Exception:
            print(f"Warning: Collection '{self.collection_name}' not found. Please run ingest.py first or ensure Qdrant is accessible and contains the collection.")

    def retrieve(self, query_text: str, top_k: int = 3, target_module: str = None):
        """
        Retrieves top-k relevant chunks from Qdrant based on the query.
        Optionally filters by target_module.
        """
        query_embedding = self.embedder.generate_embedding(query_text)
        
        should_filters = []
        if target_module and target_module != "general": # 'general' module is a default, not a filter
            should_filters.append(models.FieldCondition(
                key="module",
                match=models.KeywordMatch(keyword=target_module)
            ))

        search_result = self.client.search(
            collection_name=self.collection_name,
            query_vector=query_embedding,
            query_filter=models.Filter(
                must=should_filters
            ) if should_filters else None,
            limit=top_k
        )

        retrieved_chunks = []
        for hit in search_result:
            # Reconstruct chunk data including the text content from payload
            chunk_data = {
                "text": hit.payload.get("text_content", "No content available"),
                "module": hit.payload.get("module"),
                "chapter": hit.payload.get("chapter"),
                "section_title": hit.payload.get("section_title"),
                "section_number": hit.payload.get("section_number")
            }
            retrieved_chunks.append(chunk_data)
        return retrieved_chunks

    def generate_response(self, query_text: str, retrieved_chunks: list):
        """
        Generates a response based on retrieved chunks, enforcing strict grounding.
        This is a minimal LLM call abstraction.
        """
        if not retrieved_chunks:
            return {
                "response_text": "I'm sorry, I couldn't find any relevant information in my knowledge base for this query.",
                "sources": []
            }

        context = "\n\n".join([chunk["text"] for chunk in retrieved_chunks if chunk["text"]])
        
        # In a real scenario, this would involve an LLM call to synthesize an answer
        # from the context and query. For this minimal implementation, we'll
        # just return a dummy response synthesizing the query with context.
        response_text = f"Based on the available information regarding '{query_text}', I found:\n\n{context}\n\n"
        
        sources = []
        for chunk in retrieved_chunks:
            # For source citation, we only need module, chapter, section_title
            sources.append({
                "module": chunk["module"],
                "chapter": chunk["chapter"],
                "section_title": chunk["section_title"]
            })
        
        # Enforce strict grounding (minimal implementation: just check if context exists)
        if not context.strip():
             return {
                "response_text": "I'm sorry, I couldn't find any relevant information in my knowledge base for this query.",
                "sources": []
            }

        return {
            "response_text": response_text,
            "sources": sources
        }

if __name__ == "__main__":
    # Example Usage (requires Qdrant to be running and ingest.py to have been run)
    retriever = RAGRetriever()
    query = "What is ROS 2?"
    # To test with a specific module, e.g., "001-ros2-module-spec"
    # retrieved = retriever.retrieve(query, target_module="001-ros2-module-spec")
    retrieved = retriever.retrieve(query)
    response = retriever.generate_response(query, retrieved)
    print("Response:", response["response_text"])
    print("Sources:", response["sources"])
