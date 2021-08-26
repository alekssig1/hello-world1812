from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView
from django.core.paginator import Paginator
from .models import Post
from .filters import PostFilter, F, C, X



class PostsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 2


class SearchList(ListView):
    model = Post
    template_name = 'news_list.html'
    context_object_name = 'news'
    paginate_by = 1


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
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'


# дженерик для получения деталей о товаре
class PostDetailView(DetailView):
    template_name = 'product_detail.html'
    queryset = Post.objects.all()


def news_list(request):
    c = PostFilter(request.GET, queryset=Post.objects.all())
    return render(request, 'product_t.html', {'filter': c})


# дженерик для удаления товара
class PostDeleteView(DeleteView):
    template_name = 'news_delete.html'
    queryset = Post.objects.all()
    success_url = '/products/'



