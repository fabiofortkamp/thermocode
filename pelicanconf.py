#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Fábio Fortkamp'
SITENAME = 'thermocode'
SITEURL = ''

FAVICON = ''

USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = 'Article'

DEFAULT_DATE_FORMAT = '%Y-%m-%d'

DEFAULT_METADATA = {'status': 'draft',}

IGNORE_FILES = ['.#*', "*~"]

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
ARTICLE_SAVE_AS = 'blog/{slug}.html'

PAGE_URL = 'pages/{slug}'
PAGE_SAVE_AS = 'pages/{slug}.html'

CATEGORY_URL = 'blog/category/{slug}'
CATEGORY_SAVE_AS = 'blog/category/{slug}.html'

TAG_URL = 'blog/tag/{slug}'
TAG_SAVE_AS = 'blog/tag/{slug}.html'

THEME = 'pelican-bootstrap3/'
