# Topics: The Public Broadcast System

Topics are the most common communication mechanism in ROS 2, designed for streaming continuous, asynchronous data. Imagine a radio station broadcasting information; anyone with a radio can tune in and listen. In ROS 2, a node that wants to share information publishes messages on a named "topic." Any other node that wants to receive that information subscribes to the same topic.

Key characteristics of topics:
*   **One-to-Many**: A single publisher can send messages to multiple subscribers simultaneously.
*   **Asynchronous**: Publishers don't wait for subscribers to receive messages. They just send them out.
*   **Decoupled**: Publishers and subscribers don't need to know about each other's existence directly, only the topic name. This makes the system highly modular and flexible.

Common uses for topics include transmitting sensor data (e.g., camera images, LiDAR scans), robot odometry (position and orientation), and control commands (e.g., motor speeds). This "public broadcast" model is ideal for continuous data streams that many parts of the robot might need to access.