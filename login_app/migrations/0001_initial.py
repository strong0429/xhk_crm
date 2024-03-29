# Generated by Django 2.2.5 on 2019-10-21 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sys_admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='账号')),
                ('password', models.CharField(max_length=256, verbose_name='密码')),
                ('mobile', models.CharField(max_length=12, unique=True, verbose_name='手机')),
                ('address', models.CharField(blank=True, max_length=128, null=True, verbose_name='住址')),
                ('wechat', models.CharField(blank=True, max_length=128, null=True, verbose_name='微信')),
                ('emial', models.EmailField(blank=True, max_length=254, null=True, verbose_name='邮箱')),
                ('hobby', models.CharField(blank=True, max_length=256, null=True, verbose_name='爱好')),
                ('active', models.BooleanField(default='True', verbose_name='状态')),
                ('c_time', models.DateTimeField(auto_now_add=True, verbose_name='注册日期')),
                ('employee', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='sys_admin.Employee')),
            ],
            options={
                'db_table': 'app_user',
                'ordering': ['c_time'],
            },
        ),
    ]
