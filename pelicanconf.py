#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'EUREC4A Community'
SITENAME = 'EUREC4A Hackathon 2020'
SITEURL = 'https://eurec4a.github.io/hackathon2020_blog/'

PATH = 'content'

MARKUP = ("md", "ipynb")

TIMEZONE = 'UTC'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('EUREC4A', 'http://eurec4a.eu/'),
        )

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

from pelican_jupyter import markup as nb_markup
PLUGINS = [nb_markup]

IGNORE_FILES = [".ipynb_checkpoints"]
