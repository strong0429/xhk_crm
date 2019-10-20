from django.db import models

# Create your models here.

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

'''
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
'''


