from django.contrib import admin

from .models import Category, Comment, Genre, Review, Title


class TitleAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "year", "category", "description")
    list_editable = ("name", "year", "description")
    search_fields = ("name", "year", "category", "genre")
    list_filter = ("name", "year", "category", "genre")
    empty_value_display = "-пусто-"


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
        "slug",
    )


class GenreAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
        "slug",
    )


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("pk", "author", "title", "text", "score", "pub_date")
    search_fields = ("author", "title", "score")
    list_filter = ("author", "title", "score")
    empty_value_display = "-пусто-"


class CommentAdmin(admin.ModelAdmin):
    list_display = ("pk", "author", "review", "text", "pub_date")
    search_fields = ("author", "review")
    list_filter = ("author", "review")
    empty_value_display = "-пусто-"


admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
