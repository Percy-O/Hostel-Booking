from .common import *



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--&kl$l^&94cv_hy@-ddx)rvk(13j+%)zm2_^^2otirj^_(v(r('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
