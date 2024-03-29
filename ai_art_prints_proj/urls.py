"""
URL configuration for ai_art_prints_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from prints.admin import admin_site
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from pages.views import (
     homeView,
     aboutView,
     contactView,
)

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('purchase/', include('purchase.urls')),
    path('guest/', include('guest_auth.urls')),
    path('cart/', include('cart.urls')),
    path('prints/', include('prints.urls')),
    path('news', include('news.urls')),
    path('admin/', admin_site.urls),
    path('', homeView, name='home'),
    path('about/', aboutView, name='about'),
    path('contact/', contactView, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
