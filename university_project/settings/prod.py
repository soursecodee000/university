from .common import *
import os
import dj_database_url

SECRET_KEY=os.environ['SECRET_KEY']

DEBUG = False


ALLOWED_HOSTS = ['uet-prod-43c9f78ba7bd.herokuapp.com']

DATABASES = {
    'default':dj_database_url.config()
}