# Django settings.
import os
import datetime
PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

gettext = lambda s: s

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Name', 'email@uncommonsense.com'),
)

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '&40th!_z-tge1p^%)z&x8bdysalx5w0evk8h_h28m&d3inb@oo'

# django-cms settings
LANGUAGE_CODE = 'en'

CMS_TEMPLATES = (
		('home.html', gettext('Homepage')),
)

CMS_PLACEHOLDER_CONF = {
    'example-conf': {
        'plugins': ('PodAdPlugin','TextPlugin','CMSNewsPlugin',),
        'name':gettext('Example Conf'),
        'extra_context': {"thumbnail_size":"220x121","crop":"smart"},
    },
}

LANGUAGES = (
        ('en', gettext('English')),
)

CMS_LANGUAGES = LANGUAGES

GOOGLE_MAPS_API_KEY = ""

CMS_SHOW_END_DATE = True
CMS_SHOW_START_DATE = True
CMS_PERMISSION = True
CMS_MODERATOR = False
CMS_URL_OVERWRITE = True
CMS_MENU_TITLE_OVERWRITE = True
CMS_SEO_FIELDS = True
CMS_REDIRECTS = True
CMS_SOFTROOT = True

VIDEO_AUTOPLAY = False
VIDEO_AUTOHIDE = False
VIDEO_FULLSCREEN = True
VIDEO_LOOP = False
VIDEO_AUTOPLAY = False
VIDEO_AUTOPLAY = False

VIDEO_BG_COLOR = "000000"
VIDEO_TEXT_COLOR = "FFFFFF"
VIDEO_SEEKBAR_COLOR = "13ABEC"
VIDEO_SEEKBARBG_COLOR = "333333"
VIDEO_LOADINGBAR_COLOR = "828282"
VIDEO_BUTTON_OUT_COLOR = "333333"
VIDEO_BUTTON_OVER_COLOR = "000000"
VIDEO_BUTTON_HIGHLIGHT_COLOR = "FFFFFF"

DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS" : False,
}

# Allowed IPs for the Django Debug Toolbar
INTERNAL_IPS = ('127.0.0.1',)

CMS_USE_TINYMCE = True

# TinyMCE config
TINYMCE_DEFAULT_CONFIG = {
		"mode" : "textareas",
		"theme" : "advanced",
		#"spellchecker_rpc_url" : "/tinymce/spellchecker/",
		#"plugins" : "safari,pagebreak,style,layer,table,save,advhr,advimage,advlink,emotions,iespell,inlinepopups,insertdatetime,preview,media,searchreplace,print,contextmenu,paste,directionality,fullscreen,noneditable,visualchars,nonbreaking,xhtmlxtras,template",
		"plugins" : "pagebreak,style,advhr,spellchecker,inlinepopups,contextmenu,paste,directionality,noneditable,xhtmlxtras,table,advlink",

		"theme_advanced_buttons1" : "cut,copy,paste,pastetext,pasteword,|,bold,italic,charmap,table,|,formatselect",
		"theme_advanced_buttons2" : "bullist,|,outdent,indent,blockquote,|,undo,redo,|,anchor,link,unlink,|,hr,|,code",
		"theme_advanced_buttons3" : "",
		"theme_advanced_buttons4" : "",
		#"theme_advanced_buttons1" : "save,newdocument,|,bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,styleselect,formatselect,fontselect,fontsizeselect",
		#"theme_advanced_buttons2" : "cut,copy,paste,pastetext,pasteword,|,search,replace,|,bullist,numlist,|,outdent,indent,blockquote,|,undo,redo,|,link,unlink,anchor,image,cleanup,help,code,|,insertdate,inserttime,preview,|,forecolor,backcolor",
		#"theme_advanced_buttons3" : "tablecontrols,|,hr,removeformat,visualaid,|,sub,sup,|, charmap,emotions,iespell,media,advhr,|,print,|,ltr,rtl,|,fullscreen",
		#"theme_advanced_buttons4" : "insertlayer,moveforward,movebackward,absolute,|,styleprops,|,cite,abbr,acronym,del,ins,attribs,|,visualchars,nonbreaking,template,pagebreak",
		"theme_advanced_toolbar_location" : "top",
		"theme_advanced_toolbar_align" : "left",
		"theme_advanced_statusbar_location" : "bottom",
		"theme_advanced_resizing" : True,
		"theme_advanced_blockformats" : "p,h1,h2,h3,h4,blockquote",
		#"content_css":"/media/css/tinymce.css?blarg=%s" % (datetime.datetime.now().time()),
	}

CMS_PLUGIN_TEXT_TINYMCE_CONFIG = TINYMCE_DEFAULT_CONFIG

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)


# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
    'django.template.loaders.eggs.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
        "django.core.context_processors.auth",
        'django.core.context_processors.debug',
        "django.core.context_processors.i18n",
        "django.core.context_processors.request",
        "django.core.context_processors.media",
        "cms.context_processors.media",
        'django.contrib.messages.context_processors.messages',
)


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.media.PlaceholderMediaMiddleware',
)

ROOT_URLCONF = 'pythonkc.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
	os.path.join(PROJECT_DIR,'templates'),
)

FIXTURE_DIRS = (
    os.path.join(PROJECT_DIR, "fixtures"),
)

EMAIL_HOST= ''

EMAIL_HOST_USER = ''

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

EMAIL_HOST_PASSWORD = ''

EMAIL_PORT = '587'

EMAIL_USE_TLS = True

INSTALLED_APPS = (
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'cms',
    'cms.plugins.text',
    'cms.plugins.picture',
    'cms.plugins.link',
    'cms.plugins.file',
    'cms.plugins.snippet',
    'cms.plugins.googlemap',
    'mptt',
    'publisher',
    'reversion',
    'debug_toolbar',
    'tinymce',
    'menus',
    'cms.plugins.video',
    'cms.plugins.inherit',
    'cms.plugins.twitter',
    'south',
    'filer',
    'easy_thumbnails',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_image',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_video',
    'appmedia',
)

#admin tools
ADMIN_TOOLS_INDEX_DASHBOARD = 'dashboard.CMSIndexDashboard'

try:
    from settings_local import *
except ImportError:
    pass