
from django.contrib import admin
from django.utils.html import format_html

from main.models import *


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Content)
class ContenttAdmin(admin.ModelAdmin):
    list_display = ('text', 'image', 'article')

class ContentInline(admin.StackedInline):
    model = Content
    extra = 1

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'intro','cover', 'author', 'read_time', 'views', 'important', 'published',  'created_at', 'cover_preview' )
    list_filter = ('category', 'published')
    search_fields = ('title', 'intro')
    inlines = [ContentInline, ]

    def cover_preview(self, obj):
        if obj.cover:
            return format_html(
                '<img src="{}" width="100" height="100" style="object-fit: cover;" />',
                obj.cover.url

            )
        return "No image"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','email', 'text', 'article')
    list_filter = ('article','email')

@admin.register(Moment)
class MomentAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo', 'author',  'published', )

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email', 'phone_number', 'subject', 'message', 'seen',)

@admin.register(Newsletter)
class NewletterAdmin(admin.ModelAdmin):
    list_display = ('email',)





