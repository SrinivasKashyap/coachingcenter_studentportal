# Generated by Django 2.0.13 on 2019-06-19 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0010_auto_20190619_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='rt1_result',
            field=models.FloatField(default=-1, null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='rt2_result',
            field=models.FloatField(default=-1, null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='sa1_result',
            field=models.FloatField(default=-1, null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='sa2_result',
            field=models.FloatField(default=-1, null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='total',
            field=models.FloatField(default=-1, null=True),
        ),
    ]
