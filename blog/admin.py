from .models import Post, Category
from django.contrib import admin

# Register your models here.

admin.site.register(Category)

@admin.register(Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("title", "id", "status", "slug", "author")
    prepopulated_fields = {"slug": ("title",)}