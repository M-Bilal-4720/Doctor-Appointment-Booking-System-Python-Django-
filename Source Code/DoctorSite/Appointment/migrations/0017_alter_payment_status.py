# Generated by Django 4.2.2 on 2023-07-19 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appointment', '0016_alter_payment_doctor_alter_payment_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(default='Paid', max_length=20),
        ),
    ]
