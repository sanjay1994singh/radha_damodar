from django.contrib import admin

from .models import God


# Register your models here.
class GodAdmin(admin.ModelAdmin):
    list_display = ['name_hindi', 'img', 'id']


admin.site.register(God, GodAdmin)
