from django.contrib import admin

from .models import Owner


# Register your models here.
class OwnerAdmin(admin.ModelAdmin):
    list_display = ['name_hindi', 'img', 'id']


admin.site.register(Owner, OwnerAdmin)
