# Generated by Django 2.1.5 on 2019-02-05 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='ip',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
    ]