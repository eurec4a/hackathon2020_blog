#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'EUREC4A Community'
SITENAME = 'EUREC4A Hackathon 2020'
SITETITLE = "EUREC4A"
SITESUBTITLE = "Hackathon 2020"
SITEURL = '/'

PATH = 'content'

MARKUP = ("md", "ipynb")

THEME = 'themes/flex'
SITELOGO = SITEURL + "images/logo_eurec4a.png"
MAIN_MENU = True

_menuitems = [('Archives', 'archives.html'),
              ('Categories', 'categories.html'),
              ('Tags', 'tags.html'),
              ('Authors', 'authors.html'),]

def make_menu(basepath):
    return [(name, basepath + link) for name, link in _menuitems]

MENUITEMS = make_menu(SITEURL)
TIMEZONE = 'UTC'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('EUREC4A Campaign Website', 'http://eurec4a.eu/'),
        )

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

STATIC_PATHS = ['images']

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

from pelican_jupyter import markup as nb_markup
PLUGINS = [nb_markup]

IGNORE_FILES = [".ipynb_checkpoints"]
