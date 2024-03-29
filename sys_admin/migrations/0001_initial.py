# Generated by Django 2.2.5 on 2019-10-21 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='校名')),
                ('addr', models.CharField(max_length=128, verbose_name='地址')),
                ('phone', models.CharField(max_length=256, verbose_name='电话')),
                ('web_site', models.CharField(blank=True, max_length=256, null=True, verbose_name='网址')),
                ('comment', models.CharField(blank=True, max_length=256, null=True, verbose_name='备注')),
            ],
            options={
                'db_table': 'app_campus',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='名称')),
                ('duty', models.CharField(max_length=256, verbose_name='职责')),
            ],
            options={
                'db_table': 'app_department',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='姓名')),
                ('id_num', models.CharField(max_length=18, unique=True, verbose_name='身份证')),
                ('school', models.CharField(blank=True, max_length=32, null=True, verbose_name='毕业学校')),
                ('major', models.CharField(blank=True, max_length=32, null=True, verbose_name='专业')),
                ('degree', models.CharField(blank=True, max_length=32, null=True, verbose_name='学历')),
                ('active', models.BooleanField(default=True, verbose_name='状态')),
                ('entry_date', models.DateField(verbose_name='入职日期')),
                ('comment', models.CharField(blank=True, max_length=256, null=True, verbose_name='备注')),
                ('base', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sys_admin.Campus')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sys_admin.Department')),
                ('supervisor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='sys_admin.Employee')),
            ],
            options={
                'db_table': 'app_employee',
            },
        ),
        migrations.AddField(
            model_name='department',
            name='director',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='director', to='sys_admin.Employee'),
        ),
        migrations.AddField(
            model_name='department',
            name='superior',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sys_admin.Department'),
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='教室名')),
                ('seat', models.SmallIntegerField(verbose_name='座位数量')),
                ('state', models.BooleanField(default='True', verbose_name='是否可用')),
                ('comment', models.CharField(max_length=256, verbose_name='备注')),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sys_admin.Campus')),
                ('warden', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sys_admin.Employee')),
            ],
            options={
                'db_table': 'app_classroom',
            },
        ),
        migrations.AddField(
            model_name='campus',
            name='supervisor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sys_admin.Employee'),
        ),
    ]
