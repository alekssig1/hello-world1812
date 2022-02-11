from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
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
                #form_class = PostForm

                             #метод get_context_data нужен нам для того, чтобы мы могли передать переменные в шаблон.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
                    #context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now

                    #context['categories'] = Category.objects.all()
                    #context['form'] = PostForm()
        return context


class SearchList(ListView):
    paginate_by = 2
    model = Post

    template_name = 'news_search.html'
    context_object_name = 'news'

    ordering = ['-dateCreation']


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
                    #context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now

        return context


class PostDetail(DetailView):
    template_name = 'new.html'
    context_object_name = 'new'
    queryset = Post.objects.all()


class PostCreateView(CreateView):
    template_name = 'news_create.html'
    form_class = PostForm
    success_url = '/news/'


class PostUpdateView(UpdateView):
    template_name = 'news_update.html'
    form_class = PostForm
    success_url = '/news/'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


# дженерик для удаления товара
class PostDeleteView(DeleteView):
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
