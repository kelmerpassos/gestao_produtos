from django.urls import path

from products.views import delete_products, update_products, new_products, list_products

urlpatterns = [
    path('list/', list_products, name='list_products'),
    path('new/', new_products, name='new_products'),
    path('update/<int:id>/', update_products, name='update_products'),
    path('delete/<int:id>/', delete_products, name='delete_products'),
]