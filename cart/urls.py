from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('cart/', views.cart_view, name='cart'),
    path('add_to_cart/<int:print_id>/<int:quantity>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:cart_print_id>/', views.remove_from_cart, name='remove_from_cart'),
]