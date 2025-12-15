# rag/src/settings.py

import os

# Qdrant settings
# For embedded mode, set QDRANT_HOST to empty string or None, and provide QDRANT_PATH
QDRANT_HOST = os.getenv("QDRANT_HOST", "") # Empty string implies embedded mode
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY", None) # Not needed for local embedded
QDRANT_PATH = os.getenv("QDRANT_PATH", "./qdrant_storage") # Path for local storage
COLLECTION_NAME = os.getenv("QDRANT_COLLECTION_NAME", "textbook_rag_collection")

# Embedding model settings (using a dummy for minimal implementation)
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "dummy-embedding-model")
EMBEDDING_MODEL_DIM = int(os.getenv("EMBEDDING_MODEL_DIM", 1536)) # Common dimension for many models (e.g., OpenAI, Cohere)

# LLM settings for response generation and translation (dummy for minimal implementation)
LLM_MODEL = os.getenv("LLM_MODEL", "dummy-llm-model")
LLM_API_KEY = os.getenv("LLM_API_KEY", None)