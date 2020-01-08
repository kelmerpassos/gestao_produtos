from django.shortcuts import render, get_object_or_404, redirect

from products.forms import ProductForm
from products.models import Product


def list_products(request):
    products = Product.objects.all()
    return render(request, 'list_products.html', {'products': products})


def new_products(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        redirect('list_products')
    return render(request, 'generic_form.html', {'form': form})


def update_products(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid():
        form.save()
        redirect('list_products')
    return render(request, 'generic_form.html', {'form': form})


def delete_products(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    redirect('list_products')

