from django.contrib import admin
from .models import Patrika


# Register your models here.
class PatrikaAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


admin.site.register(Patrika, PatrikaAdmin)
