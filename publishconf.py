# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = "https://my-learning-blog.pages.dev"
RELATIVE_URLS = False

# RSS/ATOM Feed Configuration
FEED_ALL_ATOM = "feeds/all.atom.xml"
FEED_ALL_RSS = "feeds/all.rss.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
TAG_FEED_ATOM = "feeds/tag-{slug}.atom.xml"
FEED_MAX_ITEMS = 20

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

# Cloudflare Web Analytics (Free & Privacy-Friendly)
# After setting up Cloudflare Pages, go to:
# Dashboard > Analytics & Logs > Web Analytics
# Create a new site and get your beacon token
# Then uncomment and add your token:
# CLOUDFLARE_ANALYTICS = "YOUR_BEACON_TOKEN_HERE"

# Optional: Disqus Comments (if you want to add comments later)
# Sign up at https://disqus.com and add your site shortname:
# DISQUS_SITENAME = "boogerly"

# Note: We're using Cloudflare Web Analytics instead of Google Analytics
# for better privacy and performance on Cloudflare Pages
