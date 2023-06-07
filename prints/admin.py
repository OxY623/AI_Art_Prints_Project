from django.contrib.admin import AdminSite
from .models import Print

class AIArtPrintsAdmin(AdminSite):
    title_header = 'AI Art Prints Admin'
    site_header = 'AI Art Prints Administrotion'
    index_title = 'AI Art Prints site admin'
    logout_template = 'logged_out.html'

admin_site = AIArtPrintsAdmin(name='ai_art_prints')
# Register your models here.
admin_site.register(Print)
