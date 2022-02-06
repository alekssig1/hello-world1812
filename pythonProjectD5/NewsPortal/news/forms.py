from django.forms import ModelForm, MultipleChoiceField
from django.db import models
from .models import Post, Category
from django_filters import ModelChoiceFilter


# Создаём модельную форму
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'title', 'postCategory', 'text',)
