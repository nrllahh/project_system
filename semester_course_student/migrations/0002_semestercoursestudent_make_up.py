# Generated by Django 4.1.7 on 2023-04-24 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semester_course_student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='semestercoursestudent',
            name='make_up',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
