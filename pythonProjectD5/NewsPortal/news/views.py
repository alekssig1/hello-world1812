from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Post, Category
from .filters import PostFilter
from datetime import datetime
from .forms import PostForm

from django.shortcuts import redirect


from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required


class PostList(ListView):

    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'news.html'  # указываем имя шаблона, в котором будет лежать HTML,
    context_object_name = 'news'  # это имя списка,
    # qeryset = Post.objects.order_by('-id')
    ordering = ['-dateCreation']
    paginate_by = 2
                #form_class = PostForm

                             #метод get_context_data нужен нам для того, чтобы мы могли передать переменные в шаблон.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
                    #context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now

        #context['categories']: Category.objects.all()
                    #context['form'] = PostForm()
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


    # paginate_by = 2
    # model = Post
    #
    # template_name = 'news_search.html'
    # context_object_name = 'news'
    #
    # ordering = ['-dateCreation']
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
    #                 #context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
    #
    #     return context


class PostDetail(DetailView):
    model = Post          # новость полностью
    template_name = 'new.html'
    context_object_name = 'news'
    success_url = '/news/'

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


class AddNews(PermissionRequiredMixin, PostCreateView):
    permission_required = ('news.add_post',)


class ChangeNews(PermissionRequiredMixin, PostUpdateView):
    permission_required = ('news.change_post',)


class DeleteNews(PermissionRequiredMixin, PostDeleteView):
    permission_required = ('news.delete_post',)


@login_required
def subscribe_me(request, pk):
    print(pk)

    user = request.user

    print(user)

    my_category = Category.objects.get(id=pk)

    print(my_category)

    sub_user = User.objects.get(id=user.pk)

    print(sub_user)

    print(my_category.subscribers.filter(id=user.pk))

    id = user.pk
    print(id)

    if my_category.subscribers.filter(id=user.pk):
        my_category.subscribers.remove(sub_user)
        print(my_category.subscribers)
        print(sub_user, id)

        return redirect('/news/')
    else:
        my_category.subscribers.add(sub_user)
        print('Пользователь', request.user, 'добавлен в подписчики категории:', Category.objects.get(pk=pk))
        print(my_category.subscribers)
        print(sub_user)

        return redirect('/news/')


# функция рассылки писем при добавлении новой статьи
# def send_mail_for_sub(instance):
#
#     sub_text = instance.text
#     # получаем нужный объект модели Категория через рк Пост
#     category = Category.objects.get(pk=Post.objects.get(pk=instance.pk).category.pk)
#
#     subscribers = category.subscribers.all()
#
#
#     for qaz in subscribers:
#         print(qaz.email)
#
#
#     for subscriber in subscribers:
#
#         html_content = render_to_string(
#             'mail.html', {'user': subscriber, 'text': sub_text[:50], 'post': instance})
#
#         sub_username = subscriber.username
#         sub_useremail = subscriber.email

        # msg = EmailMultiAlternatives(
        #     subject=f'Здравствуй, {subscriber.username}. Новая статья в вашем разделе!',
        #     from_email='factoryskill@yandex.ru',
        #     to=[subscriber.email]
        # )
        #
        # msg.attach_alternative(html_content, 'text/html')

        # # для удобства вывода инфы в консоль
        # print()
        # print(html_content)
        # print()

        # фукнция для таски, передаем в нее все что нужно для отправки подписчикам письма
        # send_mail_for_sub_once.delay(sub_username, sub_useremail, html_content)

        # код ниже временно заблокирован, чтоб пока в процессе отладки не производилась реальная рассылка писем
        # msg.send()
    #
    # print('Представления - конец')
    #
    # return redirect('/news/')


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
#
# aa = Post.objects.all().values()
# for i in aa:
#     print(i)

