from django.contrib import admin
# from .models import Departments, Campus

# Register your models here.
'''
@admin.register(Departments)
class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ('code_dep', 'name_dep', 'supervisor_dep', 'superior_dep', 'duty_dep')
    list_editable = ['name_dep', 'duty_dep']
    list_per_page = 50
    ordering = ('code_dep',)
    # 设置哪些字段点击可以进入编辑界面
    # list_display_links = ('code_dep')

@admin.register(Campus)
class CampusAdmin(admin.ModelAdmin):
    list_display = ('name_cam', 'phone_cam', )
    # list_editable = ('address_cam', 'phone_cam', 'supervisor_cam', 'comment_cam')
    list_per_page = 50
'''