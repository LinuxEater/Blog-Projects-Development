from django.contrib import admin
from .models import Category, Blog

# Register your models here.

admin.site.site_header = "Blog Projects Admin"
admin.site.site_title = "Blog Projects Admin Portal"

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'status', 'is_featured', 'created_at')
    search_fields = ('title', 'short_description', 'blog_body')
    list_filter = ('status', 'category', 'is_featured', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-created_at']  # Order by creation date descending

class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'created_at', 'updated_at')
    search_fields = ('category_name',)
    list_filter = ('created_at', 'updated_at')
    
admin.site.register(Category, BlogCategoryAdmin)
admin.site.register(Blog, BlogAdmin)