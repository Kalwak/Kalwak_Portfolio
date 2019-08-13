from django.contrib import admin
from Service.models import ServiceRequest, Files


# Register your models here.

class FileInline(admin.TabularInline):
    model = Files

    readonly_fields = [
        'file', 'service'
    ]


class ServiceRequestAdmin(admin.ModelAdmin):
    inlines = [
        FileInline
    ]


admin.site.register(ServiceRequest, ServiceRequestAdmin)
admin.site.register(Files)
