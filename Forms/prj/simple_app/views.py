from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from django.core.paginator import Paginator
from .models import Product, Comment
from .filters import ProductFilter, F, C, X
from django.contrib.auth.models import User
from .forms import ProductForm


class ProductList(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    ordering = ['-price']
    paginate_by = 1

    def get_filter(self):
        return ProductFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *args, **kwargs):
        return {
            **super().get_context_data(*args, **kwargs),
            "filter": self.get_filter(),
        }


# дженерик для получения деталей о товаре
class ProductDetailView(DetailView):
    template_name = 'product_detail.html'
    queryset = Product.objects.all()


# дженерик для создания объекта.
class ProductCreateView(CreateView):
    template_name = 'product_create.html'
    form_class = ProductForm


# дженерик для редактирования объекта
class ProductUpdateView(UpdateView):
    template_name = 'product_create.html'
    form_class = ProductForm


    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Product.objects.get(pk=id)


# дженерик для удаления товара
class ProductDeleteView(DeleteView):
    template_name = 'product_delete.html'
    queryset = Product.objects.all()
    success_url = '/products/'


def user_list(request):
    f = F(request.GET, queryset=User.objects.all())
    return render(request, 'user_t.html', {'filter': f})


def product_list(request):
    c = C(request.GET, queryset=Product.objects.all())
    return render(request, 'product_t.html', {'filter': c})


def comment_list(request):
    x = X(request.GET, queryset=Comment.objects.all())
    return render(request, 'comment_t.html', {'filter': x})
