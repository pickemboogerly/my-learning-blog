# Development Guide - Boogerly

This guide provides instructions for setting up and working on the Boogerly blog.

## Prerequisites
- **Python 3.13+**
- **pip** (Python package manager)
- **Git**

## Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd my-learning-blog
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Mac/Linux
   # .venv\Scripts\activate  # Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Local Development Commands
We use `invoke` for automation. Base commands are:

| Command | Description |
| :--- | :--- |
| `invoke build` | Generate the site into the `output/` folder. |
| `invoke serve` | Start a local web server at http://localhost:8000. |
| `invoke livereload` | **Recommended:** Start server with auto-rebuild on file changes. |
| `invoke clean` | Delete the generated `output/` folder. |
| `invoke rebuild` | Clean and then build the site. |

## Writing Content
All content resides in the `content/` directory.

### Post Template
New posts should be Markdown files with the following header:
```markdown
Title: My Great Post
Date: 2026-01-29 14:00
Category: Tech
Tags: python, ai
Slug: my-great-post
Authors: Pickem Boogerly
Summary: A short description for the index page.

# Your content starts here
```

### Static Assets
- **Images:** Place in `content/images/`. Reference using `{static}/images/filename.jpg`.
- **Custom CSS:** Found in `content/static/css/custom.css`.

## Build and Deployment
- **Local Preview:** Always use `invoke livereload` to verify changes.
- **Production Build:** Triggered automatically via GitHub push to `main`.
- **Manual Build:** `pelican content -s publishconf.py`.
