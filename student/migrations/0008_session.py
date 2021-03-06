# Generated by Django 2.0.13 on 2019-06-18 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
        ('student', '0007_auto_20190618_1339'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('className', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='teacher.Class')),
                ('student', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
            ],
        ),
    ]
