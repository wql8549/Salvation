# Generated by Django 3.1.3 on 2021-09-06 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '0006_auto_20210902_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('casename', models.CharField(max_length=100, verbose_name='用列名')),
                ('title', models.CharField(max_length=100, verbose_name='用列名称')),
                ('precondition', models.CharField(blank=True, max_length=100, null=True, verbose_name='前置条件')),
                ('data', models.CharField(blank=True, max_length=500, null=True, verbose_name='测试数据')),
                ('isdone', models.BooleanField(blank=True, default=False, null=True, verbose_name='是否完成')),
                ('maintainer', models.CharField(blank=True, max_length=32, null=True, verbose_name='维护者')),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updatetime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('moduleid', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='project.module', verbose_name='关联模块')),
            ],
            options={
                'verbose_name': '测试用例',
                'verbose_name_plural': '测试用例',
            },
        ),
        migrations.CreateModel(
            name='LocationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_type', models.CharField(max_length=100, unique=True, verbose_name='定位类型')),
            ],
            options={
                'verbose_name': '定位类型',
                'verbose_name_plural': '定位类型',
            },
        ),
        migrations.CreateModel(
            name='OperateType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operate_type', models.CharField(max_length=100, unique=True, verbose_name='定位类型')),
            ],
            options={
                'verbose_name': '执行类型',
                'verbose_name_plural': '执行类型',
            },
        ),
        migrations.CreateModel(
            name='CaseSte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('casesteid', models.IntegerField(verbose_name='步骤顺序')),
                ('locate', models.CharField(max_length=200, verbose_name='定位器')),
                ('info', models.CharField(blank=True, max_length=200, null=True, verbose_name='步骤说明')),
                ('expect', models.CharField(blank=True, max_length=200, null=True, verbose_name='预期结果')),
                ('Locat_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='element.locationtype', verbose_name='定位类型')),
                ('caseid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='case_ste', to='element.case', verbose_name='关联用列')),
                ('operate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='element.operatetype', verbose_name='执行类型')),
            ],
            options={
                'verbose_name': '用列步骤',
                'verbose_name_plural': '用列步骤',
            },
        ),
    ]
