from django.contrib import admin
from .models import Article, OfferedArticle
from django.utils.safestring import mark_safe

admin.site.site_header = "Администрационная панель"

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name','htmlimage','date')

    def htmlimage(self, object):
        return mark_safe(f'<img src = "{object.image}" style = "height: 50px;">')

class OffArticleAdmin(admin.ModelAdmin):
    list_display = ('name','date','htmlimage','is_accepted')
    list_editable = ('is_accepted',)

    def htmlimage(self, object):
        return mark_safe(f'<img src = "{object.image}" style = "height: 50px;">')

# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(OfferedArticle, OffArticleAdmin)
