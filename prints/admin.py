from django.contrib.admin import AdminSite
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Print, Cart, CartPrint, UserProfile
from django.contrib import admin
# код упрощает администраторам просмотр, изменение и
# удаление связанных данных.
class AIArtPrintsAdmin(AdminSite):
    title_header = 'AI Art Prints Admin'
    site_header = 'AI Art Prints Administrotion'
    index_title = 'AI Art Prints site admin'
    logout_template = 'logged_out.html'

class PrintAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('title',  'artist','price', 'quantity')
    list_filter = ('title','price')


class CartAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('user', 'created_at', 'updated_at')

class CartPrintAdmin(admin.ModelAdmin):
    list_display = ('cart', 'print', 'quantity')

class UserProfileAdmin(admin.ModelAdmin):

    list_display = ('user', 'country', 'city')
    list_filter = ('user', 'city')


class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions',)


admin_site = AIArtPrintsAdmin(name='ai_art_prints')

admin_site.register(Print, PrintAdmin)
admin_site.register(Cart, CartAdmin)
admin_site.register(CartPrint, CartPrintAdmin)
admin_site.register(UserProfile, UserProfileAdmin)


# admin.site.register(Print, PrintAdmin)
# admin.site.register(Cart, CartAdmin)
# admin.site.register(CartPrint, CartPrintAdmin)
# admin.site.register(UserProfile, UserProfileAdmin)
