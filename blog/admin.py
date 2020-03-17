from django.contrib import admin
from.models import Category, Post
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_field = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_field = ('created', 'updated')
    list_display = ('title', 'author', 'published', 'post_categories') # columnas de datos que quiero que salgan 
    ordering = ('author', 'published') #ordenamiento
    search_fields = ('title', 'content', 'author__username' , 'categories__name') #busqueda
    date_hierarchy = 'published'     #fechas
    list_filter = ('author__username', 'categories__name')

    def post_categories(self, obj):
        return ",".join(c.name for c in obj.categories.all().order_by("name"))
    
    post_categories.short_description = "Categorias"  #cambio el nombre de la columna


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

