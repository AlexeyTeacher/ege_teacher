from django.contrib import admin
from .models import *


class EgeTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'number_task', 'title', 'time_create', 'preview_image', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content', 'number_task')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Task, EgeTaskAdmin)
admin.site.register(Category, CategoryAdmin)
