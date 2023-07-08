from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    save_on_top = True
    # empty_value_display = "-empty-" does not work
    list_display = ["title", "category"]
    readonly_fields = ["category",]


admin.site.register(Post, PostAdmin)
admin.site.register(Category)

