from config.settings import *


DEBUG = True
MODE = 'devel'

DATABASES = {
    'default': {
        'NAME': 'marketplace_sneakarc',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}