from django.contrib import admin
from .models import Post, Comment

class CommentAdminRestrictions(admin.ModelAdmin):
    fields = ['post', 'text', 'author', 'creation_date', 'approval']
    readonly_fields = ['creation_date']

admin.site.register(Post)
admin.site.register(Comment, CommentAdminRestrictions)
