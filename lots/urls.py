from django.urls import path

from lots.views import delete_lots, update_lots, new_lots, list_mov

urlpatterns = [
    path('mov/list/', list_mov, name='list_mov'),
    path('input/new/', new_lots, name='new_lots'),
    path('input/update/', update_lots, name='update_lots'),
    path('input/delete/', delete_lots, name='delete_lots'),
]