from common import *
import dj_database_url, os

PRODUCTION = True

# Debug Settings
DEBUG = bool(os.environ.get('DJANGO_DEBUG', ''))
TEMPLATE_DEBUG = DEBUG
THUMBNAIL_DEBUG = DEBUG

# Http Settings
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
PREPEND_WWW = False

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']

# Database settings sourced from Heroku
DATABASES = { 'default': dj_database_url.config() }

# CDN settings
AWS_ACCESS_KEY_ID = os.environ.get('AWS_KEY')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET')
# AWS_STORAGE_BUCKET_NAME = 'static.rocketlistings.com'
# see http://developer.yahoo.com/performance/rules.html#expires
AWS_HEADERS = {
    'Cache-Control': 'max-age=86400, pubic',
}

STATICFILES_STORAGE = 'settings.s3storages.StaticStorage'
DEFAULT_FILE_STORAGE = 'settings.s3storages.MediaStorage'

UPLOAD_DIR = 'uploads'

# not using static.rocketlistings.com because its CNAME 
# redirects to 'static.rocketlistings.com.s3-website-us-east-1.amazonaws.com' 
# and that doesn't work with SSL apparently because of the '.' char.
STATIC_URL = '//s3.amazonaws.com/STATIC_BUCKET_NAME/'
MEDIA_URL = '//s3.amazonaws.com/MEDIA_BUCKET_NAME/'
#AWS_S3_CUSTOM_DOMAIN = "s3.amazonaws.com/media.rocketlistings.com"
AWS_S3_SECURE_URLS = False

##CACHE_MIDDLEWARE_ALIAS = 'local-rocket-cache'
##CACHE_MIDDLEWARE_SECONDS = 300
##CACHE_MIDDLEWARE_KEY_PREFIX = 'rocketlistings'
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True # Caching only anonymous pages.

# Logging settings
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', 'console'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
