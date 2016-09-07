"""
Django settings for mainsite project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
from djangae.settings_base import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# GLOBAL Settings

SITE_ID = 5302669702856704

SITE_TITLE = "Daniel Jackson"
SITE_TAGLINE = ""
SITE_DESCRIPTION = ""
GOOGLE_ANALYTICS = ""

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'o%$vzmks_7_b==cvomwxt8=4kh$dp&xb#31-)73ui$1)5!g-(+'

# SECURITY WARNING: don't run with debug turned on in production!
import os
if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine'):
    DEBUG = False
else:
    DEBUG = True

ALLOWED_HOSTS = ['*','localhost', '127.0.0.1', 'cloudplayapp.com', 'www.cloudplayapp.com', 'danielmarkjackson.com', 'www.danielmarkjackson.com', 'danj.co', 'www.danj.co']


# Application definition

INSTALLED_APPS = (
    'djangae',                  # Used for Google Datastore and Google Cloud Storage as a backend
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'website',
    'api',
    'geoposition',
)

SUIT_CONFIG = {
    'ADMIN_NAME': 'Daniel Jackson'
}

TEMPLATE_CONTEXT_PROCESSORS = TCP + [
    'django.core.context_processors.request',
]

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'djangae.contrib.security.middleware.AppEngineSecurityMiddleware',
)

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'project.context_processors.global_settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# Local Database
# Using Local DB for testing prior to release
# To start the local db: mysql.server start

CLOUD_STORAGE_BUCKET = 'tams-142602.appspot.com'

# [START db_setup]
DATABASES = {
    'default': {
        'ENGINE': 'djangae.db.backends.appengine',
    }
}


AUTH_USER_MODEL = 'api.MyUser'

TOKEN_EXPIRATION_SEC = 604800 #7 days
TOKEN_MAX_PER_CLIENT = 5

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#for geoposition
GEOPOSITION_MAP_OPTIONS = {
    'minZoom': 3,
    'center_on_current':True,
    'scrollwheel':True,
    'zoom':13,
    'center': {'lat': 38.5815719, 'lng': -121.49439960000001},
}

GEOPOSITION_MARKER_OPTIONS = {
    'cursor': 'move',
    'position_on_current':True,
    'position': {'lat': 38.5815719, 'lng': -121.49439960000001},
}

GEOPOSITION_MAP_WIDGET_HEIGHT = 500
GEOPOSITION_GOOGLE_MAPS_API_KEY = 'AIzaSyC5XxGIUssSSOzGqvhOnNOtn7PGbAfYYOk'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_ROOT = "static"
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'