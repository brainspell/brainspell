# -*- coding: utf-8 -*-

from django.contrib import admin
from models import *


class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('is_active',)
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(News, ContentAdmin)
admin.site.register(Page, ContentAdmin)
