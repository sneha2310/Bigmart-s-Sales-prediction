# Generated by Django 3.2.3 on 2021-05-20 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project1', '0003_rename_outlet_location_user_outlet_location_types'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='Outlet_Location_Types',
            new_name='Outlet_Location_Type',
        ),
    ]