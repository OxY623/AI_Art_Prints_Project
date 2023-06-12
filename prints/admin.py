from django.contrib.admin import AdminSite
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
    list_display = ('title',  'artist','price')
    list_filter = ('title','price')


class CartAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('user', 'created_at', 'updated_at')

class CartPrintAdmin(admin.ModelAdmin):
    list_display = ('cart', 'print', 'quantity')

class UserProfileAdmin(admin.ModelAdmin):

    list_display = ('user', 'country', 'city')
    list_filter = ('user', 'city')


admin_site = AIArtPrintsAdmin(name='ai_art_prints')
# Register your models here.
admin_site.register(Print, PrintAdmin)
admin_site.register(Cart, CartAdmin)
admin_site.register(CartPrint, CartPrintAdmin)
admin_site.register(UserProfile, UserProfileAdmin)

# admin.site.register(Print)
# admin.site.register(Cart)
# admin.site.register(CartPrint)
# admin.site.register(UserProfile)



