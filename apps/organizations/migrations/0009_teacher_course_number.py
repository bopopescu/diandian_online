# Generated by Django 2.1.7 on 2019-03-02 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0008_courseorganization_organization_mark'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='course_number',
            field=models.IntegerField(default=0, verbose_name='课程数量'),
        ),
    ]