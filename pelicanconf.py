#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Fábio Fortkamp'
SITENAME = 'thermocode.net'
SITEURL = ''
SITESUBTITLE = 'The research blog of ' + AUTHOR

TYPOGRIFY = True 

FAVICON = ''



USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = 'Article'

DEFAULT_DATE_FORMAT = '%Y-%m-%d'
DEFAULT_DATE = 'fs'

DEFAULT_METADATA = {'status': 'published',}

IGNORE_FILES = ['.#*', "*~"]

SHOW_ARTICLE_CATEGORY = True

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

ARTICLE_URL = 'blog/{slug}'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'

PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'

CATEGORY_URL = 'blog/category/{slug}'
CATEGORY_SAVE_AS = 'blog/category/{slug}/index.html'

TAG_URL = 'blog/tag/{slug}'
TAG_SAVE_AS = 'blog/tag/{slug}/index.html'

THEME = 'pelican-bootstrap3/'

BOOTSTRAP_THEME = 'spacelab'

DISPLAY_CATEGORIES_ON_MENU = False

SOCIAL = (('@fabiofortkamp', 'http://twitter.com/fabiofortkamp', 'twitter'),
          ('My Github page', 'http://github.com/fabiofortkamp', 'github'),
          ('Meu blog em português', 'http://fabiofortkamp.com/', 'pencil'))

DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_CATEGORIES_ON_SIDEBAR = True

# Creative commons license
CC_LICENSE = "CC-BY-NC"

# Attach draft status to future posts]
WITH_FUTURE_DATE = False

# ---
# Plugins

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ["series", "render_math"]

## Series

SERIES_TEXT = "Part %(index)s of a series on %(name)s"

# show series under the title
SHOW_SERIES = False

# show series on the sidebar
DISPLAY_SERIES_ON_SIDEBAR = True

# Static settings

CUSTOM_CSS = 'static/custom.css'

# Tell Pelican to add 'extra/custom.css' to the output dir
STATIC_PATHS = ['images', 'extra/custom.css']

# Tell Pelican to change the path to 'static/custom.css' in the output dir
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'}
}
