# import os
# from celery import Celery
# os.environ.setdefault('DJANGO_SETTINGS_MODULE','contact_project.settings')  
# app=Celery('contact_project')
# app.config_from_object('django.conf:settings',namespace='CELERY')
# app.autodiscover_tasks()



import ssl
from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')

app = Celery('your_project')
app.config_from_object('django.conf:settings', namespace='CELERY')

redis_url = os.environ.get('REDIS_URL', '')
if redis_url.startswith("rediss://"):
    ssl_options = {"ssl_cert_reqs": ssl.CERT_NONE}
    app.conf.broker_transport_options = {"ssl": ssl_options}
    app.conf.redis_backend_transport_options = {"ssl_cert_reqs": ssl.CERT_NONE}

app.autodiscover_tasks()

