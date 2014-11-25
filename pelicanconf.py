#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'ylegall'
SITENAME = u'Yann Le Gall'
TAGLINE = 'art, programming, fitness'
SITEURL = 'http://localhost:8000'
FAVICON = '/images/favicon.ico'

PATH = 'content'
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = u'en'

THEME = "themes/pelican-svbhack"
#THEME = "themes/pelican/bootlex"
#THEME = "themes/chunk"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

ARTICLE_URL = 'posts/{slug}.html'	#The URL to refer to an article.
ARTICLE_SAVE_AS = 'posts/{slug}.html'

# Blogroll
LINKS = (
	('DeviantArt', 'http://selonus.deviantart.com/'),
)

# Social widget
SOCIAL = (
	('Github', 'github.png', 'https://github.com/ylegall/'),
	('Twitter', '', 'https://twitter.com/Yann_LeGall'),
    ('Instagram', '', 'http://instagram.com/ylegall'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ['plugins']
PLUGINS = ['assets', 'sitemap', 'gravatar']

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'}
}

# static paths will be copied without parsing their contents
STATIC_PATHS = [
	'images',
	'extra/robots.txt',
]

USER_LOGO_URL = 'http://www.gravatar.com/avatar/53a8a8962e717a4782c48383feef6f43.png'