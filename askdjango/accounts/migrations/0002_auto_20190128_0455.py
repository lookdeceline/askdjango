# Generated by Django 2.1.5 on 2019-01-28 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='use',
            new_name='user',
        ),
    ]
