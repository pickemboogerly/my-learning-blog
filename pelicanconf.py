AUTHOR = 'Pickem Boogerly'
SITENAME = 'Boogerly'
SITEURL = ""

PATH = "content"

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Theme Configuration
THEME = "themes/Flex"

# Flex Theme Settings
SITETITLE = SITENAME
SITESUBTITLE = "Learning Python, AI & Code"
SITEDESCRIPTION = "A blog documenting my journey learning Python and AI-assisted coding"
SITELOGO = 'images/raw/boogerly_cyberpunk.png'  # Cyberpunk slime logo

# Browser Tab Icon
FAVICON = None  # Add path to favicon later (e.g., '/images/favicon.ico')

# Copyright Information
COPYRIGHT_YEAR = 2026
COPYRIGHT_NAME = AUTHOR

# Main Menu
MAIN_MENU = True
MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)

# Code Highlighting
PYGMENTS_STYLE = "monokai"  # Code syntax highlighting theme (dark theme)
PYGMENTS_STYLE_DARK = "monokai"  # For dark mode

# Use document-relative URLs for development
RELATIVE_URLS = True

# Sidebar Links
LINKS_WIDGET_NAME = "Resources"
LINKS = (
    ("Pelican Docs", "https://docs.getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Markdown Guide", "https://www.markdownguide.org/"),
)

# Social Links - Customize these with your own profiles
SOCIAL_WIDGET_NAME = "Connect"
SOCIAL = (
    ("github", "https://github.com/yourusername"),  # Update with your GitHub
    ("twitter", "https://twitter.com/yourusername"),  # Update with your Twitter
    # Add more as needed: linkedin, rss, etc.
)

# Disable unused Flex features for now
DISABLE_URL_HASH = False

# Enable search (optional)
# Requires installing stork-search or tipue_search plugin

# Custom CSS - Cyberpunk theme based on logo
STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
}
CUSTOM_CSS = 'static/custom.css'
