# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Article, Comment
# Register your models here.

def make_reviewed(ModelAdmin, request, queryset):
    queryset.update(is_reviewed=True)
make_reviewed.short_description = "تغيير حالة المراجعة"

class ArticleAdmin(admin.ModelAdmin):
    list_display =  ['title', 'author', 'pub_date', 'is_reviewed']
    list_filter = ['author', 'is_reviewed']
    search_fields = ['title', 'author', 'body']
    actions = [make_reviewed]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
