# Research & Technical Decisions: VLA Module

This document summarizes the technical research and decisions made for implementing the Vision-Language-Action (VLA) module.

## 1. Docusaurus for Educational Content

-   **Decision**: Structure the module content using nested subdirectories within `/docs` to represent chapters and sections. Utilize MDX to create interactive quiz components and leverage the built-in `i18n` for the Urdu translation feature.
-   **Rationale**: Docusaurus is designed for this structure. Its file-system-based routing is intuitive for educational content. The `i18n` system is robust, handling both content files (`.mdx`) and UI strings (`.json`), which directly supports `FR-007`. MDX allows for embedding custom React components, which is the standard way to implement interactive elements like quizzes and summaries as required by `FR-007`.
-   **Alternatives considered**:
    -   **Static Markdown**: Using pure Markdown would prevent the creation of interactive quizzes and summaries, failing to meet functional requirements.
    -   **Separate Quiz Pages**: Building quizzes on separate, non-Docusaurus pages would create a disjointed user experience and complicate the content management workflow.

## 2. OpenAI Whisper Integration Pattern

-   **Decision**: For conceptual explanation, the content will describe an asynchronous, background task-based pattern for handling voice-to-text transcription.
-   **Rationale**: The core of this module is educational content, not a live implementation. The content must explain a robust pattern. An asynchronous approach where the web front-end submits audio and polls for a result (or uses a websocket) is the standard and most scalable pattern. This prevents UI blocking and handles potentially long transcription times gracefully, which is a key concept to teach students. This aligns with the clarification `EH-001` which implies a decoupled front-end that can handle service unavailability.
-   **Alternatives considered**:
    -   **Synchronous API call**: Too simplistic for a real-world explanation and would teach a poor architectural pattern. It would block the user interface and not be scalable.
    -   **Real-time streaming**: While powerful, this is overly complex for the beginner/intermediate audience targeted by `FR-004`. A job-based asynchronous pattern is easier to understand and sufficient for the "voice command" concept.

## 3. RAG Chatbot Implementation (LangChain)

-   **Decision**: Use LangChain's `RecursiveCharacterTextSplitter` for document chunking. Chunks will have metadata attached (e.g., `chapter_id`, `section_id`) to enable strict filtering. The retrieval chain will be configured to *only* query against the vector store for the VLA module's content.
-   **Rationale**: `RecursiveCharacterTextSplitter` is the recommended best practice as it attempts to preserve semantic boundaries (paragraphs, sentences). This is critical for accurate retrieval. Attaching and filtering on metadata is the most effective way to enforce the strict knowledge boundary required by `FR-006` ("Answers strictly using module content"). This prevents the chatbot from "leaking" information from other modules or sources.
-   **Alternatives considered**:
    -   **Fixed-size chunking**: Simpler, but often breaks sentences and cuts off context, which would harm retrieval accuracy and violate the spirit of `SC-001` (95% accuracy).
    -   **No metadata filtering**: Relying solely on vector similarity is insufficient to guarantee the chatbot only uses content from the current module, failing `FR-006`.

## 4. Explaining "Cognitive Planning" for ROS 2

-   **Decision**: The content will explain this concept using an analogy-driven approach. It will compare the process to how a human understands a high-level command (e.g., "get me a coffee") and breaks it down into smaller steps. The explanation will position the LLM as the "brain" that creates the high-level plan, and ROS 2 as the "nervous system" that executes the individual actions (e.g., navigate, pick up, move).
-   **Rationale**: This high-level, conceptual approach is perfectly suited for the beginner-to-intermediate audience (`FR-004`). It avoids getting bogged down in complex robotics code (`FR-005`) while still clearly communicating the core idea of translating natural language intent into a sequence of robot actions.
-   **Alternatives considered**:
    -   **PDDL-based explanation**: Explaining Planning Domain Definition Language (PDDL) is too technical and low-level for the target audience.
    -   **Behavior Tree explanation**: While Behavior Trees are a common implementation detail in ROS 2, explaining the full syntax and logic would be too complex and would violate the "no robotics hardware code" rule (`FR-005`). The analogy-driven approach is more abstract and effective for conceptual understanding.