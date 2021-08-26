from django.urls import path
from .views import ProductList, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView,\
                   user_list, product_list, comment_list
from django.conf.urls import url

urlpatterns = [
    path('', ProductList.as_view()),
    url(r'^user_list$', user_list),
    path('product_list', product_list),
    path('comment_list', comment_list),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('create/<int:pk>', ProductUpdateView.as_view(), name='product_create'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('products/', ProductList.as_view()),
]
