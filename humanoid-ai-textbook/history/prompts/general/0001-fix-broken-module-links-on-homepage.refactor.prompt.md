---
id: 1
title: "Fix Broken Module Links on Homepage"
stage: "refactor"
date: "2025-12-17"
surface: "agent"
model: "gemini"
feature: "none"
branch: "main"
user: "mic"
command: "read_file, list_directory, glob, run_shell_command, replace"
labels: ["bug", "docusaurus", "routing"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - src/pages/index.js
  - .docusaurus/routes.js
tests:
  - "none"
outcome: "success"
---

# PROMPT

There is already an existing Docusaurus project in the root directory named humanoid-ai-textbook.

On the homepage, there are 4 buttons/cards that link to the four modules. These buttons are rendered from
humanoid-ai-textbook/src/pages/index.js.

I want you to:

Open src/pages/index.js inside the humanoid-ai-textbook project.

Identify the 4 module buttons/cards on the homepage.

Correct their links so they point to the correct Docusaurus module routes:

Module 1 (ROS 2): /docs/001-ros2-module-spec

Module 2 (Digital Twin): /docs/005-digital-twin-module

Module 3 (NVIDIA Isaac): /docs/006-nvidia-isaac-module

Module 4 (Vision-Language-Action): /docs/004-vla-module

Do not create any new pages, folders, or projects.

Do not modify the docs content or sidebar structure.

Only update the homepage buttons so navigation works correctly.

After making the changes, ensure the homepage renders correctly with the header, footer, and theme intact.

---
no when i clicked the button it didnt redirected me to the module but redirected me to another page and this is written there Page Not Found
We could not find what you were looking for.

Please contact the owner of the site that linked you to the original URL and let them know their link is broken.
---
i did checked it same issue i just want that when i click on the button it take me on the book page where all the modules are listed and the same module is opened the one i clicked on
---
perfect

# RESPONSE

I have updated the links for the module buttons on the homepage. They now point to the first page of each module, which should ensure the documentation sidebar opens to the correct context when you click on them.

Please verify that the links are working as you expect.
---
The user confirmed that the fix is perfect. The problem was related to Docusaurus routing, specifically that numeric prefixes in directory names are stripped from the URLs when `future: { v4: true }` is enabled. The links were updated to reflect these shorter, non-prefixed paths.