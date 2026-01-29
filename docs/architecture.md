# Architecture Documentation - Boogerly Blog

## Executive Summary

Boogerly is a static blog site leveraging the JAMstack (JavaScript, APIs, and Markup) architecture. It uses **Pelican** as its static site generator, **Python** for the build logic, and **Cloudflare Pages** for global distribution. The site is designed for high performance, security, and low maintenance.

## Technology Stack

- **Language:** Python 3.13
- **SSG:** Pelican 4.11.0
- **Templating:** Jinja2
- **Markdown:** Python-Markdown
- **Automation:** Invoke
- **Hosting:** Cloudflare Pages
- **Theme:** Flex (Modern, responsive, dark-mode support)

## Architecture Pattern: Static Site Generation (SSG)

The project follows a classic SSG pattern where source content (Markdown) and templates (Jinja2) are compiled into static HTML/CSS/JS files during a build step.

### Data Flow

1. **Source:** Markdown files in `content/` are edited by the user.
2. **Build:** Pelican processes these files using `pelicanconf.py` (or `publishconf.py`) and the `Flex` theme templates.
3. **Output:** Static files are generated in the `output/` directory.
4. **Deploy:** The `output/` directory is served via Cloudflare Pages.

## Component Overview

- **Content Parser:** Handles Markdown-to-HTML conversion and metadata extraction (Title, Date, Category).
- **Template Engine:** Jinja2 handles the mapping of content to the Flex theme layout.
- **Task Runner:** Invoke (via `tasks.py`) provides a consistent CLI for development tasks like cleaning, building, and serving.

## Development Workflow

1. Create/Edit content in `content/`.
2. Run `invoke livereload` to preview changes in real-time.
3. Commit changes to `main` branch.
4. Cloudflare Pages detects the commit and triggers a production build.

## Testing Strategy

- **Local Preview:** Visual validation using `livereload`.
- **Feed Validation:** Ensuring RSS/Atom feeds are correctly generated in production builds.
- **Link Checking:** (To be added) Checking for broken links during the build process.
