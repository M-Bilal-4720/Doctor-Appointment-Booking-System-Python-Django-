# Generated by Django 4.2.2 on 2023-07-19 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appointment', '0019_alter_review_message_alter_review_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
