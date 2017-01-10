#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date
from base64 import b64encode
from os import environ as env
import subprocess

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

CURRENT_YEAR = str(date.today().year)

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

DISPLAY_MAIN_NAVIGATION = False

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

MATERIAL_DESIGN_LITE_VERSION = "1.3.0"

p = subprocess.Popen([
    "curl",
    "-q",
    "-s",
    "-L",
    "https://code.getmdl.io/" + MATERIAL_DESIGN_LITE_VERSION + "/material.grey-blue.min.css"
], stdout=subprocess.PIPE)

MATERIAL_DESIGN_LITE_CSS = p.communicate()[0].decode('utf-8', 'ignore')

PYGMENTS_THEME = 'solarized-light'

if PYGMENTS_THEME == 'solarized-light':
    PYGMENTS_URL = 'https://gist.githubusercontent.com/aidanharris/725d960a62e1a264062eb8d219baa24f/raw/80abaa1791271466393e8264f286c1eb9240d059/solarized-light.css'
elif PYGMENTS_THEME == 'solarized-dark':
    PYGMENTS_URL = 'https://gist.githubusercontent.com/aidanharris/725d960a62e1a264062eb8d219baa24f/raw/80abaa1791271466393e8264f286c1eb9240d059/solarized-dark.css'

if PYGMENTS_THEME != 'solarized-light' and PYGMENTS_THEME != 'solarized-dark':
    PYGMENTS_CSS = subprocess.Popen([
        "pygmentize",
        "-S",
        PYGMENTS_THEME,
        "-f",
        "html",
        "-a",
        ".highlight"
    ], stdout=subprocess.PIPE)

    PYGMENTS_CSS = PYGMENTS_CSS.communicate()[0].decode('utf-8', 'ignore')
else:
    PYGMENTS_CSS = subprocess.Popen([
        "curl",
        "-q",
        "-s",
        "-L",
        PYGMENTS_URL
    ], stdout=subprocess.PIPE)

    PYGMENTS_CSS = PYGMENTS_CSS.communicate()[0].decode('utf-8', 'ignore')

DEVICONS_VERSION = "1.8.0";
FONT_AWESOME_VERSION = "4.6.3";

LIGHT_HEADING_COLOUR = "#fafafa";
DARK_HEADING_COLOUR = "#424242";

# Inline CSS to keep Google Page Speed Test Happy
# To Do:
#   * I should probably think about inlining only the critical CSS
#     since dumping tonnes of lines of CSS feels a bit dirty. But
#     hey, if it keeps Google happy and gives me a perfect score
#     I'm not complaining ;)
with open(THEME + "/static/css/style.min.css", "r") as css:
    CSS = css.read()
# Base64 encoded svg to inline in page headers for performance reasons
with open(THEME + "/templates/avatar.svg", "rb") as avatar:
    AVATAR = str(b64encode(avatar.read()))[2:-1]
