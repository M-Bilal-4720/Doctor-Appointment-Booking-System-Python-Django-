# Generated by Django 4.2.2 on 2023-07-18 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appointment', '0012_alter_appointment_doctor_alter_appointment_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appt_time',
            field=models.CharField(max_length=20),
        ),
    ]
