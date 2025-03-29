from .common import *
from decouple import config
import dj_database_url
import os
DEBUG = False
SECRET_KEY = config('SECRET_KEY')
ALLOWED_HOSTS = ['smumsj.onrender.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        # Use a default if env var is not set
        'NAME': os.getenv('DB_NAME', 'postgres'),
        # Use a default if env var is not set
        'USER': os.getenv('DB_USER', 'postgres'),
        # Use a default if env var is not set
        'PASSWORD': os.getenv('DB_PASSWORD', '0966143454Sahm'),
        'HOST': os.getenv('DB_HOST'),
        # Use a default if env var is not set
        'PORT': os.getenv('DB_PORT', '5432'),
        # 'OPTIONS': {
        #     'sslmode': 'require',  # This enforces SSL/TLS connection
        # }
    }
}


# HTTPS Settings
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')

# Social Auth
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = config('GOOGLE_OAUTH2_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = config('GOOGLE_OAUTH2_SECRET')

# Add production middleware
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Security headers
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True