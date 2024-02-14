# Generated by Django 4.2.2 on 2023-07-16 03:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Appointment', '0003_payment_appointment_status_alter_doctor_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='speci_id',
        ),
        migrations.AddField(
            model_name='doctor',
            name='specialization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Appointment.specialization'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='status',
            field=models.CharField(default='new', max_length=20),
        ),
    ]