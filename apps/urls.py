from django.contrib import admin
from django.urls import path

from apps.views import Register, Login, ProfileFormView, ProductListView, Product_updateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', Register.as_view(template_engine='apps/register.html'), name='register'),
    path('login/', Login.as_view(template_name='apps/login.html'), name='login'),
    path('profile/', ProfileFormView.as_view(template_name='apps/profile.html'), name='profile'),
    path('products/', ProductListView.as_view(template_name='apps/products.html'), name='products' ),
    path('product-update',Product_updateView.as_view(template_name='apps/product-update.html'),name='product_update' )
]
