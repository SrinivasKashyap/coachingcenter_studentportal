# Generated by Django 2.0.13 on 2019-06-19 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0012_auto_20190619_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='total',
            field=models.FloatField(default=None, null=True),
        ),
    ]
