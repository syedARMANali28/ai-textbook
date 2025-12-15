# API Contract: RAG Chatbot

This document defines the API contract for the Retrieval-Augmented Generation (RAG) chatbot specific to the VLA module.

## Endpoint: `/chat/vla`

-   **Method**: `POST`
-   **Description**: Submits a user query to the RAG chatbot and receives an answer grounded in the VLA module content.

### Request Body

```json
{
  "query": "What is cognitive planning?",
  "userId": "user-12345",
  "conversationId": "conv-abcde"
}
```

-   **query (string, required)**: The natural language query from the user.
-   **userId (string, optional)**: A unique identifier for the user to enable future personalization.
-   **conversationId (string, optional)**: A unique identifier for the conversation session to maintain context.

### Success Response (200 OK)

```json
{
  "response": "Cognitive planning is the process of translating natural language commands into a sequence of actions a robot can execute. It involves...",
  "sources": [
    {
      "chapter": "Cognitive Planning for Robotics",
      "section": "Semantic Understanding in ROS 2"
    }
  ]
}
```

-   **response (string)**: The chatbot's answer. If no relevant content is found, this will contain the message defined in `FR-006`: "I can only answer questions about the Vision-Language-Action module. Please ask a question related to the content."
-   **sources (array)**: An array of objects, each citing the chapter and section from which the information was retrieved, as required by `FR-006`.

### Error Responses

-   **400 Bad Request**: The request body is missing the `query` field or is otherwise malformed.
-   **500 Internal Server Error**: An unexpected error occurred on the server while processing the request.