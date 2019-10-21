from django.db import models

from sys_admin.models import Employee

# Create your models here.

class User(models.Model):
    name = models.CharField('账号', max_length=128, unique=True)
    password = models.CharField('密码', max_length=256)
    employee = models.OneToOneField(Employee, models.CASCADE)
    mobile = models.CharField('手机', max_length=12, unique=True)
    address = models.CharField('住址', max_length=128, null=True, blank=True)
    wechat = models.CharField('微信', max_length=128, null=True, blank=True)
    email = models.EmailField('邮箱', null=True, blank=True)
    hobby = models.CharField('爱好', max_length=256, null=True, blank=True)
    active = models.BooleanField('状态', default='True')
    c_time = models.DateTimeField('注册日期', auto_now_add=True)
    # has_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'app_user'

        ordering = ['c_time']
        # verbose_name = '用户'
        # verbose_name_plural = '用户'

'''
class ConfirmString(models.Model):
    code = models.CharField(max_length=256)
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name + ": " + self.code

    class Meta:
        db_table = 'confirm_string'

        ordering = ['c_time']
        verbose_name = '确认码'
        verbose_name_plural = '确认码'
'''