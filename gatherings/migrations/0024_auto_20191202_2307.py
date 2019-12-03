# Generated by Django 2.2.4 on 2019-12-03 05:07

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('gatherings', '0023_auto_20191202_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='pronouns',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='connection',
            field=models.CharField(blank=True, choices=[('1-Acknowledgement', 'Acknowledgement'), ('2-Dialogue/Emotional Connection', 'Dialogue/Emotional Connection'), ('3-Intersection', 'Intersection'), ('4-Invitation', 'Invitation')], max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='participation',
            field=models.CharField(blank=True, choices=[('1-Connection', 'Connection'), ('2-Contact', 'Contact'), ('3-Visitor', 'Visitor'), ('4-Participant', 'Participant'), ('5-Potential Leader', 'Potential Leader'), ('6-Leader', 'Leader'), ('7-Leader-Trainer', 'Leader-Trainer')], max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
    ]
