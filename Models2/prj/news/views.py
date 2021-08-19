from django.views.generic import ListView, DetailView      # импортируем класс, который говорит нам о том,
from .models import Post
from datetime import datetime


class PostsList(ListView):
    model = Post                   # указываем модель, объекты которой мы будем выводить
    template_name = 'news.html'      # указываем имя шаблона, в котором будет лежать HTML,
    context_object_name = 'news'     # в котором будут все инструкции о том,
    queryset = Post.objects.order_by('-id')  # это имя списка, в котором будут лежать все объекты,

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
        context[
            'value1'] = None
        return context


class PostDetail(DetailView):
    model = Post  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'new.html'  # название шаблона будет new.html
    context_object_name = 'new'
