# Generated by Django 2.0.13 on 2019-06-14 06:06

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_student', models.BooleanField(default=False)),
                ('is_teacher', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=30, verbose_name='First name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last name')),
            ],
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rt1_result', models.FloatField(default=0.0)),
                ('rt2_result', models.FloatField(default=0.0)),
                ('sa1_result', models.FloatField(default=0.0)),
                ('sa2_result', models.FloatField(default=0.0)),
                ('total', models.FloatField(default=0.0)),
                ('grade', models.CharField(default='', max_length=5, null=True)),
                ('remarks', models.CharField(default='', max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('adm_no', models.IntegerField(primary_key=True, serialize=False)),
                ('rollno', models.IntegerField()),
                ('father_name', models.CharField(max_length=100, null=True)),
                ('mother_name', models.CharField(max_length=100, null=True)),
                ('parent_phn', models.CharField(max_length=10)),
                ('date_join', models.DateField()),
                ('gender', models.CharField(max_length=10, null=True)),
                ('dob', models.DateField()),
            ],
        ),
    ]
