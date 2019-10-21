from django.db import models

# Create your models here.

# 员工信息表
class Employee(models.Model):
    name = models.CharField('姓名', max_length=16)
    id_num = models.CharField('身份证', max_length=18, unique=True)
    department = models.ForeignKey('Department', models.PROTECT)
    base = models.ForeignKey('Campus', models.PROTECT)
    supervisor = models.ForeignKey('self', models.PROTECT, null=True, blank=True)
    school = models.CharField('毕业学校', max_length=32, null=True, blank=True)
    major = models.CharField('专业', max_length=32, null=True, blank=True)
    degree = models.CharField('学历', max_length=32, null=True, blank=True)
    active = models.BooleanField('状态', default=True)
    entry_date = models.DateField('入职日期')
    comment = models.CharField('备注', max_length=256, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'app_employee'


# 部门信息表
class Department(models.Model):
    name = models.CharField('名称', max_length=32, unique=True)
    superior = models.ForeignKey('self', models.SET_NULL, null=True, blank=True)
    director = models.ForeignKey('Employee', models.SET_NULL, null=True, blank=True, \
        related_name='director')
    duty = models.CharField('职责', max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'app_department'


#校区信息表
class Campus(models.Model):
    name = models.CharField('校名', max_length=64, unique=True)
    addr = models.CharField('地址', max_length=128)
    phone = models.CharField('电话', max_length=256)
    web_site = models.CharField('网址', max_length=256, null=True, blank=True)
    supervisor = models.ForeignKey('Employee', models.SET_NULL, null=True, blank=True)
    comment = models.CharField('备注', max_length=256, null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'app_campus'


# 教室信息表
class Classroom(models.Model):
    name = models.CharField('教室名', max_length=32)
    campus = models.ForeignKey('Campus', models.CASCADE)
    warden = models.ForeignKey('Employee', models.SET_NULL, null=True, blank=True)
    seat = models.SmallIntegerField('座位数量')
    state = models.BooleanField('是否可用', default='True')
    comment = models.CharField('备注', max_length=256)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'app_classroom'

