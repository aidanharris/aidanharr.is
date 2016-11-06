#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

from base64 import b64encode

AUTHOR = 'Aidan Harris'
SITENAME = 'Aidan Harris'
SITEURL = ''

THEME = 'theme/simple'

PATH = 'content'

STATIC_PATHS = [
    "uploads",
    "CNAME"
]

EXTRA_PATH_METADATA = {
    'CNAME': {'path': 'CNAME'}
}

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

DISPLAY_PAGES_ON_MENU = False

DISPLAY_CATEGORIES_ON_MENU = False

DISPLAY_MAIN_NAVIGATION = True

MAIN_NAVIGATION_PAGES = [
    "Portfolio",
    "",
    "Legal",
    ""
]

MAIN_NAVIGATION  = [
    (
        ('All', '#'),
        ('Web Design', '#'),
    ),
    (
        ('Contact', '#'),
    ),
    (
        ('Copyright', '#'),
        ('Privacy Policy', '#'),
    ),
    (
        ('Glossary', '#'),
    )
]

with open(THEME + "/templates/avatar.svg", "rb") as avatar:
    AVATAR = str(b64encode(avatar.read()))[2:-1]
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
