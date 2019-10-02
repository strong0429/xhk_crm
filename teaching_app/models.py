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
    supervisor_cam = models.ForeignKey('Employee', on_delete=models.PROTECT)      # 校区负责人
    comment_cam = models.CharField(max_length=256, null=True)   # 备注信息

# 校区教室信息表
class Classroom(models.Model):
    class Meta:
        db_table = 'classroom'

    id_room = models.AutoField(primary_key=True)        # 教室索引id
    name_room = models.CharField(max_length=32)         # 教室名字
    campus_room = models.ForeignKey('Campus', on_delete=models.CASCADE)           # 教室所在校区
    warden_room = models.ForeignKey('Employee', on_delete=models.PROTECT)         # 教室管理员
    content_room = models.SmallIntegerField()           # 教室的座位容量
    state_room = models.BooleanField()                  # 教室状态：是否可用
    comment_room = models.CharField(max_length=64, null=True)   # 备注信息

# 课程类别信息表
class CourseCategory(models.Model):
    class Meta:
        db_table = 'course_category'

    id_cc = models.AutoField(primary_key=True)      # 索引, 主键
    name_cc = models.CharField(max_length=32)       # 课程名称
    stage_cc = models.CharField(max_length=16)      # 课程所处阶段
    amount_cc = models.SmallIntegerField()          # 该阶段课程数量
    comment_cc = models.CharField(max_length=64, null=True)     # 备注信息

# 课程信息表
class Lessons(models.Model):
    class Meta:
        db_table = 'lessons'
    
    id_les = models.AutoField(primary_key=True)         # 索引，主键
    id_cc_les = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)     # 所属课程类别
    order_les = models.SmallIntegerField()              # 第几课
    name_les = models.CharField(max_length=32)          # 课程名称
    path_les = models.CharField(max_length=256)         # 课件路径
    length_les = models.FloatField()                    # 课时
    version_les = models.CharField(max_length=8, null=True)     # 课件版本
    comment_les = models.CharField(max_length=64, null=True)    # 备注信息

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

# 班级信息表
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

    STATE_CLA = (
        ('1', '未开课'),
        ('2', '开课中'),
        ('3', '已结课'),
    )

    class Meta:
        db_table = 'classes'

    name_cla = models.CharField(max_length=32)
    # 当两个外键指向同一个表时，需要指定不同的 related_name
    master_cla = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name='master_emp')
    teacher_cla = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name='teacher_emp')

    id_room_cla = models.ForeignKey(Classroom, on_delete=models.PROTECT)
    number_stu_cla = models.SmallIntegerField()

    start_date_cla = models.DateField()
    week_day_cla = models.CharField(max_length=1, choices=WEEK_DAY)
    state_cla = models.CharField(max_length=1, choices=STATE_CLA)

# 学生信息表
class Students(models.Model):
    class Meta:
        db_table = 'students'

    STU_SEX = (
        ('M', '男'),
        ('F', '女')
    )

    STU_STATE = (
        ('0', '正常'),
        ('1', '补课'),
        ('2', '请假'),
        ('3', '毕业'),
    )

    id_stu = models.AutoField(primary_key=True)
    name_stu = models.CharField(max_length=32)
    sex_stu = models.CharField(max_length=1, choices=STU_SEX)
    age_stu = models.SmallIntegerField()
    id_cc_stu = models.ForeignKey(CourseCategory, on_delete=models.PROTECT)
    id_cla_stu = models.ForeignKey(Classes, on_delete=models.PROTECT)
    date_entry_stu = models.DateField()
    cur_les_stu = models.ForeignKey(Lessons, on_delete=models.PROTECT)
    state_stu = models.CharField(max_length=1, choices=STU_STATE)

    comment_stu = models.CharField(max_length=256, null=True)



