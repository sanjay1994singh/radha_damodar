from django.contrib import admin

from .models import BankDetail


# Register your models here.
class BankDetailAdmin(admin.ModelAdmin):
    list_display = ['account_name', 'bank_name', 'account_number', 'ifsc_code']


admin.site.register(BankDetail, BankDetailAdmin)
