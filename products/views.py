from django.shortcuts import render
from products.models import Product


def list_products(request):
    products = Product.objects.all()
    return render(request, 'list_products.html', {'products': products})


def new_products(request):
    pass


def update_products(request):
    pass


def delete_products(request):
    pass
