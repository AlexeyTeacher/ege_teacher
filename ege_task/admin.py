from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class EgeTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'number_task', 'title', 'time_create', 'get_html_preview_image', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content', 'number_task')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')

    def get_html_preview_image(self, object):
        if object.preview_image:
            return mark_safe(f'<img src="{object.preview_image.url}" width=90>')

    get_html_preview_image.short_description = 'Preview image'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Task, EgeTaskAdmin)
admin.site.register(Category, CategoryAdmin)
