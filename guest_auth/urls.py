from django.urls import path
from .views import login_view, register_view

app_name = 'guest_login'

urlpatterns = [
    path('', login_view, name='guest_login'),
    path('register/', register_view, name='guest_register'),

]