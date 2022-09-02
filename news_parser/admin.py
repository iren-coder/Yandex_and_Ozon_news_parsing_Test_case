from django.contrib import admin

# Register your models here.
from news_parser.models import News

admin.site.site_header = u'Панель администратора'
admin.site.index_title = u'Управляйте новостными данными'

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    fields = ('title', 'content', 'date', 'tag', 'canal')

