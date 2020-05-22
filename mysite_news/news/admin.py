from django.contrib import admin

from . import models

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('headline', 'pub_date', 'reporter')
    list_filter = ['pub_date']
    search_fields = ['headline']

admin.site.register(models.Article, ArticleAdmin)
