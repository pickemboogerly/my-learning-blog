# Project Documentation Index

## Project Overview

- **Type:** Monolith (Static Site Generator)
- **Primary Language:** Python
- **Architecture:** Static Site Generation (SSG)

## Quick Reference

- **Tech Stack:** Pelican, Python, Jinja2, Markdown, Invoke, Cloudflare Pages
- **Entry Point:** `pelicanconf.py` (Development), `publishconf.py` (Production)
- **Primary Commands:** `invoke livereload`, `invoke build`, `invoke publish`

## Generated Documentation

- [Project Overview](./project-overview.md) - High-level summary of the site and its purpose.
- [Architecture](./architecture.md) - Detailed technical architecture and data flow.
- [Source Tree Analysis](./source-tree-analysis.md) - Annotated directory structure.
- [Component Inventory](./component-inventory.md) - Inventory of Jinja2 templates and partials.
- [Development Guide](./development-guide.md) - Local setup, writing content, and deployment instructions.
- [Data Models](./data-models.md) - Markdown metadata schema and configuration variables.

## Existing Documentation

- [README.md](../README.md) - Quick start and project overview.
- [Setup Guide](./setup-guide.md) - Legacy or detailed environment setup reference.

## Getting Started

To start developing locally:

1. Ensure you have Python 3.13+ installed.
2. Activate your virtual environment: `source .venv/bin/activate`.
3. Start the live-reloading server: `invoke livereload`.
4. Visit `http://localhost:8000`.
