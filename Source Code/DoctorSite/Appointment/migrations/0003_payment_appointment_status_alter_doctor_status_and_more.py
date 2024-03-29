# Generated by Django 4.2.2 on 2023-07-15 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Appointment', '0002_rename_specialization_specialization_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateTimeField()),
                ('amount', models.CharField(default='', max_length=100)),
                ('status', models.CharField(default='False', max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='status',
            field=models.CharField(default='False', max_length=20),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='status',
            field=models.CharField(default='False', max_length=20),
        ),
        migrations.DeleteModel(
            name='AppointmentStatus',
        ),
        migrations.AddField(
            model_name='payment',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Appointment.doctor'),
        ),
        migrations.AddField(
            model_name='payment',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Appointment.patient'),
        ),
    ]
