from celery import shared_task
from .models import Subscribe


@shared_task
def update_subsribe_swipes():
    for subscribe in Subscribe.objects.all():
        if subscribe.name = 'basic':
            subscribe.swipes = 25.0
        elif subscribe.name = 'vip':
            subscribe.swipes = 100.0
