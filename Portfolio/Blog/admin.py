from django.contrib import admin

# Register your models here.
from Blog.models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_filter = [
        'tag',
        'date'
    ]


admin.site.register(Blog, BlogAdmin)
