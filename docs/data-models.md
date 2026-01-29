# Data Models - Boogerly

The "data" in this static site project is managed through Markdown metadata and configuration variables.

## Blog Post Model (Markdown)
Each post in `content/*.md` follows this schema:

| Field | Required | Description |
| :--- | :--- | :--- |
| `Title` | Yes | The title of the post. |
| `Date` | Yes | ISO format (YYYY-MM-DD HH:MM). |
| `Category` | Yes | Primary grouping (about, tech, tutorial). |
| `Tags` | No | Comma-separated list for discovery. |
| `Slug` | Yes | URL-friendly name. |
| `Authors` | No | Overrides default site author. |
| `Summary` | Yes | Snippet for the index and RSS feeds. |
| `Status` | No | Set to `draft` to hide from production. |

## Page Model (Markdown)
Static pages (like archives or tags) are often auto-generated, but custom pages in `content/pages/` (if added) follow a similar schema but without a `Date`.

## Global Site Configuration (`pelicanconf.py`)
| Variable | Description |
| :--- | :--- |
| `AUTHOR` | Default site author. |
| `SITENAME` | Site title. |
| `SITEURL` | Root URL (empty for local development). |
| `THEME` | Path to the Flex theme. |
| `LINKS` | Tuple of (name, url) for the sidebar. |
| `SOCIAL` | Tuple of (icon, url) for social icons. |

## Theme Variables (Flex Specific)
- `SITETITLE`
- `SITESUBTITLE`
- `SITEDESCRIPTION`
- `SITELOGO`
- `PYGMENTS_STYLE` (Code highlighting)
