from django.urls import path

from lots.views import delete_lots, update_lots, new_lots, list_lots

urlpatterns = [
    path('list/', list_lots, name='list_lots'),
    path('input/new/', new_lots, name='new_lots'),
    path('input/update/', update_lots, name='update_lots'),
    path('input/delete/', delete_lots, name='delete_lots'),
]