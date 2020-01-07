from django.shortcuts import render

from providers.models import Provider


def list_providers(request):
    providers = Provider.objects.all()
    return render(request, 'list_providers.html', {'providers': providers})


def new_providers(request):
    pass


def update_providers(request):
    pass


def delete_providers(request):
    pass
