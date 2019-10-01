from django.db import models

# Create your models here.
# 校区信息表
class Campus(models.Model):
    class Meta:
        db_table = 'campus'

    id_cam = models.AutoField(primary_key=True)         # 校区索引id
    name_cam = models.CharField(max_length=32)          # 校区名字
    address_cam = models.CharField(max_length=64)       # 校区地址
    phone_cam = models.CharField(max_length=16)         # 校区联系电话
    supervisor_cam = models.ForeignKey('Employee')      # 校区负责人
    comment_cam = models.CharField(max_length=256, null=True)   # 备注信息

# 校区教室信息表
class Classroom(models.Model):
    class Meta:
        db_table = 'classroom'

    id_room = models.AutoField(primary_key=True)        # 教室索引id
    name_room = models.CharField(max_length=32)         # 教室名字
    campus_room = models.ForeignKey('Campus')           # 教室所在校区
    warden_room = models.ForeignKey('Employee')         # 教室管理员
    content_room = models.SmallIntegerField()           # 教室的座位容量
    state_room = models.BooleanField()                  # 教室状态：是否可用
    comment_room = models.CharField(max_length=64, null=True)   # 备注信息

# 培训课程信息表


# 职位信息表
class Positions(models.Model):
    code_pos = models.CharField(max_length=8, primary_key=True)
    name_pos = models.CharField(max_length=32, unique=True)
    duty_pos = models.CharField(max_length=64)

    class Meta:
        db_table = 'positions'

# 部门信息表
class Departments(models.Model):
    code_dep = models.CharField(max_length=8, primary_key=True)
    name_dep = models.CharField(max_length=16, unique=True)
    supervisor_dep = models.CharField(max_length=8, null=True)
    superior_dep = models.CharField(max_length=8, null=True)
    duty_dep = models.CharField(max_length=128)

    class Meta:
        db_table = 'departments'

# 员工信息表
class Employee(models.Model):
    name_emp = models.CharField(max_length=32)
    id_num_emp = models.CharField(max_length=18, unique=True)
    tel_num_emp = models.CharField(max_length=12, unique=True)
    supervisor_emp = models.IntegerField()
    entry_date_emp = models.DateField()
    ecp_emp = models.CharField(max_length=16, null=True)
    ecpt_emp = models.CharField(max_length=12, null=True)
    email_emp = models.CharField(max_length=64, null=True)
    wechat_emp = models.CharField(max_length=64, null=True)
    address_emp = models.CharField(max_length=128, null=True)

    position = models.ForeignKey('Positions', on_delete=models.CASCADE)
    department = models.ForeignKey('Departments', on_delete=models.CASCADE)

    class Meta:
        db_table = 'employee'

class Classes(models.Model):
    WEEK_DAY = (
        ('1', '星期一'),
        ('2', '星期二'),
        ('3', '星期三'),
        ('4', '星期四'),
        ('5', '星期五'),
        ('6', '星期六'),
        ('0', '星期日'),
    )

    class Meta:
        db_table = 'classes'

    name_cla = models.CharField(max_length=32)
    # 当两个外键指向同一个表时，需要指定不同的 related_name
    master_cla = models.ForeignKey('Employee', on_delete=models.PROTECT, related_name='master_emp')
    teacher_cla = models.ForeignKey('Employee', on_delete=models.PROTECT, related_name='teacher_emp')

    room_cla = models.CharField(max_length=32)

    start_date_cla = models.DateField()
    week_day_cla = models.CharField(max_length=1, choices=WEEK_DAY)

'''
class Students(models.Model):
    STU_SEX = (
        ('M', '男'),
        ('F', '女')
    )

    name_stu = models.CharField(max_length=32)
    sex_stu = models.CharField(max_length=1, choices=STU_SEX)
    age_stu = models.SmallIntegerField()

'''