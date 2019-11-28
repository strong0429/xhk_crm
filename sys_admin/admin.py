from django.contrib import admin

from .models import *

# Register your models here.
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'superior', 'director', 'duty')
    list_editable = ['superior', 'director']

@admin.register(Campus)
class CampusAdmin(admin.ModelAdmin):
    pass

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'department')
