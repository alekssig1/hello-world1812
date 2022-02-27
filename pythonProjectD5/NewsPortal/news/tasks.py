from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from celery.schedules import crontab
from .views import news_mail


@shared_task
def send_mail_for():
    # def news_mail():
    print('___________________')
    # for category in Category.objects.all():
    #     print(category)
    #
    #     week_news = Post.objects.filter(dateCreation__range=[datetime.now(tz=timezone.utc) - timedelta(days=14),
    #                                                          datetime.now(tz=timezone.utc)], postCategory=category)
    #
    #     # news_from_each_category = []
    #
    #     for subscriber in category.subscribers.all().distinct():
    #         print(subscriber.username, '_______________', subscriber.email)
    #         url = ''
    #         for week_new in week_news:
    #             # url += f'{week_new.get_absolute_url}, '
    #             print(week_new.title)
    #
    #             url += (f'http://127.0.0.1:8000/news/{week_new.id}, ')
    #
    #             # news_from_each_category.append(url)
    #             print(url)
    #
    #         send_mail(
    #             subject=f'News in the week!',
    #             message=f'Новости в категории {category} за неделю: {url}',
    #
    #             from_email=None,
    #             recipient_list=[subscriber.email, ]
    #         )

    # news_mail()
#     msg = EmailMultiAlternatives(
#         subject=f'Здравствуй, {sub_username}, новые статьи за прошлую неделю в вашем разделе!',
#         from_email=None,
#         to=[sub_useremail]
#     )
#
#     msg.attach_alternative(html_content, 'text/html')
#
#     msg.send()

