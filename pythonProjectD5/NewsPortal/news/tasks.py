from celery import shared_task

from .views import news_mail


@shared_task
def send_mail_for():
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    news_mail()

