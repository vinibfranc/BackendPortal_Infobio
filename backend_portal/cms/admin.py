from django.contrib import admin
from .models import Section, Category, Content, Post, Comment

admin.site.site_header = 'Admin - Portal da InfoBio'
admin.site.site_title = 'Site de Administração do Portal da InfoBio'

admin.site.register(Section)
admin.site.register(Category)
admin.site.register(Content)

admin.site.register(Post)
admin.site.register(Comment)