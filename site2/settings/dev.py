from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+f7^_-h(c$ic==2&1an)%kb1fo%r*6%%v!d^i4g5&ku1tw3lia'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

WAGTAILADMIN_STATIC_FILE_VERSION_STRINGS = False

try:
    from .local import *
except ImportError:
    pass
