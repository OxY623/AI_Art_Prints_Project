from django.urls import path

from .views import (
    print_list_view,
    print_lookup_view,
    print_search_view,
    print_detail_full,
    edit_print_superuser,
)

app_name = 'prints'

urlpatterns = [
    path('', print_list_view, name='prints-list'),
    path('?page=<int:page_number>', print_list_view, name='prints-list'),
    path('<int:my_id>/', print_lookup_view, name='prints-detail'),
    path('prints_search/', print_search_view, name='prints_search'),
    path('<int:my_id>/', print_lookup_view, name='prints-detail'),
    path('full/<int:my_pk>/', print_detail_full, name='prints-detail-full'),
    path('superuser/create', edit_print_superuser, name='prints-edit'),
    path('new/', edit_print_superuser, name='print_create'),
]
