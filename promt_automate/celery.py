# celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'promt_automate.settings')

# Create a Celery instance and configure it using the settings from Django.
app = Celery('promt_automate')
app.config_from_object('django.conf:settings', namespace='CELERY')

# app.conf.beat_schedule = {
#     'task_orm': {
#         'task': 'automate.tasks.my_background_task',
#          'schedule': crontab(minute='*'),  # Adjust the crontab parameters as needed
#     }
# }
app.conf.update(
    result_backend='django-db',
)

# Auto-discover tasks in all registered Django app configs.
app.autodiscover_tasks()
