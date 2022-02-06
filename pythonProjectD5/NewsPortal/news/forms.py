from django.forms import ModelForm
from django.db import models
from .models import Post, Category
from django_filters import ModelChoiceFilter


# Создаём модельную форму
class PostForm(ModelForm):

    category = ['Спорт', 'Политика', 'Здоровье', 'Культура']

    postCategory = ModelChoiceFilter('Post', queryset=Post.objects.values("postCategory__name"))

    class Meta:
        model = Post
        fields = ['author', 'title', 'postCategory', 'text', ]
