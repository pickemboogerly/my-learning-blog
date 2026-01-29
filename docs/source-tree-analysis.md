# Source Tree Analysis - my-learning-blog

This project is a Pelican-based static site generator monolith.

## Annotated Directory Tree

```text
my-learning-blog/
├── content/              # PRIMARY CONTENT: All blog posts and static assets
│   ├── images/          # Image assets (raw and processed)
│   ├── static/          # Custom CSS and JS for the frontend
│   ├── extra/           # Extra files like robots.txt and custom.css
│   └── *.md             # Blog posts in Markdown format
├── themes/               # THEMES: UI templates and styling
│   └── Flex/            # Currently active theme (Flex)
│       ├── templates/   # Jinja2 templates (base, article, index, etc.)
│       │   └── partial/ # Reusable UI components (sidebar, nav, etc.)
│       └── static/      # Theme-specific CSS/JS
├── docs/                 # DOCUMENTATION: Project guides and BMad artifacts
│   ├── setup-guide.md   # Detailed project setup instructions
│   └── project-scan-report.json # BMad scan state file
├── pelicanconf.py        # CONFIG: Main development settings
├── publishconf.py        # CONFIG: Production/publishing settings
├── tasks.py              # AUTOMATION: Invoke tasks for build/serve
├── requirements.txt      # DEPENDENCIES: Python package list
├── Makefile              # LEGACY: Old build commands
└── README.md             # OVERVIEW: Project introduction and quick start
```

## Critical Folders Summary

| Folder | Purpose | Key Files |
| :--- | :--- | :--- |
| `content/` | Source of truth for blog posts and local assets. | `*.md` |
| `themes/Flex/` | Defines the look and feel through Jinja2 templates. | `templates/base.html` |
| `/` (Root) | Configuration and automation scripts. | `pelicanconf.py`, `tasks.py` |

## Entry Points

- **Development Server:** `invoke livereload` (serves from `output/` on port 8000)
- **Production Build:** `invoke publish` or `pelican content -s publishconf.py`
- **Main Configuration:** `pelicanconf.py`
