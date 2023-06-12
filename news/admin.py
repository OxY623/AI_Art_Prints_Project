from django.contrib import admin
from .models import Article
from prints.admin import admin_site

# Register your models here.
# admin.site.register(Article)
admin_site.register(Article)
