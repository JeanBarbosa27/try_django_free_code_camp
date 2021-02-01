from django.urls import path
from .views import products_list_view, product_detail_view, create_product_raw_form_view, create_product_model_form_view, update_product_raw_form_view, product_delete_view, update_product_model_form_view

app_name = "products"
urlpatterns = [
    path('', products_list_view, name='index'),
    path('<int:product_id>/', product_detail_view, name='product_detail'),
    path('<int:product_id>/delete', product_delete_view, name='product_delete'),

    # raw form urls
    path('add_with_raw_form/', create_product_raw_form_view, name='create_product_raw_form'),
    path('<int:product_id>/edit_with_raw_form/', update_product_raw_form_view, name='update_product_raw_form'),

    #model form urls
    path('add_with_model_form/', create_product_model_form_view, name='create_product_model_form'),
    path('<int:product_id>/update_product_model_form', update_product_model_form_view, name="update_product_model_form"),
]
