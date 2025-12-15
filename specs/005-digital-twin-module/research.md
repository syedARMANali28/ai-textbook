# Research & Decisions for Module 2

**Purpose**: This document records the key technical and pedagogical decisions for the "Digital Twin" module.

## 1. Approach to Explaining Simulation Engines

- **Decision**: Cover both Gazebo and Unity at a conceptual level, focusing on their roles in robotics simulation rather than providing a feature-by-feature comparison.
- **Rationale**:
    - The goal is to educate beginners on *why* and *how* simulation is used, not to train them as expert users of a specific tool.
    - **Gazebo**: Will be presented as the "de facto standard" in the ROS ecosystem, emphasizing its tight integration with ROS, focus on physics accuracy, and its open-source nature.
    - **Unity**: Will be presented as a powerful, modern alternative, emphasizing its high-fidelity graphics, C# scripting environment, and growing support for robotics via official and third-party tools.
    - The "Physics vs. Visualization" section will be the core of the analysis, using Gazebo and Unity as primary examples to illustrate the trade-offs.
- **Alternatives Considered**:
    - **Focusing only on Gazebo**: This would simplify the module but would not give learners a view of the broader simulation landscape, which increasingly includes game engines like Unity and Unreal.
    - **Providing code examples**: This would violate the project's non-goal of avoiding complex implementation code and would detract from the conceptual focus.

## 2. RAG Strategy

- **Decision**: The RAG strategy will be identical to Module 1. Content will be chunked by section, and metadata for the chapter and section will be attached to each chunk before ingestion into Qdrant.
- **Rationale**: Consistency in the content pipeline is crucial for maintainability. The chatbot's ability to cite sources depends on this structured metadata.
- **Alternatives Considered**: No alternatives were considered, as a consistent RAG strategy across all modules is a core architectural principle.
