# Generated by Django 4.2.2 on 2023-07-18 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appointment', '0013_alter_appointment_appt_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(default='New', max_length=20),
        ),
    ]
