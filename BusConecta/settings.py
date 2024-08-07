

# https://docs.render.com/deploy-django


# importamos os para la produccion
import os 
#  Importamos el conector de PosterSQL
import dj_database_url

from pathlib import Path



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-f00zjvc(19s0#%zeah-1db&@3c4xn3haaj&mqq*lm^bj=y$0f4'

# # Secret key de ------- RENDER  ----------------
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# pra producccion : [ False]
# DEBUG = False
# Me ha interasado mucho para ver el error en produccion
# DEBUG = os.environ.get("DEBUG", "False").lower() == "True"


# hago lo siguiente - ORIGINAL 
ALLOWED_HOSTS = ["*"]

#Para produccon
# ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(" ")



# variable de entorno que da ------ RENDER ------- 



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'AppBussConecta',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # ----------------- render ---------------
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # ----------------------------------------
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'BusConecta.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'BusConecta.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# base de datos de : POSTGRESQL - que he codigo de Render


# DATABASES["default"] = dj_database_url.parse(database_url)

DATABASES = {
    'default': dj_database_url.parse("postgresql://bbdd_bus_conecta_user:pdAYWFQ8GvBTJmXGLBMopdyasHRgTaUy@dpg-cqpro6g8fa8c73eliic0-a.oregon-postgres.render.com/bbdd_bus_conecta")
        # Replace this value with your local database's connection string.
        # default='postgresql://postgres:postgres@localhost/postgres',
        # conn_max_age=600

}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'es-ES'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/


# if not DEBUG:    # Tell Django to copy static assets into a path called `staticfiles` (this is specific to Render)
#     STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
#     # Enable the WhiteNoise storage backend, which compresses static files to reduce disk use
#     # and renames the files with unique names for each version to support long-term caching
#     STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

#



# Archivos estáticos
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    # # Directorios adicionales donde Django también buscará archivos estáticos
# STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'static'),]

# Enable the WhiteNoise storage backend, which compresses static files to reduce disk use
# and renames the files with unique names for each version to support long-term caching
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'



# Configuración de archivos multimedia

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
