from django.shortcuts import render, redirect, get_object_or_404

from providers.forms import ProviderForm
from providers.models import Provider


def list_providers(request):
    providers = Provider.objects.all()
    return render(request, 'list_providers.html', {'providers': providers})


def new_providers(request):
    form = ProviderForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_providers')
    return render(
        request, 
        'generic_form.html', 
        {
            'form': form, 
            'title': 'Criar Provedor',
            'roth': 'http://localhost:8000/providers/list/',
        }
    )


def update_providers(request, id):
    provider = get_object_or_404(Provider, pk=id)
    form = ProviderForm(request.POST or None, instance=provider)
    if form.is_valid():
        form.save()
        return redirect('list_providers')
    return render(
        request, 
        'generic_form.html',{
            'form': form, 
            'title': f'Editar {provider.name}',
            'roth': 'http://localhost:8000/providers/list/',
        }
    )


def delete_providers(request, id):
    provider = get_object_or_404(Provider, pk=id)
    provider.delete()
    return redirect('list_providers')
