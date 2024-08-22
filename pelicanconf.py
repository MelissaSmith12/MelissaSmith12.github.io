from __future__ import unicode_literals
import os
import gettext

AUTHOR = 'Melissa Smith'
SITENAME = 'Datasmithing'
SITEDESCRIPTION = 'Habit coaching to help you get out of your own way'
SITEURL = 'http://localhost:8000'

# plugins
PLUGIN_PATHS = ['pelican-plugins']
# PLUGINS = []
PLUGINS = ['i18n_subsites']
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
#JINJA_ENVIRONMENT = {'trim_blocks': True, 'lstrip_blocks': True}

# theme and theme localization
THEME = 'pelican-fh5co-marble'
I18N_GETTEXT_LOCALEDIR = '\pelican-fh5co-marble\locale'
I18N_GETTEXT_DOMAIN = 'messages'
I18N_GETTEXT_NEWSTYLE = True
TIMEZONE = 'Europe/Zurich'
DEFAULT_DATE_FORMAT = '%a, %d %b %Y'
I18N_TEMPLATES_LANG = 'en_US'
DEFAULT_LANG = 'en'
# LOCALE = 'en_US'

# content paths
PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['blog']

# logo path, needs to be stored in PATH Setting
LOGO = '/images/square-logo-for-web-4.svg'

# special content
HERO = [
  {
    'image': '/images/hero/blur.jpg',
    'title': 'Do you struggle with staying focused on your goals?',
    'text': 'I provide accountability and troubleshooting to keep you on track.',
  }, {
    'image': '/images/hero/sounding_board.jpg',
    'title': 'Life is easier with a sounding board.',
    'text': 'I excel at asking insightful questions and problem solving.',
  }, {
    'image': '/images/hero/race_track.jpg',
    'title': 'When was the last time someone coached you to become your best?',
    'text': 'My only agenda is your growth and success.',
  }, {
    'image': '/images/hero/compass_map.jpg',
    'title': 'You know where you want to go.',
    'text': 'Together, we can get there.',
  }, {
    'image': '/images/hero/lego_wall.jpg',
    'title': 'Are you neurodiverse and face unique challenges?',
    'text': "I'm neurodiverse too and problem solving is my superpower.",
    },
]

# Social widget
SOCIAL = (
  ('Facebook', 'https://www.facebook.com/Datasmithing-106756724287010'),
  ('Twitter', 'https://twitter.com/datasmithing1'),
  ('Instagram', 'https://instagram.com/datasmithing'),
)

ABOUT = {
  'image': '/images/about/headshot.jpg',
  'mail': 'melissa@datasmithing.com',
  #'text': 'Learn more about Datasmithing or drop a message.',
  # 'link': 'contact.html',
  # the address is also taken for google maps
  'address': 'Cincinnati, Ohio',
}

# navigation and homepage options
DISPLAY_PAGES_ON_MENU = True
DISPLAY_PAGES_ON_HOME = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_TAGS_ON_MENU = False
USE_FOLDER_AS_CATEGORY = False
PAGE_ORDER_BY = 'order'

MENUITEMS = [
  ('Blog', 'archives.html'),
  #('Contact', 'contact.html')
]

DIRECT_TEMPLATES = [
  'index',
  'tags',
  'authors',
  'archives',
  #'search', # needed for tipue_search plugin
  #'contact' # needed for the contact form
]

# setup disqus
DISQUS_SHORTNAME = 'gitcd-dev'
DISQUS_ON_PAGES = False # if true its just displayed on every static page, like this you can still enable it per page

# setup google maps
GOOGLE_MAPS_KEY = 'AIzaSyCefOgb1ZWqYtj7raVSmN4PL2WkTrc-KyA'