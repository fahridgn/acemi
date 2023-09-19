from django.contrib import admin
from .models import Motto, Comment

class CommentInline(admin.TabularInline):
    model=Comment

class ArticleAdmin(admin.ModelAdmin):
    inlines=[
        CommentInline,
    ]

admin.site.register(Motto, ArticleAdmin)

admin.site.register(Comment)