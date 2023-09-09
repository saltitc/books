from django.contrib import admin

from store.models import Book, UserBookRelation


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("name", "author_name", "price")
    fields = ("name", "author_name", "price", "owner")
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(UserBookRelation)
class BookAdmin(admin.ModelAdmin):
    list_display = ("user", "book", 'like', "in_bookmarks", 'rate')
    fields = ("user", "book", 'like', "in_bookmarks", 'rate')
    search_fields = ("book",)
    ordering = ("rate",)
