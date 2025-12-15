# Services: The Request/Response Model

While topics are excellent for continuous data streams, sometimes a node needs to perform a specific task and receive a direct result. This is where **services** come in. Services provide a synchronous request/response communication mechanism between two nodes. Think of it like a client making a function call to a server and waiting for the return value.

Key characteristics of services:
*   **One-to-One**: A single client sends a request to a single server.
*   **Synchronous**: The client waits until the server processes the request and sends a response before continuing its own execution.
*   **Transactional**: Services are ideal for one-shot operations that have a clear start and end, and where the client needs immediate feedback.

Common uses for services include:
*   **Configuration changes**: Setting a robot's parameter (e.g., turning a motor on/off).
*   **Triggering actions**: Initiating a specific motion sequence or calibration routine.
*   **Querying data**: Asking for the current state of a sensor or system at a particular moment.

Services are crucial for coordinated operations where direct interaction and a confirmed response are necessary, contrasting with the broadcast nature of topics.