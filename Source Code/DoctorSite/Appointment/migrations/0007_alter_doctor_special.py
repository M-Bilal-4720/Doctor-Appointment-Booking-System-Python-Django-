# Generated by Django 4.2.2 on 2023-07-16 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appointment', '0006_rename_special_id_doctor_special'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='special',
            field=models.CharField(default='', max_length=100),
        ),
    ]