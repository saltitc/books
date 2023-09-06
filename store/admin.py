from django.contrib import admin

from store.models import Book


@admin.register(Book)
class PostAdmin(admin.ModelAdmin):
    list_display = ("name", "price")
    fields = ("name", "price")
    search_fields = ("name",)
    ordering = ("name",)