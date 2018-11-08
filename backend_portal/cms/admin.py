from django.contrib import admin
from .models import Homepage, About, AreaBigCategory, SpecificArea, Opportunity

admin.site.site_header = 'Admin - Portal da InfoBio'
admin.site.site_title = 'Site de Administração do Portal da InfoBio'

admin.site.register(Homepage)
admin.site.register(About)
admin.site.register(AreaBigCategory)
admin.site.register(SpecificArea)
admin.site.register(Opportunity)