from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404

from .models import Product
from .forms import ProductRawForm, ProductModelForm


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

# Handling wiht raw form
def create_product_raw_form_view(request):
    '''This method is just for illustration prupose'''

    form = ProductRawForm()

    if request.method == 'POST':
        form = ProductRawForm(request.POST)
        if form.is_valid():
            Product.objects.create(**form.cleaned_data)
            return redirect('products:products_list')


    context = {'form': form, 'page_title': 'Create product with raw form' }

    return render(request, 'product_form.html', context)


def update_product_raw_form_view(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return redirect('products:products_list')

    initial_data = {
        'title': product.title,
        'description': product.description,
        'price': product.price,
        'summary': product.summary,
        'featured': product.featured
    }

    form = ProductRawForm(initial=initial_data)

    if request.method == 'POST':
        form = ProductRawForm(request.POST)
        is_featured = True if request.POST.get('featured') else False

        if form.is_valid():
            product.title = request.POST['title']
            product.description = request.POST['description']
            product.price = request.POST['price']
            product.summary = request.POST['summary']
            product.featured = is_featured
            product.save()

            return redirect('products:product_detail', product.id)

    context = {
        'form': form,
        'page_title': f"Edit product {product.title}"
    }

    return render(request, 'product_form.html', context)

def product_delete_view(request, product_id):
    product = Product.objects.get(pk=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('products:products_list')

    context = {'product': product}

    return render(request, 'product_delete.html', context)

# Handling with model form
def create_product_model_form_view(request):
    form = ProductModelForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('products:products_list')

    context = { 'form': form, 'page_title': 'Create product with model form' }

    return render(request, 'product_form.html', context)

def update_product_model_form_view(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404

    form = ProductModelForm(request.POST or None, instance=product)

    if form.is_valid():
        form.save()
        return redirect('products:product_detail', product.id)

    context = {'form': form, 'page_title': f"Edit {product}"}

    return render(request, 'product_form.html', context)
