#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from urllib.parse import urlencode

AUTHOR = 'EUREC4A Community'
SITENAME = 'EUREC4A Hackathon 2020'
SITETITLE = "EUREC4A"
SITESUBTITLE = "Hackathon 2020"
SITEURL = ''

PATH = 'content'

MARKUP = ("md", "ipynb")

THEME = 'themes/flex'
SITELOGO = SITEURL + "/images/logo_eurec4a.png"
MAIN_MENU = True

_menuitems = [('Archives', '/archives.html'),
              ('Categories', '/categories.html'),
              ('Tags', '/tags.html'),
              ('Authors', '/authors.html'),]

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
LINKS = (('eurec4a.eu', 'http://eurec4a.eu/'),
         ('operational center', 'https://observations.ipsl.fr/aeris/eurec4a/'),
         ('Thredds Catalog', 'https://observations.ipsl.fr/thredds/catalog/EUREC4A/catalog.html'),
        )

# Social widget
SOCIAL = (
    ('github', 'https://github.com/eurec4a'),
)

STATIC_PATHS = ['images']

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

from pelican_jupyter import markup as nb_markup
PLUGINS = [nb_markup]

IGNORE_FILES = [".ipynb_checkpoints"]

def binder_link(data_path="",
                env_repo="https://github.com/eurec4a/hackathon_env",
                data_repo="https://github.com/eurec4a/hackathon2020_blog",
                env_branch="master",
                data_branch="master",
                data_prefix="content/",
                binder="https://mybinder.org"):
    nbgitpuller_src= urlencode({"repo": data_repo, "urlpath": "tree/{}/{}{}".format(data_repo.split("/")[-1], data_prefix, data_path), "branch": data_branch})
    nbgitpuller_conf = urlencode({"urlpath": "git-pull?{}".format(nbgitpuller_src)})
    group, repo = env_repo.split("/")[-2:]
    return "{}/v2/gh/{}/{}/{}?{}".format(binder, group, repo, env_branch, nbgitpuller_conf)

JINJA_FILTERS = {'binder_link': binder_link}
