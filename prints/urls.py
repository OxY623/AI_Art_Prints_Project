from django.urls import path

from .views import (
    print_list_view,
    print_lookup_view,
    print_search_view
)

app_name = 'prints'

urlpatterns = [
    path('', print_list_view, name='prints-list'),
    path('<int:my_id>/', print_lookup_view, name='prints-detail'),
    path('prints_search/', print_search_view, name='prints_search'),
    # path('', name_VIEW, name='prints-list'),
    # path('', name_VIEW, name='prints-list'),
    # path('', name_VIEW, name='prints-list'),
]
