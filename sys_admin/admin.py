from django.contrib import admin

from .models import *

# Register your models here.
@admin.register(Department)
class DepartmentAdimn(admin.ModelAdmin):
    list_display = ('name', 'superior', 'director', 'duty')
    list_editable = ['superior', 'director']