from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Departments)
class DepartmentsAdmin(admin.ModelAdmin):
    pass

@admin.register(Campus)
class CampusAdmin(admin.ModelAdmin):
    pass
