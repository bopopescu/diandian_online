# Generated by Django 2.1.7 on 2019-03-07 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0025_auto_20190306_2222'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='is_banner',
            field=models.BooleanField(default=False, verbose_name='是否处于轮播位'),
        ),
    ]