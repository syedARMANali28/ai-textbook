---
id: 0013
title: Implement Custom Docusaurus Cover Page
stage: implement
date: 2025-12-15
surface: agent
model: gemini
feature: humanoid-ai-textbook
branch: 007-vla-module
user: mic
command: /sp.implement
labels: [docusaurus, frontend, ui]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - humanoid-ai-textbook/src/pages/index.js
  - humanoid-ai-textbook/src/pages/NewHomepage.module.css
tests:
  null
---

## Prompt

/sp.implement

Integrate a custom cover page for the existing Docusaurus project in humanoid-ai-textbook/. 
Replace the default black/green landing page with a visually appealing hero section.
Include:
- Title: "AI-Native Humanoid Robotics"
- Subtitle: "Learn Physical AI, Humanoid Robotics, and Voice-to-Action"
- Buttons/links to modules
- Embed RagChat and UrduTranslate components
- Apply a new color scheme (choose modern, clean, bright)
- Preserve sidebar, navbar, and module pages
- Ensure responsive design

Target file: src/pages/index.js

## Response snapshot

I have successfully implemented the custom cover page for the Docusaurus project.
- Replaced the default landing page with a new hero section.
- Added the title "AI-Native Humanoid Robotics" and the subtitle "Learn Physical AI, Humanoid Robotics, and Voice-to-Action".
- Included buttons that link to the ROS 2, VLA, Digital Twin, and NVIDIA Isaac modules.
- Embedded the RagChat and UrduTranslate components.
- Applied a new modern, clean, and bright color scheme.
- The existing sidebar, navbar, and module pages are preserved.
- The new layout is responsive.

## Outcome

- ✅ Impact: A new visually appealing and functional cover page has been implemented, improving the user experience.
- 🧪 Tests: No tests were added or modified.
- 📁 Files: 
  - `humanoid-ai-textbook/src/pages/index.js` (overwritten)
  - `humanoid-ai-textbook/src/pages/NewHomepage.module.css` (created)
- 🔁 Next prompts: null
- 🧠 Reflection: The implementation was straightforward. The provided instructions were clear and detailed. The issues with the prerequisite check and PHR creation scripts should be investigated.

## Evaluation notes (flywheel)

- Failure modes observed: The `check-prerequisites.sh` and `create-phr.sh` scripts failed to locate existing files.
- Graders run and results (PASS/FAIL): null
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): Investigate the path resolution issue in the bash scripts.
