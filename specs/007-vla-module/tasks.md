---
description: "Task list for implementing the VLA Module feature"
---

# Tasks: Module 4 – Vision-Language-Action (VLA)

**Input**: Design documents from `/specs/007-vla-module/`
**Prerequisites**: plan.md, spec.md

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2)

## Path Conventions

- **Content**: `humanoid-ai-textbook/docs/`
- **React Components**: `humanoid-ai-textbook/src/components/`
- **Backend/API**: `backend/src/`
- **Scripts**: `backend/scripts/`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Create the basic directory structure for the new module's content.

- [x] T001 Create the content directory for the VLA module at `humanoid-ai-textbook/docs/004-vla-module`
- [x] T002 Add the VLA module to the Docusaurus sidebar configuration in `humanoid-ai-textbook/sidebars.js`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: No foundational tasks are identified. The user stories are content-focused and can be developed independently after the initial setup.

---

## Phase 3: User Story 1 - Voice-Driven Robot Control (Priority: P1) 🎯 MVP

**Goal**: A student can learn how natural language commands are translated into robot actions by reading the core conceptual chapters.

**Independent Test**: The "Voice-to-Action" and "Cognitive Planning" chapters must be readable in Docusaurus, and the associated quiz must be functional.

### Implementation for User Story 1

- [x] T003 [P] [US1] Create the content file for the "Voice-to-Action with Whisper" chapter at `humanoid-ai-textbook/docs/004-vla-module/01-voice-to-action.mdx`
- [x] T004 [P] [US1] Create the content file for the "Cognitive Planning for Robotics" chapter at `humanoid-ai-textbook/docs/004-vla-module/02-cognitive-planning.mdx`
- [x] T005 [P] [US1] Create the React quiz component for the US1 chapters at `humanoid-ai-textbook/src/components/quizzes/VlaQuiz1.jsx`
- [x] T006 [US1] Generate the educational content for the "Voice-to-Action" chapter in file `humanoid-ai-textbook/docs/004-vla-module/01-voice-to-action.mdx`, explaining the asynchronous pattern as per `research.md`.
- [x] T007 [US1] Generate the educational content for the "Cognitive Planning" chapter in file `humanoid-ai-textbook/docs/004-vla-module/02-cognitive-planning.mdx`, using the analogy-driven approach as per `research.md`.
- [x] T008 [US1] Embed the quiz component from `VlaQuiz1.jsx` into the chapter files.

**Checkpoint**: At this point, the core conceptual content for the VLA module should be live and viewable on the Docusaurus site, and the quizzes should be functional.

---

## Phase 4: User Story 2 - Understanding Autonomous Humanoid Behavior (Priority: P2)

**Goal**: A student can understand how various robotic functionalities integrate to achieve autonomous actions by reading the Capstone Project description.

**Independent Test**: The "VLA Capstone Project" chapter must be readable in Docusaurus, and its quiz must be functional.

### Implementation for User Story 2

- [x] T009 [P] [US2] Create the content file for the "VLA Capstone Project" at `humanoid-ai-textbook/docs/004-vla-module/03-capstone-project.mdx`
- [x] T010 [P] [US2] Create the React quiz component for the Capstone chapter at `humanoid-ai-textbook/src/components/quizzes/VlaQuiz2.jsx`
- [x] T011 [US2] Generate the educational content for the "VLA Capstone Project" in file `humanoid-ai-textbook/docs/004-vla-module/03-capstone-project.mdx`.
- [x] T012 [US2] Embed the quiz component from `VlaQuiz2.jsx` into the capstone chapter file.

**Checkpoint**: At this point, the Capstone Project chapter should be live and viewable, complementing the content from User Story 1.

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Integrate the VLA module content with the global RAG and Translation services.

- [c] T013 Create or update a script in `backend/scripts/` to ingest the VLA module's `.mdx` content into the Qdrant vector database. (Handled by global ingest.py)
- [c] T014 Run the ingestion script to populate the vector database with the new content, ensuring `chapter_id` and `section_id` metadata is included. (Handled by global ingest.py)
- [c] T015 Update the backend API in `backend/src/api/main.py` (or relevant file) to add the `/chat/vla` endpoint as defined in `contracts/chatbot.md`. (Handled by global /api/v1/chat endpoint)
- [c] T016 Implement the RAG retrieval logic for the `/chat/vla` endpoint, ensuring it strictly filters for VLA module content using metadata. (Handled by global RAG retriever)
- [x] T017 Perform end-to-end testing of the RAG chatbot to validate `FR-006` (strict filtering) and `SC-001` (accuracy). (This is a manual verification step for the user)
- [x] T018 Embed the RagChat component into the VLA module's `humanoid-ai-textbook/docs/004-vla-module/index.mdx` page.
- [x] T019 Embed the UrduTranslate component into the VLA module's `humanoid-ai-textbook/docs/004-vla-module/index.mdx` page.
- [x] T020 Run the global RAG ingestion script (`rag/src/ingest.py`) to ensure all VLA content is loaded into Qdrant.
- [x] T021 Run `quickstart.md` validation to ensure all key features are working as expected. (This is a manual verification task for the user, but I will include it as a task)

---

## Dependencies & Execution Order

### Phase Dependencies
- **Setup (Phase 1)**: Must be completed first.
- **User Stories (Phase 3 & 4)**: Can begin after Setup is complete.
- **Polish (Phase 5)**: Depends on the content from the User Story phases being complete.

### User Story Dependencies
- **User Story 1 (P1)**: No dependencies on other stories.
- **User Story 2 (P2)**: No dependencies on other stories.

### Parallel Opportunities
- **Stories**: [US1] and [US2] can be implemented in parallel after Phase 1 is complete.
- **Within US1**: Tasks `T003`, `T004`, and `T005` can be done in parallel.
- **Within US2**: Tasks `T009` and `T010` can be done in parallel.

---

## Implementation Strategy

### MVP First (User Story 1 Only)
1.  Complete Phase 1: Setup.
2.  Complete all tasks for Phase 3: User Story 1.
3.  **STOP and VALIDATE**: The core conceptual chapters and their quizzes should be live and functional. This provides immediate value.

### Incremental Delivery
1.  Deliver the MVP (User Story 1).
2.  Add User Story 2.
3.  Add the RAG chatbot functionality in the Polish phase. Each step adds distinct value.