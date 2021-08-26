from django.contrib import admin
from .models import PostCategory, Post, Author

admin.site.register(PostCategory)
admin.site.register(Post)
admin.site.register(Author)
