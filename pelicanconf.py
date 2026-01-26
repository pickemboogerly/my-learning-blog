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

DEFAULT_PAGINATION = 10

# Theme Configuration
THEME = "themes/Flex"

# Flex Theme Settings
SITETITLE = SITENAME
SITESUBTITLE = "AI Slop and Coding Adventures"
SITEDESCRIPTION = "A blog documenting my experiences and projects in Python, AI, coding, and generating AI slop."
SITELOGO = 'images/raw/boogerly_cyberpunk.png'  # Cyberpunk slime logo

# Browser Tab Icon
FAVICON = 'images/favicon.ico'  # Add path to favicon later (e.g., '/images/favicon.ico')

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
    ("github", "https://github.com/pickemboogerly"),  
    ("mastodon", "https://dobbs.town/@boogerly"), 
    
)

# Disable unused Flex features for now
DISABLE_URL_HASH = False

# Enable search (optional)
# Requires installing stork-search or tipue_search plugin

# Custom CSS - Cyberpunk theme based on logo
STATIC_PATHS = ['images', 'static', 'extra']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
}
CUSTOM_CSS = 'static/css/custom.css'

# Discourage search engine indexing
ROBOTS = 'noindex, nofollow'
