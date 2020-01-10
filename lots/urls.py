from django.urls import path

from lots.views import (delete_input, delete_output, list_input,
                        list_mov, list_output, new_input, new_output,
                        update_input, update_output)

urlpatterns = [
    path('mov/list/', list_mov, name='list_mov'),
    path('input/list/', list_input, name='list_input'),
    path('input/new/', new_input, name='new_input'),
    path('input/update/', update_input, name='update_input'),
    path('input/delete/', delete_input, name='delete_input'),
    path('output/list/', list_output, name='list_output'),
    path('output/new/', new_output, name='new_output'),
    path('output/update/', update_output, name='update_output'),
    path('output/delete/', delete_output, name='delete_output'),
]
