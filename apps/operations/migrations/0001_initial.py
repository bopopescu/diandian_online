# Generated by Django 2.1.7 on 2019-02-19 18:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_mark', models.FloatField(default=10.0, verbose_name='课程评分')),
                ('teacher_mark', models.FloatField(default=10.0, verbose_name='教师评分')),
                ('comment', models.CharField(max_length=300, verbose_name='评论')),
                ('add_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='问询添加时间')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='课程')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizations.Teacher', verbose_name='教师')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '用户评论',
                'verbose_name_plural': '用户评论',
            },
        ),
        migrations.CreateModel(
            name='UserAsk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('mobile', models.CharField(max_length=11, verbose_name='手机')),
                ('course_name', models.CharField(max_length=50, verbose_name='课程名称')),
                ('question', models.TextField(verbose_name='咨询内容')),
                ('add_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='问询添加时间')),
            ],
            options={
                'verbose_name': '课程咨询',
                'verbose_name_plural': '课程咨询',
            },
        ),
        migrations.CreateModel(
            name='UserCollection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_id', models.IntegerField(default=0, verbose_name='数据表_id')),
                ('collection_type', models.CharField(choices=[(1, '课程'), (2, '课程机构'), (3, '教师')], default=1, max_length=10, verbose_name='收藏类型')),
                ('add_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='收藏添加时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '用户评论',
                'verbose_name_plural': '用户评论',
            },
        ),
        migrations.CreateModel(
            name='UserCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='学习时间')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='课程')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '用户学习的课程',
                'verbose_name_plural': '用户学习的课程',
            },
        ),
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField(default=0, verbose_name='接受id')),
                ('message', models.CharField(max_length=500, verbose_name='消息内容')),
                ('has_read', models.BooleanField(default=False, verbose_name='消息是否已读')),
                ('send_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='消息发送时间')),
            ],
            options={
                'verbose_name': '用户消息',
                'verbose_name_plural': '用户消息',
            },
        ),
    ]
