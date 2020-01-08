from django.urls import path

from providers.views import list_providers, new_providers, update_providers, delete_providers

urlpatterns = [
    path('list/', list_providers, name='list_providers'),
    path('new/', new_providers, name='new_providers'),
    path('update/<int:id>/', update_providers, name='update_providers'),
    path('delete/<int:id>/', delete_providers, name='delete_providers'),
]
