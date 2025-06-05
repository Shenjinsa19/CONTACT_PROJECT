# import os
# from celery import Celery
# os.environ.setdefault('DJANGO_SETTINGS_MODULE','contact_project.settings')  
# app=Celery('contact_project')
# app.config_from_object('django.conf:settings',namespace='CELERY')
# app.autodiscover_tasks()

import os
import ssl
from celery import Celery

# Set default settings module for Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'contact_project.settings')

app = Celery('contact_project')

# Use Django settings for Celery config
app.config_from_object('django.conf:settings', namespace='CELERY')

# If using rediss:// (Upstash Redis), apply SSL options
if os.environ.get('REDIS_URL', '').startswith('rediss://'):
    ssl_options = {"ssl_cert_reqs": ssl.CERT_NONE}
    app.conf.broker_transport_options = {'ssl': ssl_options}
    app.conf.redis_backend_transport_options = {'ssl_cert_reqs': ssl.CERT_NONE}

# Discover tasks in installed apps
app.autodiscover_tasks()
