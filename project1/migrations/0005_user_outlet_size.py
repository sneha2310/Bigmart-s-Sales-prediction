# Generated by Django 3.2.3 on 2021-05-20 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project1', '0004_rename_outlet_location_types_user_outlet_location_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Outlet_Size',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
