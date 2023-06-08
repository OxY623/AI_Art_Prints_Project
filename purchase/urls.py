from django.urls import path
from .views import confirm_purchase, thank_you

app_name = 'purchase'

urlpatterns = [
    path('thanks', thank_you, name='confirm_purchase'),
    path('', confirm_purchase, name='purchase'),

]