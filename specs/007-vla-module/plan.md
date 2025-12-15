# Implementation Plan: Module 4 – Vision-Language-Action (VLA)

**Branch**: `007-vla-module` | **Date**: 2025-12-14 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/007-vla-module/spec.md`

## 1. Summary

This plan outlines the technical approach for generating the content for Module 4, focusing on Vision-Language-Action (VLA). The implementation will produce educational content for a Docusaurus frontend and configure a RAG chatbot. The core of this work involves content generation and configuration, not new software architecture, following the pattern of previous modules.

## 2. Technical Context & Decisions

The technical context remains consistent with the existing project architecture. Key decisions for this specific module, based on our research ([research.md](research.md)), are:

-   **Content Structure (Docusaurus)**: Module content will be structured in subdirectories within `/docs`. Interactive elements like quizzes and summaries will be implemented as custom React components embedded within MDX files. The `i18n` system will be used for Urdu translations.
-   **Conceptual Patterns (Whisper & ROS 2)**: The educational content will describe an asynchronous, background-task pattern for Whisper transcription and an analogy-driven explanation for ROS 2 Cognitive Planning, positioning the LLM as the "brain" and ROS 2 as the "nervous system."
-   **RAG Chatbot (LangChain)**: The chatbot will use `RecursiveCharacterTextSplitter` for chunking and rely on metadata filtering (by `chapter_id` and `section_id`) to ensure responses are strictly sourced from VLA module content, as per `FR-006`.

**Language/Version**: Python 3.11 (Backend/Agents), TypeScript (Frontend)
**Primary Dependencies**: FastAPI, Docusaurus, LangChain, Qdrant, Neon, OpenAI Whisper.

## 3. Constitution Check

-   [x] **Mission Alignment**: Aligned. Builds a core chapter of the AI-native textbook.
-   [x] **Core Deliverable**: Aligned. Contributes to the Docusaurus textbook and the RAG chatbot.
-   [x] **Success Criteria**: Aligned. Plan respects performance goals and accuracy requirements.
-   [x] **Architecture Principles**: Aligned. Follows the established modular, free-tier architecture.

*The plan is fully aligned with the project constitution.*

## 4. Project & Data Structure

The implementation will populate the existing project structure.

### 4.1. Documentation Artifacts

The design phase produced the following documentation within `specs/007-vla-module/`:
-   `research.md`: Summarizes key technical decisions.
-   `data-model.md`: Defines the structure for Modules, Chapters, Sections, and Quizzes.
-   `contracts/chatbot.md`: Defines the API for the RAG chatbot.
-   `quickstart.md`: Provides instructions for running the module.

### 4.2. Content & Code Structure

-   **Content**: New `.mdx` files will be created within the `/website/docs/` directory, organized into a new `007-vla-module` subdirectory (or similar).
-   **Quizzes/Summaries**: New React components for this module's quizzes will be added to `/website/src/components/`.
-   **RAG Configuration**: A new knowledge base configuration will be added to the backend to ingest and serve answers for the VLA module. This involves updating configuration files, not creating new source directories.

## 5. Implementation Phases (for `/sp.tasks`)

### Phase 1: Content Scaffolding
1.  Create the directory structure for the VLA module within `/website/docs/`.
2.  Generate placeholder `.mdx` files for each chapter and section defined in the plan (3-5 chapters).
3.  Add the new module to the Docusaurus sidebar configuration (`sidebars.js`).

### Phase 2: Content Generation
1.  Use an agent or script to generate the educational text for the "Cognitive Planning for ROS 2" chapter, following the analogy-driven approach.
2.  Generate the text for the "Voice-to-Action with Whisper" chapter, explaining the asynchronous architectural pattern.
3.  Generate the text for the "VLA Capstone Project" chapter.

### Phase 3: Interactive Elements
1.  Develop the React components for the VLA module's quizzes.
2.  Embed the quiz components into the relevant `.mdx` chapter files.

### Phase 4: RAG Chatbot Configuration
1.  Create a script to ingest the newly generated VLA module content into the Qdrant vector database with appropriate metadata (`chapter_id`, `section_id`).
2.  Update the backend API configuration to recognize and route queries for the `/chat/vla` endpoint defined in the contract.
3.  Verify that the RAG retrieval mechanism correctly filters for VLA-only content.

## 6. Complexity & Risks

-   **Complexity**: Low. This feature largely involves content generation and configuration within an existing architecture.
-   **Risks**:
    -   *Content Quality*: LLM-generated content may require manual review to ensure it meets educational standards for a beginner audience.
    -   *RAG Accuracy*: The chatbot's ability to strictly adhere to the VLA content depends on robust metadata filtering. This needs thorough testing.
