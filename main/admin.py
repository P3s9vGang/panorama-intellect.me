from django.contrib import admin
from .models import Article, OfferedArticle

admin.site.site_header = "Администрационная панель"

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name','date')

class OffArticleAdmin(admin.ModelAdmin):
    list_display = ('name','date','is_accepted')
    list_editable = ('is_accepted',)

# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(OfferedArticle, OffArticleAdmin)
