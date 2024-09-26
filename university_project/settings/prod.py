from .common import *
import os
import dj_database_url

SECRET_KEY=os.environ['SECRET_KEY']

DEBUG = False


ALLOWED_HOSTS = ['uet-prod-9bd1d0504011.herokuapp.com']

DATABASES = {
    'default':dj_database_url.config()
}


EMAIL_HOST=os.environ['MAILGUN_SMTP_SERVER']
EMAIL_HOST_USER=os.environ['MAILGUN_SMTP_LOGIN']
EMAIL_HOST_PASSWORD=os.environ['MAILGUN_SMTP_PASSWORD']
EMAIL_PORT=os.environ['MAILGUN_SMTP_PORT']


