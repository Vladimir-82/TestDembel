from django.contrib import admin
from django.db.models import Sum

from .models import *


class PostAdmin(admin.ModelAdmin):

    change_list_template = "app/posts_changelist.html"

    save_on_top = True
    # empty_value_display = "-empty-" does not work
    list_display = ["author", "title", "category", "views",]
    list_display_links = ["title", "category"]
    readonly_fields = ["category",]
    search_fields = ['body',]
    search_help_text = 'Введите строку для поиска'


    # def get_queryset(self, request):
    #     queryset = super().get_queryset(request)
    #     queryset.views = 0
    #     return queryset


    def make_zero_views(self, obj):
        obj.views = 0
        obj.save()





class CategoryAdmin(admin.ModelAdmin):

    change_list_template = "app/categories_changelist.html"
    save_on_top = True
    list_display = ["title", "views_count"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(sum_views=Sum('post__views'))
        return queryset

    def views_count(self, obj):
        return obj.sum_views

    views_count.short_description = 'Суммарное колличество просмотров'




admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = "Vladimir" #название страницы в браузере
admin.site.site_header = "Vladimir" #заголовок
