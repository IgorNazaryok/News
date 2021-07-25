from django.contrib import admin

from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'createdAt', 'updateAt', 'isPublished')
    list_display_links = ('title',)
    list_editable = ('isPublished',)
    list_filter = ('isPublished', 'category')
    search_fields = ('title', 'content')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
