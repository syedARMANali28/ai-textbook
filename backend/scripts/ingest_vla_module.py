import os
import re
from langchain_text_splitters import RecursiveCharacterTextSplitter
from qdrant_client import QdrantClient, models
from langchain.vectorstores import Qdrant
from langchain.embeddings import OpenAIEmbeddings

# --- Configuration ---
# In a real application, these would come from a config file or environment variables
QDRANT_URL = os.environ.get("QDRANT_URL", "http://localhost:6333")
QDRANT_API_KEY = os.environ.get("QDRANT_API_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
COLLECTION_NAME = "vla_module_content"
CONTENT_DIR = "../../humanoid-ai-textbook/docs/004-vla-module"

def get_chapter_id_from_filename(filename):
    """Extracts a chapter ID from the filename, e.g., '01-voice-to-action.mdx' -> 'voice-to-action'"""
    match = re.match(r"\d+-(.*)\.mdx", filename)
    if match:
        return match.group(1)
    return "general"

def ingest_vla_content():
    """
    Finds all .mdx files in the VLA module directory, chunks them,
    and ingests them into a Qdrant vector database.
    """
    print("Starting VLA module content ingestion...")

    # 1. Find all .mdx files
    mdx_files = [f for f in os.listdir(CONTENT_DIR) if f.endswith(".mdx")]
    if not mdx_files:
        print(f"No .mdx files found in {CONTENT_DIR}. Exiting.")
        return

    print(f"Found {len(mdx_files)} files to ingest.")

    # 2. Read and process each file
    all_chunks = []
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separators=["\n\n", "\n", " ", ""]
    )

    for filename in mdx_files:
        file_path = os.path.join(CONTENT_DIR, filename)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Simple extraction of section titles and content
        # A more robust parser would be better for production
        sections = content.split("## ")
        chapter_id = get_chapter_id_from_filename(filename)
        
        for section in sections[1:]: # Skip content before the first '##'
            lines = section.split('\n')
            section_title = lines[0].strip()
            section_content = '\n'.join(lines[1:]).strip()

            if not section_content:
                continue

            chunks = text_splitter.split_text(section_content)
            for i, chunk in enumerate(chunks):
                metadata = {
                    "source": filename,
                    "chapter_id": chapter_id,
                    "section_id": section_title.lower().replace(" ", "-"),
                    "chunk_index": i
                }
                # Create a LangChain Document object
                # We are creating a simple dict here, but in a full app
                # this would be a Document object with page_content and metadata
                all_chunks.append({"page_content": chunk, "metadata": metadata})


    if not all_chunks:
        print("No content chunks were generated. Exiting.")
        return

    print(f"Generated {len(all_chunks)} chunks to be ingested.")

    # 3. Connect to Qdrant and ingest
    print("Connecting to Qdrant...")
    embeddings = OpenAIEmbeddings()
    
    # This is a simplified approach. In a real app, you'd use the Qdrant client directly
    # for more control, or use the LangChain integration like this.
    # The from_texts method is convenient for a one-time script.
    qdrant = Qdrant.from_texts(
        [chunk["page_content"] for chunk in all_chunks],
        embedding=embeddings,
        metadatas=[chunk["metadata"] for chunk in all_chunks],
        url=QDRANT_URL,
        api_key=QDRANT_API_KEY,
        collection_name=COLLECTION_NAME,
        force_recreate=True, # For this script, we'll recreate the collection each time
    )

    print(f"Ingestion complete. Collection '{COLLECTION_NAME}' in Qdrant has been populated.")


if __name__ == "__main__":
    # Check for necessary API keys
    if not OPENAI_API_KEY:
        print("Error: OPENAI_API_KEY environment variable not set.")
    else:
        ingest_vla_content()
