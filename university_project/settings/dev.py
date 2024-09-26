from .common import *


SECRET_KEY = 's3#tej=^qp^iwkfb889@2160&(&#&tr$ryzhx%!2n%!7m0!@d('

DEBUG = True


# if you want to use my_sql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'school_project',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': '1122'
    }
}



## email sending app
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'expressyourthought05@gmail.com'
EMAIL_HOST_PASSWORD = 'thisisbusinessemail'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False