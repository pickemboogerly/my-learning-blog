---
stepsCompleted:
  - step-01-init
  - step-02-discovery
  - step-03-success
  - step-04-journeys
  - step-05-domain
  - step-06-innovation
  - step-07-project-type
  - step-08-scoping
  - step-09-functional
  - step-10-nonfunctional
  - step-11-polish
  - step-12-complete
  - step-11-polish
inputDocuments:
  - docs/index.md
  - docs/project-overview.md
  - docs/architecture.md
  - docs/source-tree-analysis.md
  - docs/component-inventory.md
  - docs/development-guide.md
  - docs/data-models.md
  - docs/setup-guide.md
classification:
  projectType: web_app
  domain: general
  complexity: low
  projectContext: brownfield
workflowType: 'prd'
documentCounts:
  briefCount: 0
  researchCount: 0
  brainstormingCount: 0
  projectDocsCount: 8
---

# Product Requirements Document - my-learning-blog

**Author:** Patrick
**Date:** 2026-01-29T14:55:04-05:00

## Executive Summary

**my-learning-blog** (Boogerly) is a personal Pelican-based static site documenting AI-assisted coding experiments. This project focuses on achieving a "fully documented" state to ensure technical clarity, maintainability, and seamless integration for both human contributors and AI agents.

## Success Criteria

### User Success
- **Technical Clarity:** Developers can understand every part of the Boogerly blog without source code inspection.
- **Onboarding Efficiency:** New posts or theme changes can be implemented using only `docs/` resources.

### Business Success
- **100% Completion:** The `docs/index.md` contains zero "(To be generated)" markers.
- **Reference Integrity:** Every critical directory and configuration variable is accurately described across the documentation suite.

### Technical Success
- **Document Validation:** All internal links between documentation files are functional.
- **Codebase Alignment:** `architecture.md` and `data-models.md` accurately reflect current `pelicanconf.py` and `tasks.py` states.

### Measurable Outcomes
- **Status:** `project-scan-report.json` progress is marked as `complete`.
- **Coverage:** 100% file existence for all documents listed in `docs/index.md`.

## Product Scope

### MVP - Minimum Viable Product (Phase 1)
- **Document Suite:** Finalized versions of Architecture, Source Tree, Development Guide, Data Models, and Component Inventory.
- **Master Index:** Fully functional `docs/index.md` as the single source of truth.

### Growth Features (Phase 2)
- **Workflow Detail:** Guides for specific AI agent orchestration and "AI Slop" generation pipelines.
- **Plugin Docs:** Documentation for supplementary Pelican plugins (search, sitemaps).

### Vision (Phase 3)
- **Self-Healing Docs:** Automated tools to detect and flag documentation drift when the codebase changes.

## User Journeys

### Journey 1: The Maintenance Developer (Future Patrick)
- **Opening Scene**: Patrick returns to the project after months to update the site's typography. He can't remember the file structure.
- **Rising Action**: He bypasses source code digging and uses `component-inventory.md` to identify `sidebar.html` and `custom.css`.
- **Climax**: Using `development-guide.md`, he spins up the environment and makes confident, targeted edits.
- **Resolution**: The update is completed rapidly without reverse-engineering, preserving Patrick's time for content.

### Journey 2: The Content Architect (Pickem Boogerly)
- **Opening Scene**: Pickem needs to audit metadata for 50+ posts to ensure perfect indexing.
- **Rising Action**: He consults `data-models.md` for schema verification and `docs/index.md` for plugin documentation.
- **Climax**: He identifies and corrects missing `Slug` metadata that would have broken URL structures.
- **Resolution**: The site remains a professionally architected platform with reliable, standardized metadata.

### Journey 3: The AI Agent Consumer (Technical User)
- **Opening Scene**: A newsletter agent is commissioned to publish weekly summaries.
- **Rising Action**: The agent reads `data-models.md` to identify required field formats and asset pathing rules.
- **Climax**: The agent generates a valid `.md` file, places it in `content/`, and successully triggers a build.
- **Resolution**: The post builds flawlessly on the first attempt, proving the documentation's technical utility.

## Project Scoping & Phased Development

### MVP Strategy & Philosophy
- **Approach:** Documentation Completion (Goal-Oriented)
- **Resource Requirements:** 1 Developer/Architect (Patrick) + AI Assistant

### Risk Mitigation Strategy
- **Technical Risks:** Documentation drift from code changes.
- **Mitigation:** MVP built directly from source analysis; Phase 3 vision includes automated drift detection.

## Functional Requirements

### Documentation Navigation
- **FR1:** Users can access a central `index.md` linking to all project documentation.
- **FR2:** Users can identify high-level purpose and tech stack via `project-overview.md`.
- **FR3:** Users can navigate a visual/mapped `source-tree-analysis.md`.
- **FR4:** Users can understand SSG data flow via `architecture.md`.

### Technical Operations
- **FR5:** Developers can follow `development-guide.md` for local environment setup.
- **FR6:** Developers can identify and run all `invoke` automation commands.
- **FR7:** Writers can format valid blog posts using the Markdown schema in `data-models.md`.
- **FR8:** Theme editors can identify Jinja2 partials via `component-inventory.md`.

### System Context
- **FR9:** Developers can identify where to add custom CSS overrides.
- **FR10:** AI Agents can retrieve technical contracts (data models/architecture) for content generation.
- **FR11:** Every documentation file contains a "Context" header for version and relationship awareness.

## Non-Functional Requirements

### Accuracy & Integrity
- **NFR1:** 100% of directories in `source-tree-analysis.md` must have associated descriptions.
- **NFR2:** `data-models.md` must reflect 100% of metadata fields used in `content/*.md`.

### Maintainability & Usability
- **NFR3:** All documents must use standardized "Context" headers.
- **NFR4:** Documentation must be written in standard GitHub-Flavored Markdown.
- **NFR5:** `docs/index.md` must be accessible from the project root with a single click.
- **NFR6:** Navigation between any two documentation pages must require no more than 2 clicks from the index.

### Security
- **NFR7:** Documentation must warn against hardcoding `SITEURL` in production.
- **NFR8:** Credentials must never be documented in plain text in the `docs/` folder.
