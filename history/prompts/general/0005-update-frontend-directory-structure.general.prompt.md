---
id: 5
title: Update Frontend Directory Structure
stage: general
date_iso: 2025-12-10
surface: agent
model: claude-3-5-sonnet
feature: none
branch: main
user: mic
command: and i must have a seperate frontend folder like backend with docs src static inside src are components pages services themes
labels: ["frontend", "directory-structure", "refactor"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml:
  - website/ (renamed to frontend/)
  - frontend/docs/
  - frontend/src/services/
  - frontend/src/themes/
  - frontend/static/
  - .github/workflows/ci.yml (modified)
tests_yaml: []
prompt_text: |-
  and i must have a seperate frontend folder like backend with docs src static inside src are components pages services themes
response_text: |-
  The frontend directory structure has been updated according to your specifications.
  [... directory listing ...]
outcome: success
evaluation:
  correctness: 5
  clarity: 5
  completeness: 5
  broader_impact: 4
---
