from django.urls import path
from .views import PostList, PostDetail, PostCreateView, PostUpdateView, PostDeleteView, AddNews, ChangeNews, DeleteNews


urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>/', PostDetail.as_view(), name='news_detail'),
    # path('create/', PostCreateView.as_view(), name='news_create'),
    # path('create/<int:pk>', PostUpdateView.as_view(), name='news_create'),
    # path('delete/<int:pk>', PostDeleteView.as_view(), name='news_delete'),

    path('create/', AddNews.as_view(), name='news_create'),
    path('create/<int:pk>', ChangeNews.as_view(), name='news_create'),
    path('delete/<int:pk>', DeleteNews.as_view(), name='news_delete'),


]

