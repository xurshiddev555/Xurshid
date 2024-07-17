from django.db.models import Model
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, ListView, UpdateView

from apps.forms import RegisterForm
from apps.models import Product, Order


# Create your views here.
class Register(FormView):
    login_url = 'login'
    template_name = 'apps/register.html'


class Login(FormView):
    login_url = 'login'
    template_name = 'apps/login.html'

    class Meta:
        template_name = 'Login'
        fields = '__all__'
        db_table = 'login'


class ProfileFormView(FormView):
    form_class = ProfileForm
    template_name = 'apps/profile.html'

    def form_valid(self, form):
        data = form.save(commit=False)
        print(data)

    def form_invalid(self, form):
        data = form.errors
        print(data)


class ProductListView(ListView):
    model = Product
    template_name = "apps/products.html"
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        return Product.objects.all().order_by('name')


class OrderListView(ListView):
    model = Order
    template_name = "apps/orders.html"
    context_object_name = 'orders'
    paginate_by = 10

    def get_queryset(self):
        return Order.objects.all().order_by('name')


