from django.shortcuts import render, get_object_or_404

from .models import Product
from .forms import ProductRawForm

# Create your views here.
#TODO: Create methods to handle forms and CRUD. Remember to use django reverse method to refeer into get_absolute_url method (must be created to). Views will use templates from app folder
def products_list_view(request):
    products = Product.objects.all()
    context = {
        'products': products
    }

    return render(request, 'products_list.html', context)

def product_detail_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    context = {
        'product': product
    }

    return render(request, 'product_detail.html', context)

def create_product_raw_form_view(request):
    '''This method is just for illustration prupose'''

    form = ProductRawForm(request.POST or None)
    context = {
        'form': form
    }
    return render(request, 'create_product.html', context)

