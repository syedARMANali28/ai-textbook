# Choosing the Right Communication Method

With topics, services, and actions at your disposal, selecting the appropriate ROS 2 communication method is crucial for designing efficient and robust robot applications. The choice largely depends on the nature of the data being exchanged and the desired interaction pattern.

*   **Use Topics when**:
    *   You need continuous, asynchronous data streaming (e.g., sensor data, odometry, video feeds).
    *   Multiple consumers might be interested in the same data, but the publisher doesn't need to know who is listening.
    *   The loss of an occasional message is acceptable (as there's no guaranteed delivery).

*   **Use Services when**:
    *   You need a single, synchronous request-response interaction.
    *   The client needs an immediate, guaranteed result from the server.
    *   The operation is short-lived and transactional (e.g., setting a parameter, querying a state).

*   **Use Actions when**:
    *   You need a goal-oriented, long-running task.
    *   Continuous feedback on progress is required.
    *   The ability to preempt (cancel) the task is necessary.

By understanding the strengths of each communication pattern, you can effectively choreograph the interactions between your robot's nodes, building a truly intelligent and responsive system.