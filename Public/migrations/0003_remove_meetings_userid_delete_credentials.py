# Generated by Django 5.2.3 on 2025-06-23 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Public', '0002_rename_password_credentials_password_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meetings',
            name='userID',
        ),
        migrations.DeleteModel(
            name='Credentials',
        ),
    ]
