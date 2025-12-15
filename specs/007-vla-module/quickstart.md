# Quickstart: VLA Module

This guide provides the essential steps to set up and view the VLA module content.

## Prerequisites

1.  **Node.js and Yarn**: Ensure you have Node.js (v18 or higher) and Yarn installed.
2.  **Docusaurus Environment**: The project's Docusaurus frontend (`/website` directory) should be set up. If not, run `yarn install` inside the `/website` directory.

## Running the Module Content Locally

1.  **Navigate to the website directory**:
    ```bash
    cd website
    ```

2.  **Start the Docusaurus development server**:
    ```bash
    yarn start
    ```

3.  **View the content**:
    -   Open your web browser and go to `http://localhost:3000`.
    -   The "Module 4: Vision-Language-Action (VLA)" will be visible in the documentation sidebar.

## Key Features to Test

-   **Content Rendering**: All chapters and sections should render correctly from their `.mdx` files.
-   **Urdu Translation**: The Urdu translation toggle should be functional.
-   **Interactive Quizzes**: Quizzes at the end of chapters should be interactive and provide feedback.
-   **RAG Chatbot**: The chatbot interface should be present and able to respond to queries about the module content.