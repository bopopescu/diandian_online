# Generated by Django 2.1.7 on 2019-02-21 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20190220_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofiles',
            name='head_portrait',
            field=models.ImageField(default='apps/users/static/users/images/head_portrait/default.png', max_length=200, upload_to='apps/users/static/users/images/head_portrait/%Y/%m', verbose_name='头像'),
        ),
        migrations.AlterField(
            model_name='viewpage',
            name='image',
            field=models.ImageField(max_length=500, upload_to='apps/users/static/users/images/view_page/%Y/%m', verbose_name='轮播图'),
        ),
    ]
