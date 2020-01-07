from django.urls import path

from providers.views import list_providers, new_providers, update_providers, delete_providers

urlpatterns = [
    path('list/', list_providers, name='list_providers'),
    path('new/', new_providers, name='new_providers'),
    path('update/', update_providers, name='update_providers'),
    path('delete/', delete_providers, name='delete_providers'),
]
