from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Article
from prints.admin import admin_site


class ArticleAdmin(admin.ModelAdmin):

    list_display = ('title', 'author')
    list_filter = ('title', 'author')
# Register your models here.
# admin.site.register(Article)
admin_site.register(Article, ArticleAdmin)
