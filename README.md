# Boogerly

A blog documenting my journey learning Python and AI-assisted coding.

## About

**Boogerly** is a static blog built with [Pelican](https://getpelican.com/) and deployed on [Cloudflare Pages](https://pages.cloudflare.com/). This project showcases the JAMstack architecture and serves as a learning platform for Python development.

**Author:** Pickem Boogerly

## Tech Stack

- **Static Site Generator:** Pelican 4.11.0
- **Theme:** [Flex](https://github.com/alexandrevicenzi/Flex)
- **Language:** Python 3.13
- **Hosting:** Cloudflare Pages
- **Content Format:** Markdown

## Features

- Modern, responsive design with dark mode
- Syntax highlighting for code blocks
- RSS/ATOM feeds for subscribers
- Category and tag organization
- Privacy-friendly analytics (Cloudflare Web Analytics)
- Fast loading with global CDN

## Local Development

### Prerequisites

- Python 3.13+
- Git

### Setup

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd my-learning-blog
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # Mac/Linux:
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Writing Content

1. Create a new Markdown file in the `content/` directory:
   ```markdown
   Title: My Post Title
   Date: 2026-01-25 10:00
   Category: Tutorial
   Tags: python, learning
   Slug: my-post-title
   Summary: A brief summary of the post

   # Your content here
   ```

2. Build and preview the site:
   ```bash
   # Generate the site
   pelican content

   # Or use the development server with auto-reload
   pelican --listen --autoreload
   ```

3. Visit `http://localhost:8000` to preview

### Useful Commands

```bash
# Generate the site for development
pelican content

# Generate the site for production
pelican content -s publishconf.py

# Start development server with auto-reload
pelican --listen --autoreload

# Using invoke tasks
invoke build           # Build the site
invoke rebuild         # Clean and rebuild
invoke serve           # Serve locally
invoke livereload      # Serve with auto-reload
```

## Deployment

This blog is configured for automatic deployment to Cloudflare Pages:

1. Push changes to the `main` branch on GitHub
2. Cloudflare Pages automatically builds and deploys
3. Build command: `pip install -r requirements.txt && pelican content -s publishconf.py`
4. Build output directory: `output`

## Project Structure

```
my-learning-blog/
├── content/              # Blog posts (Markdown files)
├── themes/
│   └── Flex/            # Flex theme files
├── output/              # Generated static site (gitignored)
├── .venv/               # Python virtual environment (gitignored)
├── pelicanconf.py       # Development configuration
├── publishconf.py       # Production configuration
├── requirements.txt     # Python dependencies
├── tasks.py             # Invoke automation tasks
└── README.md           # This file
```

## Customization

### Update Site Information

Edit `pelicanconf.py`:
- `SITENAME`: Your blog title
- `SITESUBTITLE`: Tagline
- `SOCIAL`: Your social media links
- `LINKS`: Resource links in sidebar

### Update Production Settings

Edit `publishconf.py`:
- `SITEURL`: Your Cloudflare Pages URL
- `CLOUDFLARE_ANALYTICS`: Your analytics token

### Add Images

Place images in `content/images/` and reference them in posts:
```markdown
![Alt text]({static}/images/photo.jpg)
```

## Learning Resources

- [Pelican Documentation](https://docs.getpelican.com/)
- [Markdown Guide](https://www.markdownguide.org/)
- [Cloudflare Pages Docs](https://developers.cloudflare.com/pages/)
- [Python Tutorial](https://docs.python.org/3/tutorial/)

## License

Content is © Pickem Boogerly. Code is available under the MIT License.

---

Built with Python and Pelican. Hosted on Cloudflare Pages.
