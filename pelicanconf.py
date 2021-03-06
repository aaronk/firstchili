#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime
from dateutil.tz import tzlocal

PLUGIN_PATHS = ['../pelican-plugins/']
PLUGINS = ['tag_cloud.tag_cloud',
           'interlinks',
           'pelican-toc',
           'tipue_search',
           'rmd_reader',
           'pin_to_top',
           'events',
           ]

PLUGIN_EVENTS = {
 'ics_fname': 'calendar.ics',
}

KNITR_OPTS_CHUNK = {
    'fig.path': 'images/',
}
MD_EXTENSIONS = (['codehilite(use_pygments=True)', 'fenced_code'])
TOC = {
    'TOC_HEADERS' : '^h[1-3]',  # What headers should be included in the generated toc
                                # Expected format is a regular expression
    'TOC_RUN'     : 'true'      # Default value for toc generation, if it does not evaluate
                                # to 'true' no toc will be generated
}
AUTHOR = u'Aaron Kitzmiller'
SITENAME = u"AKtion Items"
SITEURL = 'http://www.firstchili.org'
TAGS_URL = 'tags.html'
# PATH = 'content2'
BANNER = True
BANNER_ALL_PAGES = False
DISPLAY_PAGES_ON_MENU = True
FAVICON = 'favicon.ico?v=1'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

PYGMENTS_STYLE = 'github'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
FEED_ALL_RSS = 'rss.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Sidebar stuff, Link images are first
LINKS = (
  ('/images/us-flag-icon-31.png', 'ActBlue', 'https://secure.actblue.com/'),
  ('/images/us-flag-icon-31.png', 'DailyKos Action', 'https://www.dailykos.com/campaigns'),
)

SHOW_ARTICLE_AUTHOR = True
# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DISPLAY_RECENT_POSTS_ON_SIDEBAR = False
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = True
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 100

DISPLAY_CATEGORIES_ON_SIDEBAR = False
DISPLAY_CATEGORIES_ON_MENU = True

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

# Common URLs
#INTERLINKS = {
#    'account_request': 'https://account.rc.fas.harvard.edu/request/',
# }

DIRECT_TEMPLATES = ['search', 'index', 'archives', 'tags']

CUTOFF_DATE = datetime(2090, 1, 1, 0, 0, 0, tzinfo=tzlocal())
