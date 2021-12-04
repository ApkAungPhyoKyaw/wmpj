from django.contrib import admin

# Register your models here.
from .models import Clinic
#admin.site.register(Clinic)
class ClinicAdmin(admin.ModelAdmin):
    list_display = ['patient_name','patient_phone','patient_address','patient_case','drug','fees','datetime','doctor']
    list_filter = ['patient_name','patient_phone','patient_address','patient_case','datetime']
    search_fields = ['patient_name']
admin.site.register(Clinic, ClinicAdmin)
