#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

from base64 import b64encode
from os import environ as env

AUTHOR = 'Aidan Harris'
SITENAME = 'Aidan Harris'

SITEPROTOCOL = 'http';

SITEURL = str(open('content/CNAME')).split("\n")
SITEURL = SITEPROTOCOL + '://' + SITEURL[0]

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

def defaultSettings():
    FEED_ALL_ATOM = True
    CATEGORY_FEED_ATOM = True
    TRANSLATION_FEED_ATOM = True
    AUTHOR_FEED_ATOM = True
    AUTHOR_FEED_RSS = True
    RELATIVE_URLS = False

try:
    if ("PELICAN_ENV" in env and env["PELICAN_ENV"] != "production"):
        # Feed generation is usually not desired when developing
        FEED_ALL_ATOM = False
        CATEGORY_FEED_ATOM = False
        TRANSLATION_FEED_ATOM = False
        AUTHOR_FEED_ATOM = False
        AUTHOR_FEED_RSS = False
        RELATIVE_URLS = True
    else:
        defaultSettings()
except Exception:
    defaultSettings()
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
        ('Contact', '/contact'),
    ),
    (
        ('Copyright', '/copyright'),
        ('Privacy Policy', '/privacy'),
    ),
    (
        ('Glossary', '/glossary'),
    )
]

LIGHT_HEADING_COLOUR = "#fafafa";
DARK_HEADING_COLOUR = "#424242";

# Base64 encoded svg to inline in page headers for performance reasons
with open(THEME + "/templates/avatar.svg", "rb") as avatar:
    AVATAR = str(b64encode(avatar.read()))[2:-1]
