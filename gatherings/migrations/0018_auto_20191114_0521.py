# Generated by Django 2.2.4 on 2019-11-14 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gatherings', '0017_auto_20190827_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='airtableID',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]