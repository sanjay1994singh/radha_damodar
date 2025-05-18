from django.contrib import admin

from service.models import Service


# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name_hindi', 'img', 'id']


admin.site.register(Service, ServiceAdmin)
