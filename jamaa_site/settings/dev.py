from .common import *
from decouple import config

DEBUG = True
SECRET_KEY = 'django-insecure-@_duq9%$jx6%xf(snvz!m(77sumea$35w^&q^&e*r2-)#5tf%-'
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '172.16.27.124']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = config('GOOGLE_OAUTH2_KEY', default='')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = config('GOOGLE_OAUTH2_SECRET', default='')

# Security settings for development
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'