from django.forms import ModelForm
from django.db import models
from .models import Post, Category


# Создаём модельную форму
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'title', 'postCategory', 'text',)
