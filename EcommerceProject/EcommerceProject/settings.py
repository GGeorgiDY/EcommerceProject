from pathlib import Path

from django.urls import reverse_lazy

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-)dq2d2_@s5bruq+4#*x)0$z0ukrzn@)hry5@hk2-kuxk5=6044'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    "EcommerceProject.EcommerceApp",
    "EcommerceProject.Accounts",
    "EcommerceProject.Cart",

    "debug_toolbar",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',

    # долното е нещо, което се изпълнява преди всеки един наш request - тоест когато от браузъра се поиска вю-то, това
    # е нещото което се случва посредата. След като е поискано от браузъра и преди да е стигнало до view кода ни.
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'EcommerceProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'EcommerceProject.wsgi.application'

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "ecommerce_db",
        "USER": "georgiadmin",
        "PASSWORD": "adminpass",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# статичните ми файлове ще бъдат достъпвани на static
STATIC_URL = '/static/'
# но ще се намират на директория staticfiles
STATICFILES_DIRS = (BASE_DIR / 'staticfiles',)

# медиафайловете ми файлове ще бъдат достъпвани на media
MEDIA_URL = '/media/'
# но ще се намират на директория media_files
MEDIA_ROOT = BASE_DIR / 'mediafiles'

# като натисна някакъв login бутон, да ме препраща на home страницата
LOGIN_REDIRECT_URL = reverse_lazy('home')
LOGIN_URL = '/account/login/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

INTERNAL_IPS = [
    '127.0.0.1',
]

# това е нещо с което казваме на джанго, че искаме за юзъри вече да не използваш твой си build-in юзър, а да използва този Accounts.AppUser
AUTH_USER_MODEL = 'Accounts.AppUser'
