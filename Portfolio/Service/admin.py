from django.contrib import admin
from Service.models import ServiceRequest, File, Service


# Register your models here.

class FileInline(admin.TabularInline):
    model = File

    readonly_fields = [
        'file', 'service'
    ]


class ServiceInline(admin.TabularInline):
    model = Service

    readonly_fields = [
        'service_request', 'service'
    ]


class ServiceRequestAdmin(admin.ModelAdmin):
    inlines = [
        FileInline,
        ServiceInline
    ]


admin.site.register(ServiceRequest, ServiceRequestAdmin)
admin.site.register(File)
