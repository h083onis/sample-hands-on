from .base import *

DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'app',
        'USER': 'admin',
        'PASSWORD': 'admin',
        'HOST': 'host.docker.internal',
        'PORT': 53306,
        'ATOMIC_REQUESTS': True
    }
}