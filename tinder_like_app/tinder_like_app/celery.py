import os

from celery import Celery
from celery.shedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tinder_like_app.settings')

app = Celery('tinder_like_app')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


app.conf.beat_schedule = {
    'updating-subscribe': {
        'task': 'subscribe.tasks.update_subsribe_swipes',
        'shedule': crontab(minute=0, hour=0),
    },
}
