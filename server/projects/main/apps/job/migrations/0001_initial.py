# -*- coding: utf-8 -*-
# Generated by Django 3.1.12 on 2021-11-29 11:34
"""
job数据迁移脚本
0001_initial
"""
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('scan_conf', '0001_initial'),
        ('codeproj', '0001_initial'),
        ('nodemgr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            # job_job
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scan_id', models.IntegerField(blank=True, null=True, verbose_name='扫描id')),
                ('state', models.IntegerField(
                    choices=[(0, 'Waiting'), (4, 'Initing'), (5, 'Initialized'), (1, 'Running'), (2, 'Closed'),
                             (3, 'Closing')], db_index=True, default=0, verbose_name='状态')),
                ('initialized_time', models.DateTimeField(blank=True, null=True, verbose_name='任务初始化完成时间')),
                ('start_time', models.DateTimeField(blank=True, null=True, verbose_name='启动时间')),
                ('end_time', models.DateTimeField(blank=True, null=True, verbose_name='结束时间')),
                ('expire_time', models.DateTimeField(blank=True, null=True, verbose_name='超时时间')),
                ('last_beat_time', models.DateTimeField(blank=True, null=True, verbose_name='最后一次心跳上报时间')),
                ('context_path', models.TextField(blank=True, null=True, verbose_name='Context')),
                ('result_code', models.IntegerField(blank=True, db_index=True, null=True, verbose_name='结果码')),
                ('result_msg', models.TextField(blank=True, null=True, verbose_name='结果信息')),
                ('result_path', models.TextField(blank=True, null=True, verbose_name='Result')),
                ('create_time', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='创建时间')),
                ('expected_end_time', models.DateTimeField(blank=True, null=True, verbose_name='预期结束时间')),
                ('task_num', models.IntegerField(default=0, verbose_name='子任务数量')),
                ('task_done', models.IntegerField(default=0, verbose_name='已完成子任务数')),
                ('remarks', models.CharField(blank=True, max_length=512, null=True, verbose_name='备注')),
                ('code_line_num', models.IntegerField(blank=True, null=True, verbose_name='代码行数')),
                ('comment_line_num', models.IntegerField(blank=True, null=True, verbose_name='注释行数')),
                ('blank_line_num', models.IntegerField(blank=True, null=True, verbose_name='空白行数')),
                ('total_line_num', models.IntegerField(blank=True, null=True, verbose_name='总行数')),
                ('filtered_code_line_num', models.IntegerField(blank=True, null=True, verbose_name='过滤后的代码行数')),
                ('filtered_comment_line_num', models.IntegerField(blank=True, null=True,
                                                                  verbose_name='过滤后的注释行数')),
                ('filtered_blank_line_num', models.IntegerField(blank=True, null=True, verbose_name='过滤后的空白行数')),
                ('filtered_total_line_num', models.IntegerField(blank=True, null=True, verbose_name='过滤后的总行数')),
                ('efficient_comment_line_num', models.IntegerField(blank=True, null=True, verbose_name='有效注释行')),
                ('filtered_efficient_comment_line_num',
                 models.IntegerField(blank=True, null=True, verbose_name='过滤后的有效注释行')),
                ('created_from', models.CharField(blank=True, max_length=32, null=True, verbose_name='创建渠道')),
                ('async_flag', models.BooleanField(blank=True, default=False, null=True, verbose_name='异步启动标识')),
                ('client_flag', models.BooleanField(blank=True, null=True, verbose_name='客户端创建标识')),
                ('creator', models.CharField(blank=True, max_length=32, null=True, verbose_name='启动人')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codeproj.baseproject',
                                              verbose_name='所属项目')),
                ('remarked_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                                  related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='备注人')),
            ],
            options={
                'index_together': {('end_time', 'result_code'), ('create_time', 'result_code'),
                                   ('start_time', 'result_code')},
            },
        ),
        migrations.CreateModel(
            # job_task
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module', models.CharField(max_length=64, verbose_name='模块')),
                ('task_name', models.CharField(max_length=64, verbose_name='名称')),
                ('params_path', models.CharField(blank=True, max_length=256, null=True, verbose_name='参数路径')),
                ('private', models.BooleanField(default=False, verbose_name='私有')),
                ('result_code', models.IntegerField(blank=True, null=True, verbose_name='结果码')),
                ('result_msg', models.TextField(blank=True, default=None, null=True, verbose_name='结果信息')),
                ('result_path', models.TextField(blank=True, null=True, verbose_name='结果路径')),
                ('create_version', models.CharField(blank=True, max_length=56, null=True, verbose_name='创建版本号')),
                ('execute_version', models.CharField(blank=True, max_length=56, null=True, verbose_name='执行版本号')),
                ('start_time', models.DateTimeField(blank=True, null=True, verbose_name='启动时间')),
                ('end_time', models.DateTimeField(blank=True, null=True, verbose_name='结束时间')),
                ('state', models.IntegerField(
                    choices=[(3, 'Creating'), (0, 'Waiting'), (4, 'Acking'), (1, 'Running'), (2, 'Closed')],
                    db_index=True, default=3, verbose_name='状态')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('register_time', models.DateTimeField(blank=True, null=True, verbose_name='注册时间')),
                ('log_url', models.URLField(blank=True, null=True, verbose_name='日志链接')),
                ('progress_rate', models.IntegerField(default=0, verbose_name='完成进度')),
                ('last_beat_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='心跳时间')),
                ('exec_tags', models.ManyToManyField(to='nodemgr.ExecTag', verbose_name='执行标签')),
                ('job',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.job', verbose_name='所属任务')),
                ('node', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                           to='nodemgr.node', verbose_name='执行节点')),
            ],
        ),
        migrations.CreateModel(
            # job_taskprogress
            name='TaskProgress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=512, verbose_name='进展信息')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('progress_rate', models.IntegerField(blank=True, null=True, verbose_name='完成进度')),
                ('node', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                           to='nodemgr.node', verbose_name='节点')),
                ('task',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.task', verbose_name='Task')),
            ],
        ),
        migrations.CreateModel(
            # job_taskprocessrelation
            name='TaskProcessRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.IntegerField(blank=True, null=True, verbose_name='优先级')),
                ('state', models.IntegerField(
                    choices=[(3, 'Creating'), (0, 'Waiting'), (4, 'Acking'), (1, 'Running'), (2, 'Closed')], default=0,
                    verbose_name='状态')),
                ('private', models.BooleanField(default=False, verbose_name='私有')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('start_time', models.DateTimeField(blank=True, null=True, verbose_name='启动时间')),
                ('end_time', models.DateTimeField(blank=True, null=True, verbose_name='结束时间')),
                ('result_code', models.IntegerField(blank=True, null=True, verbose_name='结果码')),
                ('result_msg', models.TextField(blank=True, default=None, null=True, verbose_name='结果信息')),
                ('result_url', models.TextField(blank=True, null=True, verbose_name='结果路径')),
                ('log_url', models.URLField(blank=True, null=True, verbose_name='日志链接')),
                ('node', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                           to='nodemgr.node', verbose_name='执行节点')),
                ('process', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scan_conf.process',
                                              verbose_name='任务子进程')),
                ('task',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.task', verbose_name='子任务')),
            ],
            options={
                'ordering': ['task__id', 'priority'],
                'unique_together': {('task', 'process')},
                'index_together': {('node', 'state')},
            },
        ),
        migrations.AddField(
            model_name='task',
            name='processes',
            field=models.ManyToManyField(through='job.TaskProcessRelation', to='scan_conf.Process',
                                         verbose_name='子进程'),
        ),
        migrations.AddField(
            model_name='task',
            name='tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='tasks', to='nodemgr.exectag', verbose_name='唯一执行标签'),
        ),
        migrations.AlterUniqueTogether(
            name='task',
            unique_together={('job', 'task_name')},
        ),
        migrations.AlterIndexTogether(
            name='task',
            index_together={('task_name', 'result_code', 'end_time'), ('result_code', 'create_time'),
                            ('task_name', 'start_time')},
        ),
    ]