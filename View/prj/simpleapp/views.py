from django.views.generic import ListView, DetailView      # импортируем класс, который говорит нам о том,
from .models import Product, Category                    # что в этом представлении мы будем выводить список объектов из БД
from datetime import datetime

class ProductsList(ListView):
    model = Product                     # указываем модель, объекты которой мы будем выводить
    template_name = 'products.html'      # указываем имя шаблона, в котором будет лежать HTML,
    context_object_name = 'products'
    queryset = Product.objects.order_by('-id')                                    # это имя списка, в котором будут лежать все объекты,

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
        context['value1'] = None                # добавим ещё одну пустую переменную, чтобы на её примере посмотреть работу другого фильтра
        return context
                                                      # его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
                                                      # создаём представление, в котором будут детали конкретного отдельного товара


class ProductDetail(DetailView):
    model = Product  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'product.html'  # название шаблона будет product.html
    context_object_name = 'product'  # название объекта. в нём будет
