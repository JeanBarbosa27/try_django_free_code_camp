#TODO: Create url routing for products with namaspacing

from django.urls import path
from .views import products_list_view, product_detail_view, create_product_raw_form_view


urlpatterns = [
    path('', products_list_view, name='products_list'),
    path('<int:product_id>/', product_detail_view, name='product_detail'),
    path('add/', create_product_raw_form_view, name='create_product_raw_form'),
]
