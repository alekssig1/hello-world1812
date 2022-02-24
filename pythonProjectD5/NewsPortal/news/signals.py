from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver  # импортируем нужный декоратор
from django.core.mail import mail_admins
from .models import Post, PostCategory, Category
from .views import subscribe_me
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.shortcuts import redirect

@receiver(m2m_changed, sender=PostCategory)
def send_sub_mail(sender, instance, action, **kwargs):

    if action == 'post_add':
        # pk = instance.id
        # print(pk)
        category_new = instance.postCategory.all()[0]
        print(category_new)

        # a = Post.objects.all()
        # for i in a:                     #.filter(postCategory__name=category_new)
        #     print(i)

        for category in instance.postCategory.all():
            for user in category.subscribers.all():
                t = user.email
                print(t)
                print(user)

                html_content = render_to_string(
                    'mail.html', {'user': user, 'instance': instance})

                msg = EmailMultiAlternatives(
                    subject=f' Новая статья в подписке "{category_new}" ',
                    # body=f'http://127.0.0.1:8000/news/{instance.id}, {instance.title[:20]}',
                    from_email='alekssig1@yandex.ru',
                    to=[user.email]
                )

                msg.attach_alternative(html_content, 'text/html')
                msg.send()


                # subject = f'{instance.title}'
                # mail_admins(
                #     subject=subject,
                #     message=instance.text[:50],
                #     to=['user.email']
                # )

        # b = category_new.subscribers.all()
        # print(b)
        #
        # for i in b:
        #
        #
        #
        #     if cc==i.author:
        #         print('kkkkkkkkkkkk')
    # subject = f'{instance.title}'
    # mail_admins(
    #     subject=subject,
    #     message=instance.text[:50],
    #     to=[suser.email]
    # )