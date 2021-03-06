# Generated by Django 2.1.7 on 2019-03-04 03:59

from django.db import migrations, models
import organizations.models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0010_auto_20190303_0355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseorganization',
            name='organization_image',
            field=models.ImageField(max_length=500, upload_to=organizations.models.get_upload_org_image_path, verbose_name='机构图片'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teacher_image',
            field=models.ImageField(max_length=500, upload_to=organizations.models.get_upload_teacher_image_path, verbose_name='教师图片'),
        ),
    ]
