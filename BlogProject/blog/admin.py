# blog/admin.py
from django.contrib import admin
from .models import Post, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date', 'category')
    list_filter = ('pub_date', 'category')
    search_fields = ('title', 'content')
    inlines = [CommentInline]

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'post', 'created_date')
    list_filter = ('created_date',)
    search_fields = ('author_name', 'content')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)