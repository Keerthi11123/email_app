# celery_config.py
from celery import Celery

celery = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

celery.conf.enable_utc = True
celery.conf.timezone = 'UTC'
