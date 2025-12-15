# Actions: For Long-Running Tasks

For operations that are goal-oriented, long-running, and require continuous feedback, ROS 2 provides **actions**. Actions combine aspects of both topics and services. Imagine commanding a robot to "go to the charging station." This isn't an instant request/response; it's a process that takes time, involves intermediate steps, and might need to be cancelled if priorities change.

Key characteristics of actions:
*   **Goal**: The client sends a goal to the action server (e.g., "go to X, Y coordinates").
*   **Feedback**: The action server provides continuous feedback on the progress towards the goal (e.g., "currently at A, B coordinates, remaining distance Z").
*   **Result**: Once the goal is achieved or cancelled, a final result is sent back to the client.
*   **Preemption**: The client can request to cancel the ongoing goal at any time.

Common uses for actions include:
*   **Navigation**: Moving a robot to a specific location.
*   **Complex Manipulation**: Picking up and placing objects.
*   **Long-duration Sensing**: Performing a detailed scan of an area.

Actions provide a robust and flexible way to manage complex, multi-stage operations, which are very common in autonomous robotics.