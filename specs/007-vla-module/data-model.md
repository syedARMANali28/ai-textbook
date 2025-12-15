# Data Model: VLA Module

This document defines the data entities and their relationships for the Vision-Language-Action (VLA) module content.

## Entity Relationship Diagram (ERD)

```mermaid
erDiagram
    Module ||--o{ Chapter : contains
    Chapter ||--o{ Section : contains
    Chapter ||--|| Quiz : has
    Quiz o--|| User : "is taken by"

    Module {
        string id PK
        string title
        string description
    }

    Chapter {
        string id PK
        string moduleId FK
        string title
        int order
    }

    Section {
        string id PK
        string chapterId FK
        string title
        string content
        int order
    }

    Quiz {
        string id PK
        string chapterId FK
        string title
    }
```

## Entity Definitions

### Module
Represents a top-level educational module in the textbook.
-   **id (string)**: Unique identifier for the module (e.g., `vla-module`).
-   **title (string)**: The display title of the module (e.g., "Module 4: Vision-Language-Action (VLA)").
-   **description (string)**: A brief summary of the module's content.

### Chapter
Represents a chapter within a module.
-   **id (string)**: Unique identifier for the chapter (e.g., `voice-to-action`).
-   **moduleId (string)**: Foreign key referencing the parent `Module`.
-   **title (string)**: The display title of the chapter (e.g., "Voice-to-Action with Whisper").
-   **order (int)**: The sequential order of the chapter within the module.

### Section
Represents a content section within a chapter. This is the primary unit of content.
-   **id (string)**: Unique identifier for the section.
-   **chapterId (string)**: Foreign key referencing the parent `Chapter`.
-   **title (string)**: The title of the section.
-   **content (string)**: The Markdown/MDX content for the section. Per `FR-004`, this should be < 250 words.
-   **order (int)**: The sequential order of the section within the chapter.

### Quiz
Represents a set of questions associated with a chapter to test comprehension.
-   **id (string)**: Unique identifier for the quiz.
-   **chapterId (string)**: Foreign key referencing the parent `Chapter`.
-   **title (string)**: The title of the quiz (e.g., "Chapter 1 Quiz").