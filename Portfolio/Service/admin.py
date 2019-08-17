from django.contrib import admin
from Service.models import ServiceRequest, File


# Register your models here.

class FileInline(admin.TabularInline):
    model = File

    readonly_fields = [
        'file', 'service'
    ]


class ServiceRequestAdmin(admin.ModelAdmin):
    inlines = [
        FileInline
    ]


admin.site.register(ServiceRequest, ServiceRequestAdmin)
admin.site.register(File)
