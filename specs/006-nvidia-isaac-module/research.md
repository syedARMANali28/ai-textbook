# Research & Decisions for Module 3

**Purpose**: This document records the key technical and pedagogical decisions for the "AI-Robot Brain (NVIDIA Isaac™)" module.

## 1. Approach to Explaining NVIDIA Isaac Platform

- **Decision**: Cover the NVIDIA Isaac platform (Isaac Sim, Isaac ROS, Nav2) at a conceptual level, focusing on their integrated roles in advanced perception, simulation, and training for humanoid robotics.
- **Rationale**:
    - The module aims to educate learners on the *capabilities* and *workflow* enabled by the Isaac platform, rather than detailed API usage or implementation specifics.
    - **Isaac Sim**: Emphasize its role in photorealistic simulation, synthetic data generation, and its importance for training AI models without real-world constraints.
    - **Isaac ROS**: Focus on its hardware-accelerated aspects, explaining how it enables faster and more efficient processing for tasks like VSLAM (Visual Simultaneous Localization and Mapping) and other perception algorithms.
    - **Nav2**: Position it within the context of humanoid robotics, explaining its path planning and navigation capabilities for bipedal movement in simulated or real environments.
    - The content will illustrate the interconnectedness of these components to form a powerful "AI-Robot Brain."
- **Alternatives Considered**:
    - **Deep dive into a single component (e.g., Isaac Sim SDK)**: This would provide technical depth but would sacrifice the broad overview of the entire AI-Robot Brain concept, which is the module's primary goal.
    - **Providing code examples**: This would violate the project's non-goal of avoiding complex implementation code and would detract from the conceptual focus.

## 2. RAG Strategy

- **Decision**: The RAG strategy will be identical to previous modules. Content will be chunked by section, and metadata for the chapter and section will be attached to each chunk before ingestion into Qdrant.
- **Rationale**: Consistency in the content pipeline is crucial for maintainability. The chatbot's ability to cite sources depends on this structured metadata.
- **Alternatives Considered**: No alternatives were considered, as a consistent RAG strategy across all modules is a core architectural principle.
