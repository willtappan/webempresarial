from django.contrib import admin
from.models import Category, Post
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_field = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_field = ('created', 'updated')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

