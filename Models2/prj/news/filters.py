from django_filters import FilterSet, CharFilter, ModelChoiceFilter, DateFromToRangeFilter
from .models import Post, Author
from django.contrib.auth.models import User


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'categoryType': ['icontains'],
            'title': ['icontains'],
            'rating': ['gte'],

                  }


class F(FilterSet):
    username = CharFilter(method='my_filter')

    class Meta:
        model = User
        fields = ['username']

    def my_filter(self, queryset, name, value):
        return queryset.filter(**{
            name: value,
        })


class C(FilterSet):
    category = ModelChoiceFilter(queryset=Post.objects.all())

    class Meta:
        model = Post
        fields = ['categoryType']


class X(FilterSet):
    date = DateFromToRangeFilter()

    class Meta:
        model = Post
        fields = ['date']
