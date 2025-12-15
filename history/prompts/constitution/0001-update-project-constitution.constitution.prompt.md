---
id: 0001
title: Update Project Constitution
stage: constitution
date: 2025-12-10
surface: agent
model: unknown
feature: none
branch: unknown
user: mic
command: /sp.constitution # Project Constitution
# AI-Native Textbook for Physical AI & Humanoid Robotics
...
labels: ["constitution"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
- .specify/memory/constitution.md
- .specify/templates/plan-template.md
- .gemini/commands/sp.constitution.toml
- .gemini/commands/sp.tasks.toml
tests:

---

## Prompt

/sp.constitution # Project Constitution
# AI-Native Textbook for Physical AI & Humanoid Robotics

## 1. Mission

Build a fully AI-native, interactive, intelligent textbook that teaches Physical AI & Humanoid Robotics.

The product must feel like a real AI-powered education platform — not a PDF, blog, or static book.

Core values:
- Fast
- Simple
- Clean
- Beautiful
- Mobile-first

---

## 2. Core Deliverables

1. A Docusaurus-based interactive textbook containing 6–8 short, modern chapters.
2. A Retrieval-Augmented Generation (RAG) chatbot that answers questions strictly and only using book content.
3. User authentication (signup/login) implemented using Better-Auth.
4. Personalized chapter content based on the learner’s background.
5. One-click, high-quality Urdu translation for every chapter.
6. Automatically generated summaries, quizzes, and learning boosters for each chapter.

---

## 3. Success Criteria

- Clean UI with fast load times and full mobile support.
- Entire book readable in under 45 minutes.
- RAG responses are accurate, cited, and grounded in textbook passages.
- Personalization produces visible and meaningful changes in content.
- Urdu translations are fast and high quality.
- Fully deployed system:
  - Frontend: Vercel
  - Backend: Railway
  - Vector Database: Qdrant
  - Relational Database: Neon

---

## 4. Non-Goals

- No decorative or unnecessary animations.
- No long-form or academic-style chapters.
- No complex robotics implementation code; education and understanding only.

---

## 5. Architecture Principles

- Frontend must remain extremely simple and readable.
- Backend must be modular using FastAPI (clear separation of routes and services).
- All structured data stored in Neon.
- All embeddings and vector data stored in Qdrant.
- Canonical folder structure:
  - /backend
  - /website
  - /rag
  - /agents
- Agent skills should be reusable and composable.
- The system must run on free-tier infrastructure.

---

## 6. User Stories (Priority Order)

1. Learners can read the textbook smoothly across devices.
2. Learners can ask questions to a chatbot and receive grounded answers.
3. Learners receive personalized chapter content.
4. Learners can translate chapters into Urdu with one click.
5. Learners can access summaries and quizzes per chapter.
6. Administrators can deploy, monitor, and maintain the system easily.

---

## 7. Constraints

- Must operate entirely on free tiers.
- Must be demoable and deployable within a 90-second recording.
- Must support low-end mobile devices.
- Must avoid heavy dependencies and unnecessary complexity.

---

## 8. Risks and Mitigation

- Low RAG accuracy → apply chunking strategies and MiniLM-style embeddings.
- High token usage → phased feature rollout and response caching.
- User confusion → minimal UI and clear content flow.
- Backend instability → health checks, logging, and retries.

---

## 9. Definition of Done

- All chapters are written and visible in Docusaurus.
- RAG chatbot answers questions with citations.
- Authentication, personalization, and translation are functional.
- Summaries and quizzes are generated for each chapter.
- Frontend and backend are deployed and stable.
- A 90-second demo recording exists and passes all flows.

## Response snapshot

I have updated the project constitution and ensured all dependent templates are in sync.

- New version: 1.0.0 (Major update)
- Updated `.specify/memory/constitution.md` with the new content.
- Updated `.specify/templates/plan-template.md` to reflect the new principles.
- Corrected paths in `.gemini/commands/sp.constitution.toml` and `.gemini/commands/sp.tasks.toml`.
- Created a PHR for this update.

## Outcome

- ✅ Impact: Major update to project constitution.
- 🧪 Tests: N/A
- 📁 Files: 
  - .specify/memory/constitution.md
  - .specify/templates/plan-template.md
  - .gemini/commands/sp.constitution.toml
  - .gemini/commands/sp.tasks.toml
- 🔁 Next prompts: N/A
- 🧠 Reflection: The process of updating the constitution and ensuring consistency across templates was successful.

## Evaluation notes (flywheel)

- Failure modes observed: N/A
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
