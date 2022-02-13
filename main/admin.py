from django.contrib import admin
from .models import Article

admin.site.site_header = "Администрационная панель"

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name','date')

# Register your models here.
admin.site.register(Article, ArticleAdmin)
