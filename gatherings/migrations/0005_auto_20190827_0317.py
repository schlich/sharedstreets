# Generated by Django 2.2.4 on 2019-08-27 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gatherings', '0004_auto_20190822_0613'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='gathering_temp',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='session_temp', to='gatherings.Gathering'),
        ),
        migrations.AlterField(
            model_name='session',
            name='gathering',
            field=models.ManyToManyField(related_name='session', to='gatherings.Gathering'),
        ),
    ]
