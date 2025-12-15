# Data Model for AI-Native Textbook

**Purpose**: This document defines the structure of data entities for the project. As per the constitution, structured data will be stored in a Neon PostgreSQL database.

---

### Entity: `User`
Represents a learner using the textbook.

- **`user_id`**: `UUID` (Primary Key)
- **`email`**: `String` (Unique, Indexed)
- **`hashed_password`**: `String`
- **`created_at`**: `Timestamp`
- **`learning_profile`**: `JSONB`
  - *Stores user's background (e.g., "beginner", "has python experience") to enable content personalization.*

---

### Entity: `Module`
A top-level container for a subject area.

- **`module_id`**: `UUID` (Primary Key)
- **`slug`**: `String` (Unique, e.g., "ros2-nervous-system")
- **`title`**: `String`
- **`description`**: `Text`

---

### Entity: `Chapter`
A chapter within a module.

- **`chapter_id`**: `UUID` (Primary Key)
- **`module_id`**: `UUID` (Foreign Key to `Module`)
- **`chapter_number`**: `Integer`
- **`slug`**: `String` (Unique within module, e.g., "core-concepts")
- **`title`**: `String`

---

### Entity: `Section`
A content section within a chapter. The actual Markdown content is stored in the Docusaurus file system, but metadata is stored here.

- **`section_id`**: `UUID` (Primary Key)
- **`chapter_id`**: `UUID` (Foreign Key to `Chapter`)
- **`section_number`**: `Integer`
- **`slug`**: `String` (Unique within chapter, e.g., "what-is-ros2")
- **`title`**: `String`
- **`filepath`**: `String`
  - *Path to the markdown file in the `website/docs` directory.*

---

### Entity: `Quiz`
A quiz associated with a chapter.

- **`quiz_id`**: `UUID` (Primary Key)
- **`chapter_id`**: `UUID` (Foreign Key to `Chapter`, Unique)
- **`questions`**: `JSONB`
  - *Array of question objects, e.g., `[{ "question_text": "...", "options": [...], "correct_answer": "..." }]`*

---

### Entity: `QuizAttempt`
Records a user's attempt at a quiz.

- **`attempt_id`**: `UUID` (Primary Key)
- **`user_id`**: `UUID` (Foreign Key to `User`)
- **`quiz_id`**: `UUID` (Foreign Key to `Quiz`)
- **`score`**: `Float`
- **`started_at`**: `Timestamp`
- **`completed_at`**: `Timestamp`

---

### Entity: `Translation`
Stores the translated version of a chapter's content.

- **`translation_id`**: `UUID` (Primary Key)
- **`chapter_id`**: `UUID` (Foreign Key to `Chapter`)
- **`language_code`**: `String` (e.g., "ur")
- **`translated_content_path`**: `String`
  - *Path to a file containing the translated markdown, or the content could be stored directly in a `TEXT` field if it's not too large.*

## Relationships

- A `User` can have many `QuizAttempts`.
- A `Module` can have many `Chapters`.
- A `Chapter` can have many `Sections` and one `Quiz`.
- A `Chapter` can have many `Translations`.
- A `Quiz` can have many `QuizAttempts`.
