# Generated by Django 3.2.3 on 2021-05-20 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project1', '0002_auto_20210519_2217'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='Outlet_Location',
            new_name='Outlet_Location_Types',
        ),
    ]
