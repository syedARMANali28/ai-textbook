# RAG Chatbot Service Contract

**Purpose**: Defines the interaction between the frontend and the backend RAG chatbot service.

## Endpoint

- **URL**: `/api/v1/chat`
- **Method**: `POST` (or WebSocket for real-time streaming)

## Interaction Model

The interaction will be over a stateful connection (WebSocket preferred) to allow for streaming responses and handling conversation history. A simple HTTP POST version is also defined as a fallback.

### WebSocket Model (Preferred)

1.  **Connection**: Client connects to `wss://<backend-host>/ws/v1/chat`.
2.  **Client Sends Query**:
    ```json
    {
      "type": "query",
      "payload": {
        "query_text": "What is the difference between a topic and a service?",
        "conversation_id": "optional-uuid-to-maintain-history"
      }
    }
    ```
3.  **Server Streams Response**: The server will send a series of messages as it processes the query.

    *   **Token Stream**:
        ```json
        {
          "type": "token",
          "payload": {
            "token": "A"
          }
        }
        ```
        ```json
        {
          "type": "token",
          "payload": {
            "token": " topic"
          }
        }
        ```
        *...and so on.*

    *   **Source Citation Stream**: Once sources are identified, they are sent. This can happen before, during, or after the token stream begins.
        ```json
        {
          "type": "source",
          "payload": {
            "source_id": "uuid-of-source",
            "chapter": 2,
            "section": 1,
            "content_snippet": "Topics are a public broadcast system where a node can publish a message..."
          }
        }
        ```

    *   **End of Stream**:
        ```json
        {
          "type": "end",
          "payload": {
            "message": "Stream finished."
          }
        }
        ```

### HTTP POST Model (Fallback)

- **Request Body**:
  ```json
  {
    "query_text": "What is the difference between a topic and a service?",
    "conversation_id": "optional-uuid-to-maintain-history"
  }
  ```

- **Success Response (`200 OK`)**:
  ```json
  {
    "response_text": "A topic is a public broadcast system where a node can publish a message, and any number of nodes can subscribe to it. A service is a request/response model where a client makes a specific request to a server and waits for a single response.",
    "sources": [
      {
        "chapter": 2,
        "section": 1,
        "content_snippet": "Topics are a public broadcast system..."
      },
      {
        "chapter": 2,
        "section": 2,
        "content_snippet": "Services use a request/response model..."
      }
    ],
    "conversation_id": "new-or-existing-uuid"
  }
  ```

- **Error Response (`400 Bad Request` or `500 Internal Server Error`)**:
  ```json
  {
    "error": "A description of the error."
  }
  ```

## Security & Auth

- The endpoint MUST be protected. The client must send a valid JWT token (obtained from Better-Auth) in the `Authorization` header for both HTTP and WebSocket connection upgrades.
- The backend will validate the token before processing any requests.
