from django.urls import path

from .views import (
    print_list_view,
    print_lookup_view,
    print_search_view,
    print_detail_full,
    edit_print_superuser,
    print_delete_view,
    PrintListViewSuperUser,
    dynamic_lookup_view,
    user_cart_view,
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
    path('superuser/list', PrintListViewSuperUser.as_view(), name='print_list_super'),
    path('superuser/<int:id>/delete/', print_delete_view, name='print_delete_super'),
    path('superuser/<int:id>/', dynamic_lookup_view, name='print-detail_super_user'),
    path('superuser/users/', user_cart_view, name='user_cart_view'),


]
