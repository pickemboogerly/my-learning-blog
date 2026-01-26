# Pelican Blog Setup Plan

## Overview
Set up a beautiful Pelican static blog with modern theme, configured for Cloudflare Pages deployment, with proper VS Code workspace setup for a beginner-friendly experience.

## Project Structure
```
my-learning-blog/
├── .venv/                    # Python virtual environment
├── content/                  # Blog posts (markdown files)
├── output/                   # Generated static site
├── pelicanconf.py           # Development config
├── publishconf.py           # Production config
├── requirements.txt         # Python dependencies
├── .gitignore              # Git ignore rules
└── README.md               # Project documentation
```

## Implementation Steps

### 1. Create Project Directory and Virtual Environment
- Create new directory `my-learning-blog`
- Create Python virtual environment using `python -m venv .venv`
- Activate virtual environment (Windows: `.venv\Scripts\activate`)
- This isolates project dependencies from system Python

### 2. Install Pelican and Dependencies
- Install core: `pelican[markdown]` (includes Markdown support)
- Install beautiful theme: `pelican-themes` and clone **Flex theme** (modern, responsive, beautiful)
- Alternative theme option: **Elegant** (feature-rich) or **Medius** (Medium-like)
- Install additional tools:
  - `ghp-import` for easy deployment
  - `invoke` for task automation
  - `livereload` for auto-refresh during development
- Create `requirements.txt` for reproducible setup

### 3. Initialize Pelican Project
- Run `pelican-quickstart` to scaffold project
- Configure settings during quickstart:
  - Site title and author
  - URL prefix for Cloudflare Pages
  - Timezone and language
  - Enable pagination
- This creates `pelicanconf.py` and `publishconf.py`

### 4. Configure Flex Theme
- Clone Flex theme from GitHub into project
- Configure theme in `pelicanconf.py`:
  - Set theme path
  - Configure sidebar with author bio and social links
  - Enable syntax highlighting for code blocks
  - Set up navigation menu
  - Configure colors and fonts
  - **Enable RSS feed generation** (ATOM and RSS2)
  - **Configure Cloudflare Web Analytics** (free, privacy-friendly)
- Add custom CSS if needed

### 5. Set Up GitHub Repository
- **Install Git** (already available)
- **Create GitHub account** (walk through signup at github.com)
- **Configure Git locally**: Set username and email
- **Initialize Git repository** in project folder
- **Create `.gitignore`** (exclude `.venv/`, `output/`, `__pycache__/`, etc.)
- **Initial commit** with all project files
- **Create new repository on GitHub** (via web interface)
- **Push local repository to GitHub** (explain git remote, push)
- **Verify** repository shows all files on GitHub

### 6. Configure for Cloudflare Pages
- Update `publishconf.py` with production settings and analytics
- Configure RSS feed settings in both config files
- Create Cloudflare Pages project:
  - Connect to GitHub repository
  - Set build command: `pip install -r requirements.txt && pelican content -s publishconf.py`
  - Set build output directory: `output`
  - Set environment variable: `PYTHON_VERSION=3.14`
- Enable Cloudflare Web Analytics and add tracking code to `publishconf.py`

### 7. Create First Blog Post
- Create sample post in `content/` directory
- Demonstrate frontmatter (title, date, category, tags)
- Add code syntax highlighting example
- Add images example

### 8. VS Code Workspace Setup
- Create `.vscode/settings.json` for workspace settings:
  - Python interpreter path to `.venv`
  - Markdown linting configuration
  - File associations
- Install recommended VS Code extensions:
  - Python extension
  - Markdown All in One
  - Code Spell Checker
- Create tasks.json for common commands (build, serve)
- Explain VS Code interface: Explorer, Editor, Terminal, Extensions

### 9. Local Development Workflow
- Set up development server with auto-reload
- Explain workflow: write markdown → save → auto-rebuild → preview
- Configure `tasks.py` with Invoke for common tasks

## Critical Files

### pelicanconf.py
Main configuration file with:
- Site metadata (title, author, description)
- Theme configuration
- Plugin settings
- URL structure
- Feed settings

### publishconf.py
Production overrides:
- Absolute URLs
- Analytics integration (optional)
- Feed generation settings

### requirements.txt
All Python dependencies with versions for reproducibility

### .gitignore
Prevent committing:
- Virtual environment
- Generated output
- Python cache files
- OS-specific files

## Cloudflare Pages Deployment Configuration

### Build Settings
- Framework preset: None (or Other)
- Build command: `pip install -r requirements.txt && pelican content -s publishconf.py`
- Build output directory: `output`
- Environment variables:
  - `PYTHON_VERSION=3.14`

### Repository Setup
- Push project to GitHub
- Connect Cloudflare Pages to GitHub repository
- Enable automatic deployments on push to main branch

## Verification Steps

1. **Local Development**
   - Activate virtual environment
   - Run `pelican content` - should build without errors
   - Run `pelican --listen` - should serve at http://localhost:8000
   - Verify theme displays correctly
   - Verify sample post renders with proper formatting

2. **Git Repository**
   - Verify `.gitignore` excludes correct files
   - Initial commit includes all necessary files
   - Push to GitHub successful

3. **Cloudflare Pages**
   - Deploy test successful
   - Site accessible at Cloudflare URL
   - Theme and content render correctly
   - Navigation works

4. **VS Code Setup**
   - Python environment recognized
   - Can run tasks from VS Code
   - Markdown preview works
   - Terminal can activate virtual environment

## Chosen Configuration

**Theme:** Flex
- Modern, clean design with dark mode toggle
- Fully responsive (mobile-friendly)
- Syntax highlighting built-in
- Sidebar with author info
- Category and tag pages with pagination

**Features to Enable:**
- **RSS/ATOM Feeds** - For blog subscribers
- **Cloudflare Web Analytics** - Privacy-friendly, free analytics (no Google Analytics needed)
- Archive and category pages
- Social media links in sidebar

**Deployment:**
- GitHub repository (will set up from scratch)
- Cloudflare Pages (automatic deployment on push)

## Post-Setup Next Steps

1. Customize theme colors and fonts
2. Add author bio and profile picture
3. Configure social media links
4. Set up analytics (optional)
5. Write first real blog post about this setup experience!
6. Set up custom domain in Cloudflare (optional)

## Learning Resources to Include in README

- Pelican documentation: https://docs.getpelican.com
- Markdown guide: https://www.markdownguide.org
- Cloudflare Pages docs: https://developers.cloudflare.com/pages
- VS Code Python tutorial: https://code.visualstudio.com/docs/python/python-tutorial
