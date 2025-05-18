from django.contrib import admin

from .models import Seva


# Register your models here.
class SevaAdmin(admin.ModelAdmin):
    list_display = ['name_hindi', 'img', 'id']


admin.site.register(Seva, SevaAdmin)
