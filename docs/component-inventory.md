# Component Inventory - Flex Theme

This project uses the **Flex** theme. UI components are implemented as Jinja2 templates and partials.

## Main Layout Templates
| Template | Location | Purpose |
| :--- | :--- | :--- |
| `base.html` | `/templates/` | The shell for all pages (header, footer, sidebar). |
| `index.html` | `/templates/` | The main listing page for blog posts. |
| `article.html` | `/templates/` | The detailed view for a single blog post. |
| `page.html` | `/templates/` | Layout for static pages. |

## Partial Components (Reusable)
Located in `themes/Flex/templates/partial/`:

| Component | Description |
| :--- | :--- |
| `sidebar.html` | The site's primary navigation and brand area. |
| `nav.html` | Main menu navigation. |
| `footer.html` | Copyright and build information. |
| `pagination.html` | List navigation for multiple pages. |
| `disqus.html` | Commenting system integration (currently disabled). |
| `cf_analytics.html` | Cloudflare Web Analytics beacon. |
| `og_article.html` | OpenGraph metadata for social sharing. |
| `social.html` | Social media icons and links. |
| `translations.html` | Language switching (if enabled). |

## Styling Components
- **CSS:** Main styles are in `themes/Flex/static/css/`.
- **Custom Overrides:** `content/static/css/custom.css` is injected via `pelicanconf.py`.
