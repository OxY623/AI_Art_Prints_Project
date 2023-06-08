from django.urls import path
from .views import confirm_purchase

app_name = 'purchase'

urlpatterns = [
    # path('', confirm_purchase, name='confirm_purchase'),
    path('', confirm_purchase, name='purchase'),

]