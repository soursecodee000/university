from .common import *
import os

SECRET_KEY=os.environ['SECRET_KEY']

DEBUG = False


ALLOWED_HOSTS = ['uet-prod-43c9f78ba7bd.herokuapp.com']

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'school_project',
#         'HOST': 'localhost',
#         'USER': 'root',
#         'PASSWORD': '1122'
#     }
# }