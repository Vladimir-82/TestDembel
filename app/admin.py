from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):

    change_list_template = "app/posts_changelist.html"

    save_on_top = True
    # empty_value_display = "-empty-" does not work
    list_display = ["author", "title", "category", "views"]
    list_display_links = ["title", "category"]
    readonly_fields = ["category",]


admin.site.register(Post, PostAdmin)
admin.site.register(Category)

admin.site.site_title = "Vladimir" #название страницы в браузере
admin.site.site_header = "Vladimir" #заголовок
