"""
Django settings for test_auth project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'w@k)(d*1-+ou$(ux)p8&a1mo)^^^4=epf%_m=-2*zigajhqoqn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'sslserver',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myauth',
    'myapp',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
#    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'test_auth.urls'

WSGI_APPLICATION = 'test_auth.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SESSION_EXPIRE_AT_BROWSER_CLOSE=True
os.environ['wsgi.url_scheme'] = 'https'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

#AUTHENTICATION_BACKENDS=('myauth.SettingsBackend.SettingsBackend', 'django.contrib.auth.backends.ModelBackend',)
AUTHENTICATION_BACKENDS=('myauth.SettingsBackend.SettingsBackend', )

ADMIN_LOGIN = 'admin'
ADMIN_PASSWORD = 'pbkdf2_sha256$12000$cQVmovdDUk7t$XPlZ4C+ZK/ypWUtIQCs+jPxZZhDHgN7yYvU2Oc0OIGE='
