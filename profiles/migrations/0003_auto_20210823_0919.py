# Generated by Django 3.2.6 on 2021-08-23 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20210823_0909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='default_email',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='default_full_name',
        ),
    ]