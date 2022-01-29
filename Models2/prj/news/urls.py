from django.urls import path
from .views import PostsList, PostDetail, PostDetailView, PostDeleteView, PostCreateView, \
                               SearchList, news_list

urlpatterns = [
    path('', PostsList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
    path('<int:pk>/', PostDetail.as_view(), name='new'),
    path('search', SearchList.as_view()),
    path('news_list', news_list),
    path('create/', PostCreateView.as_view(), name='news_create'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='news_delete'),
    path('products/', PostsList.as_view()),
]
