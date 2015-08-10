# Minimum files that are needed to run django test suite

SECRET_KEY = 'WE DONT CARE ABOUT IT'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'django_th.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'TEST_NAME': 'test_django_th.db',
    }
}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django_th',
    'test',
    )

# not python 3 compliant
TH_READABILITY = {
    # get your credential by subscribing to
    #https://www.readability.com/settings/account
    'consumer_key': '<your readability key>',
    'consumer_secret': '<your readability secret>',
}