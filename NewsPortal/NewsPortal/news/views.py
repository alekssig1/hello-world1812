from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Post, Category
from .filters import PostFilter
from datetime import datetime
from .forms import PostForm


class PostList(ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'news.html'  # указываем имя шаблона, в котором будет лежать HTML,
    context_object_name = 'news'  # это имя списка,
    # qeryset = Post.objects.order_by('-id')
    ordering = ['-dateCreation']
    paginate_by = 2
    form_class = PostForm

                             #метод get_context_data нужен нам для того, чтобы мы могли передать переменные в шаблон.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
        # context['value1'] = None  # добавим ещё одну пустую переменную

        # context['categories'] = Category.objects.all()
        # context['form'] = PostForm()
        return context

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST-запроса
    #
    #     if form.is_valid():  # если пользователь ввёл всё правильно и нигде не ошибся, то сохраняем новый товар
    #         form.save()
    #
    #     return super().get(request, *args, **kwargs)


class PostDetail(DetailView):
    template_name = 'new.html'
    context_object_name = 'new'
    queryset = Post.objects.all()


class PostCreateView(CreateView):
    template_name = 'news_create.html'
    form_class = PostForm


# дженерик для редактирования объекта
class PostUpdateView(UpdateView):
    template_name = 'news_create.html'
    form_class = PostForm
    success_url = '/news/'

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


# дженерик для удаления товара
class PostDeleteView(DeleteView):
    template_name = 'news_delete.html'
    context_object_name = 'new'
    queryset = Post.objects.all()
    success_url = '/news/'
