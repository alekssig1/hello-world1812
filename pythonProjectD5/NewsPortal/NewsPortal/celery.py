import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsPortal.settings')

app = Celery('NewsPortal')
app.config_from_object('django.conf:settings', namespace='CELERY')
# app.conf.broker_url = 'redis://localhost:15160//'
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send_mail_every_monday_8am': {
        'task': 'news.tasks.send_mail_for',

        # 'schedule': crontab(minute='*/30'),       проверкаб раз в 30 минут

        'schedule': crontab(hour=8, minute=0, day_of_week='monday'),
    },
}
