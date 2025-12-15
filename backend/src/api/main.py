from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from dotenv import load_dotenv

# Load environment variables (for RAG and Translation services)
load_dotenv()

# Import RAG components
# Assuming rag/src is in PYTHONPATH or accessible via relative import
import sys
# Adjust path to include the rag/src directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../rag/src')))

from retriever import RAGRetriever
from settings import COLLECTION_NAME

# Import Translation service
from services.translation_service import TranslationService

app = FastAPI()

# Initialize services
rag_retriever = RAGRetriever()
translation_service = TranslationService()

class ChatQuery(BaseModel):
    query_text: str
    conversation_id: str = None # Optional

class TranslateRequest(BaseModel):
    chapter_content: str
    chapter_title: str # Used for warning banner if translation fails
    target_language: str = "ur" # Hardcoded for now based on spec

@app.get("/")
async def read_root():
    return {"message": "Hello World from Backend!"}

@app.post("/api/v1/chat")
async def chat_with_rag(query: ChatQuery):
    try:
        # Here, we'd ideally filter by the module the user is currently viewing.
        # For this minimal implementation, we'll retrieve from the entire collection.
        # A more advanced implementation would pass `target_module` from frontend context.
        # For now, let's filter by a hardcoded module for testing if needed,
        # or leave it broad. Let's make it accept a target_module in the query.
        
        # contracts/chatbot.md does not specify target_module in query,
        # so for this minimal implementation, we will not filter by module initially.
        # The retriever itself has target_module as an argument, so it's ready if needed.
        retrieved_chunks = rag_retriever.retrieve(query.query_text, top_k=3)
        response = rag_retriever.generate_response(query.query_text, retrieved_chunks)
        
        # Format sources as per contracts/chatbot.md
        formatted_sources = []
        for src in response["sources"]:
            formatted_sources.append({
                "chapter": src.get("chapter", "N/A"),
                "section": src.get("section_number", "N/A"), # Use section_number as 'section'
                "content_snippet": src.get("text", "No snippet") # retriever.py doesn't return full text in sources currently.
            })
            
        return {
            "response_text": response["response_text"],
            "sources": formatted_sources,
            "conversation_id": query.conversation_id # Pass through conversation_id
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/v1/translate_chapter")
async def translate_chapter(request: TranslateRequest):
    if request.target_language.lower() != "ur":
        raise HTTPException(status_code=400, detail="Only Urdu translation is supported at this time.")

    try:
        translated_text = translation_service.translate_chapter_to_urdu(request.chapter_content)
        
        # Check for simulated failure (e.g., LLM returned an error tag)
        if "<!-- Translation Failed" in translated_text:
            return {
                "translated_content": translation_service.get_warning_banner(request.chapter_title) + request.chapter_content,
                "warning": True,
                "message": "Translation service encountered an issue. Displaying original content with a warning."
            }

        return {
            "translated_content": translated_text,
            "warning": False
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))