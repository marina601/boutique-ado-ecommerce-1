# Generated by Django 3.2.6 on 2021-08-19 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20210819_0956'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='orgiginal_bag',
            new_name='original_bag',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='striipe_pid',
            new_name='stripe_pid',
        ),
    ]
