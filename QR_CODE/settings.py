from pathlib import Path
import os
from pipes import Template
from django.contrib.messages import constants as message_s

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATES_DIR = os.path.join(BASE_DIR / 'templates')
STATIC_DIR = os.path.join(BASE_DIR / 'static')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-jkck*0-nb&uj0tqjnrk@$-&_3wtto90!vn-5&mvu5j)o55ym@!'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False
DEBUG = True

# ALLOWED_HOSTS = ['qrcode-p.herokuapp.com','127.0.0.1:8000']
ALLOWED_HOSTS = ['127.0.0.1','192.168.0.107']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    'django_filters',
    'admin_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'QR_CODE.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
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

WSGI_APPLICATION = 'QR_CODE.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# for docker 
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'qrcode',
#         'USER': 'root',
#         'PASSWORD': '123456',
#         'HOST': 'db',  
#         'PORT': '3306',        
#     }
# }


# for local machin
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'qrcode',
        'USER':'root',
        'PASSWORD':'',
        'HOSTNAME':'localhost',
        'DATABASE':'qrcode',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'  # timezone change for india
 
TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# FOR OTP
AUTH_KEY = '378254Aw1grgEXTw62a87f89P1'

STATIC_URL = '/static/'
# FOR STATIC IMAGE
STATICFILES_DIRS=[STATIC_DIR,]

MEDIA_ROOT =  os.path.join(BASE_DIR, '') 
MEDIA_URL = '/'
    
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# django message tag changed color
MESSAGE_TAGS={
    message_s.ERROR:'danger'
}

# set session time FOR 1 MIN 
SESSION_EXPIRE_AT_BROWSER_CLOSE = True     # opional, as this will log you out when browser is closed
SESSION_COOKIE_AGE = 600                 # 0r 5 * 60, same thing
SESSION_SAVE_EVERY_REQUEST = True          # Will prrevent from logging you out after 300 secondsSET_COOKIE_NAME='qrcode_application_novetrics'
# SET_COOKIE_PATH='/home'
# SESSION_ENGINE='django.contrib.sessions.backends.file'
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True
SESSION_TIMEOUT_REDIRECT = 'http://127.0.0.1:8000/login_page/'  # redirect to whatever page
SESSION_IDLE_TIMEOUT = 600


# for email integration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'shaikh.novetrics@gmail.com'
EMAIL_HOST_PASSWORD = 'efyhtdpztphnjyno'
