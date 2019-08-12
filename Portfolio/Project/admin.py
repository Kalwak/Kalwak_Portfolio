from django.contrib import admin
from .models import *


class GalleryInline(admin.TabularInline):
    model = Gallery


class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        GalleryInline
    ]


class LogsAdmin(admin.ModelAdmin):
    readonly_fields = (
        'datetime', 'status_code', 'status_text', 'response',
        'request', 'ipv4_address', 'path', 'is_ajax', 'is_secure'
    )


admin.site.register(Logs, LogsAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectCategory)
