# Generated by Django 5.1.3 on 2025-02-07 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserAttendance',
        ),
    ]
