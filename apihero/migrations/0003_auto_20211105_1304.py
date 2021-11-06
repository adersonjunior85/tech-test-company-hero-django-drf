# Generated by Django 3.2.9 on 2021-11-05 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apihero', '0002_auto_20211105_1301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='company',
        ),
        migrations.AddField(
            model_name='employee',
            name='companies',
            field=models.ManyToManyField(related_name='employees', to='apihero.Company'),
        ),
    ]
