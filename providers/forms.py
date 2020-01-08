from django.forms import ModelForm

from providers.models import Provider


class ProviderForm(ModelForm):
    class Meta:
        model = Provider
        fields = ['name', 'cnpj']
