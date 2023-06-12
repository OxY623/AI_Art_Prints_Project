from django.urls import path
from .views import confirm_purchase, thank_you

app_name = 'purchase'

urlpatterns = [
    path('thank-you/', thank_you, name='thank_you'),
    path('', confirm_purchase, name='purchase'),

]