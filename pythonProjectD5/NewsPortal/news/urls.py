from django.urls import path
from .views import PostList, PostDetail, PostCreateView, PostUpdateView, PostDeleteView, AddNews, ChangeNews,\
    DeleteNews, SearchList, subscribe_me
from .signals import send_sub_mail

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>/', PostDetail.as_view(), name='news_detail'),
    path('search/', SearchList.as_view(), name='news_search'),
    # path('create/', PostCreateView.as_view(), name='news_create'),
    # path('create/<int:pk>', PostUpdateView.as_view(), name='news_create'),
    # path('delete/<int:pk>', PostDeleteView.as_view(), name='news_delete'),

    path('create/', AddNews.as_view(), name='news_create'),
    path('update/<int:pk>', ChangeNews.as_view(), name='news_update'),
    path('delete/<int:pk>', DeleteNews.as_view(), name='news_delete'),

    path('subscribed/<int:pk>', subscribe_me, name='subscribed'),




    #path('mmm', PostCreateView.as_view(), name='make_news'),
]

