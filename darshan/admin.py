from django.contrib import admin

from .models import DailyDarshan


# Register your models here.
class DailyDarshanAdmin(admin.ModelAdmin):
    list_display = ['title', 'img', 'id']


admin.site.register(DailyDarshan, DailyDarshanAdmin)
