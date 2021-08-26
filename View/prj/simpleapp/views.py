from django.shortcuts import render
from django.views import View  # импортируем простую вьюшку
from django.core.paginator import Paginator  # импортируем класс, позволяющий удобно осуществлять постраничный вывод

from .models import Product


class ProductList(View):

    def get(self, request):
        products = Product.objects.order_by('-price')
        p = Paginator(products, 1)

        products = p.get_page(request.GET.get('page', 1))

        data = {
            'products': products,
        }
        return render(request, 'products.html', data)
