from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver

from .models import Post, PostCategory, Category
from .views import subscribe_me
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


@receiver(m2m_changed, sender=PostCategory)
def send_sub_mail(sender, instance, action, **kwargs):   # при добавлении новости идет уведомление подписчикам категории

    if action == 'post_add':

        category_new = instance.postCategory.all()[0]
        print(category_new)

        for category in instance.postCategory.all():
            for user in category.subscribers.all():
                t = user.email
                print(t)
                print(user)

                html_content = render_to_string(
                    'mail.html', {'user': user, 'instance': instance})

                msg = EmailMultiAlternatives(
                    subject=f' Новая статья в подписке "{category_new}" ',

                    from_email='alekssig1@yandex.ru',
                    to=[user.email]
                )

                msg.attach_alternative(html_content, 'text/html')
                msg.send()

