# Generated by Django 2.2.4 on 2019-11-25 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gatherings', '0021_auto_20191122_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='gathering',
            name='location',
            field=models.CharField(max_length=50, null=True),
        ),
    ]