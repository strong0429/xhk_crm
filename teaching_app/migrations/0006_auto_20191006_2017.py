# Generated by Django 2.2.5 on 2019-10-06 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teaching_app', '0005_auto_20191006_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campus',
            name='address_cam',
            field=models.CharField(max_length=64, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='campus',
            name='comment_cam',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='campus',
            name='name_cam',
            field=models.CharField(max_length=32, verbose_name='名字'),
        ),
        migrations.AlterField(
            model_name='campus',
            name='phone_cam',
            field=models.CharField(max_length=16, verbose_name='电话'),
        ),
        migrations.AlterField(
            model_name='campus',
            name='supervisor_cam',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='teaching_app.Employee', verbose_name='主管'),
        ),
        migrations.AlterField(
            model_name='departments',
            name='code_dep',
            field=models.CharField(max_length=8, primary_key=True, serialize=False, verbose_name='代码'),
        ),
        migrations.AlterField(
            model_name='departments',
            name='duty_dep',
            field=models.CharField(max_length=128, verbose_name='职责'),
        ),
        migrations.AlterField(
            model_name='departments',
            name='name_dep',
            field=models.CharField(max_length=16, unique=True, verbose_name='名字'),
        ),
        migrations.AlterField(
            model_name='departments',
            name='superior_dep',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='上级部门'),
        ),
        migrations.AlterField(
            model_name='departments',
            name='supervisor_dep',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='teaching_app.Employee', verbose_name='主管'),
        ),
    ]