# Generated by Django 2.1.7 on 2019-02-20 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20190219_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_type',
            field=models.CharField(choices=[('regist', '注册'), ('forget', '找回密码')], max_length=20, verbose_name='验证码类型'),
        ),
    ]