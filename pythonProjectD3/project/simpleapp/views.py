from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Product, Category
from .filters import ProductFilter
from datetime import datetime
from .forms import ProductForm


class ProductsList(ListView):
    model = Product  # указываем модель, объекты которой мы будем выводить
    template_name = 'products.html'  # указываем имя шаблона, в котором будет лежать HTML,
    context_object_name = 'products'  # это имя списка,
    # queryset = Product.objects.order_by('-id')
    ordering = ['-price']
    paginate_by = 1
    # form_class = ProductForm

    # def get_filter(self):
    #     return ProductFilter(self.request.GET, queryset=super().get_queryset())
    #
    # def get_queryset(self):
    #     return self.get_filter().qs
    #
    # def get_context_data(self, *args, **kwargs):
    #     return {
    #         **super().get_context_data(*args, **kwargs),
    #         "filter": self.get_filter(),
    #         'form': ProductForm
     #   }

    # метод get_context_data нужен нам для того, чтобы мы могли передать переменные в шаблон. В возвращаемом словаре context будут храниться все переменные. Ключи этого словаря и есть переменные, к которым мы сможем потом обратиться через шаблон
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
        context['value1'] = None  # добавим ещё одну пустую переменную

        # context['categories'] = Category.objects.all()
        # context['form'] = ProductForm()
        return context

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST-запроса
    #
    #     if form.is_valid():  # если пользователь ввёл всё правильно и нигде не ошибся, то сохраняем новый товар
    #         form.save()
    #
    #     return super().get(request, *args, **kwargs)


class ProductDetailView(DetailView):
    template_name = 'product_detail.html'
    queryset = Product.objects.all()


class ProductCreateView(CreateView):
    template_name = 'product_create.html'
    form_class = ProductForm


# дженерик для редактирования объекта
class ProductUpdateView(UpdateView):
    template_name = 'product_create.html'
    form_class = ProductForm

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Product.objects.get(pk=id)


# дженерик для удаления товара
class ProductDeleteView(DeleteView):
    template_name = 'product_delete.html'
    queryset = Product.objects.all()
    success_url = '/products/'
