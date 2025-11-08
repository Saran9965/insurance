from pathlib import Path
import os
import sys

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-djj*tdrdq266@5nrz(4^9o!16n0@1q*j7-ihaq(1c#9gh+l=3^'

# Disable debug for production
DEBUG = False

# ✅ Allowed hosts (Render + local)
ALLOWED_HOSTS = ['insurance-ouk8.onrender.com', 'localhost', '127.0.0.1']

# ✅ CSRF trusted origins
CSRF_TRUSTED_ORIGINS = [
    'https://insurance-ouk8.onrender.com',
    'http://52.55.71.119:8000'
]

# ✅ Security for production
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# ✅ Static & Media settings
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

# ✅ WhiteNoise for static file serving
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ✅ Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'insuranceapp',
]

# ✅ Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ✅ URL & Templates
ROOT_URLCONF = 'insurance.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ✅ WSGI
WSGI_APPLICATION = 'insurance.wsgi.application'

# ✅ Database (SQLite for now)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ✅ Password validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ✅ Localization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ✅ Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
