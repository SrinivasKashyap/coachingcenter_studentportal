# Generated by Django 2.0.13 on 2019-06-19 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
        ('student', '0008_session'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='session',
            unique_together={('className', 'student')},
        ),
    ]
