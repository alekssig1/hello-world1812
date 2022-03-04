from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.paginator import Paginator
from .models import Post, Category
from .filters import PostFilter
from .forms import PostForm

from django.utils import timezone
from datetime import datetime, timedelta

from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

import random
import time


class PostList(ListView):

    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'news.html'
    context_object_name = 'news'

    ordering = ['-dateCreation']
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())

        return context


class SearchList(ListView):

    model = Post
    template_name = 'news_search.html'
    context_object_name = 'news'
    ordering = ['-dateCreation']
    paginate_by = 2

    def get_filter(self):
        return PostFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *args, **kwargs):
        return {
            **super().get_context_data(*args, **kwargs),
            "filter": self.get_filter(),
            }


class PostDetail(DetailView):
    model = Post          # новость полностью
    template_name = 'new.html'
    context_object_name = 'news'
    success_url = '/news/'


class PostCreateView(CreateView):        # создание
    template_name = 'news_create.html'
    form_class = PostForm
    success_url = '/news/'


class PostUpdateView(UpdateView):         # редактирование
    template_name = 'news_update.html'
    form_class = PostForm
    success_url = '/news/'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDeleteView(DeleteView):           # удалениe
    template_name = 'news_delete.html'
    context_object_name = 'new'
    queryset = Post.objects.all()
    success_url = '/news/'


class AddNews(PermissionRequiredMixin, PostCreateView):           # доступ
    permission_required = ('news.add_post',)


class ChangeNews(PermissionRequiredMixin, PostUpdateView):
    permission_required = ('news.change_post',)


class DeleteNews(PermissionRequiredMixin, PostDeleteView):
    permission_required = ('news.delete_post',)


@login_required
def subscribe_me(request, pk):                             # подписка, Отписка

    user = request.user

    my_category = Category.objects.get(id=pk)

    sub_user = User.objects.get(id=user.pk)

    if my_category.subscribers.filter(id=user.pk):
        my_category.subscribers.remove(sub_user)

        return redirect('/news/')
    else:
        my_category.subscribers.add(sub_user)

        return redirect('/news/')


def news_mail():                                               # Celery, apscheduler

    now = datetime.now(tz=timezone.utc)
    for category in Category.objects.all():
        print(Category.objects.all())

        print('----------------------------', category)

        week_news = Post.objects.filter(dateCreation__range=[now - timedelta(days=14), now], postCategory=category)

        for subscriber in category.subscribers.all():

            if subscriber.email:

                url = ''
                delta_sec = 7
                for week_new in week_news:

                    url += f'http://127.0.0.1:8000/news/{week_new.id}, '

                    print(subscriber, '_______________', subscriber.email, url)

                delta_sec += random.randint(10, 20)                                 # чтобы не приняли за спам
                subject = f'News in the week!'
                message = f'{subscriber.username} Новости в категории {category} за неделю: {url}'
                time.sleep(delta_sec)                                               # тормозим отправку на разное время
                send_mail(
                    subject=subject,
                    message=message,
                    from_email=None,
                    recipient_list=[subscriber.email],

                 )






#name1 = Post.objects.get(title='Путин поручил Медведеву новую работу в Совбезе')
#print(name1)
# category_new = Post.objects.get(id='17').postCategory.all()[0]
#
#
# print(category_new)
#
# a = Post.objects.filter(postCategory__name='Спорт')
# print(a)
# for i in a:
#     print(i.author, '_____________________', i.title)


    # doc = Post.objects.get(pk=1)
    # p = doc.postCategory.all()
    # print(p)

    # queryset11 = Category.objects.filter(subscribers=1).values()
    # for i in queryset11:
    #     print(i)

    # category = Category.objects.all()
    # # # print(queryset11)
    # print(category)
    #success_url = '/news/'

    # qs = Post.objects.all()
    # # print(qs.title)
    # for i in qs:
    #     print(i)
    #
    # qs = Post.objects.all().filter(postCategory__id='1')
    # for i in qs:
    #     print(i.title)
    # # print(qs.title)
# doc = Post.objects.get(pk=1)
    # p = doc.postCategory.all()
    # print(p)