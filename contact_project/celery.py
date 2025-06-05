# import os
# from celery import Celery
# os.environ.setdefault('DJANGO_SETTINGS_MODULE','contact_project.settings')  
# app=Celery('contact_project')
# app.config_from_object('django.conf:settings',namespace='CELERY')
# app.autodiscover_tasks()



import os
import ssl
from celery import Celery

# Set default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'contact_project.settings')

# Create Celery app
app = Celery('contact_project')

# Load configuration from Django settings with CELERY_ prefix
app.config_from_object('django.conf:settings', namespace='CELERY')

# Handle rediss:// (SSL connection) configuration for Redis
redis_url = os.environ.get("REDIS_URL", "")
if redis_url.startswith("rediss://"):
    ssl_options = {"ssl_cert_reqs": ssl.CERT_NONE}  # For dev, change to CERT_REQUIRED in production
    app.conf.broker_transport_options = {"ssl": ssl_options}
    app.conf.redis_backend_transport_options = {"ssl_cert_reqs": ssl.CERT_NONE}

# Auto-discover tasks in all registered apps
app.autodiscover_tasks()

