# Generated by Django 2.2.4 on 2020-02-13 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gatherings', '0002_gathering_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='gathering',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]