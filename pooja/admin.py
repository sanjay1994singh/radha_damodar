from django.contrib import admin

from .models import Pooja, PoojaCategory


# Register your models here.
class PoojaCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']


class PoojaAdmin(admin.ModelAdmin):
    list_display = ['name_hindi', 'category', 'img', 'id']


admin.site.register(PoojaCategory, PoojaCategoryAdmin)
admin.site.register(Pooja, PoojaAdmin)
