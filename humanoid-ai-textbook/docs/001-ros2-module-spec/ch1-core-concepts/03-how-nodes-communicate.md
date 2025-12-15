# How Nodes Communicate: An Overview

Nodes in ROS 2 don't just exist in isolation; they actively communicate to orchestrate the robot's behavior. This communication is essential for the entire system to function as a cohesive unit. ROS 2 provides several flexible mechanisms for nodes to exchange information, each suited for different types of interactions.

The primary communication patterns in ROS 2 are:

1.  **Topics**: This is a publish/subscribe mechanism, ideal for streaming continuous data. A node (publisher) sends messages on a specific topic, and any other node (subscriber) interested in that data can receive them. Think of it like a radio broadcast – many can listen to the same station.
2.  **Services**: Services are a request/reply mechanism, used for discrete, synchronous interactions. A client node sends a request to a server node, and the server processes it and sends back a single response. This is akin to a function call in a distributed system.
3.  **Actions**: Actions are designed for long-running, goal-oriented tasks. They provide feedback during execution and allow for preemption (cancelling a goal). Imagine telling a robot to "go to the kitchen" – an action would provide updates on its progress and allow you to cancel the command if needed.

These communication patterns form the intricate web through which the "robotic nervous system" operates, enabling complex tasks through coordinated effort.