from django_filters import FilterSet  # импортируем filterset, чем-то напоминающий знакомые дженерики
from .models import Post


class PostFilter(FilterSet):

    class Meta:
        model = Post
        fields = ('author', 'categoryType', 'title', 'text', 'rating')
