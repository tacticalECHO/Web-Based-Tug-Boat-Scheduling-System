# Generated by Django 4.2.7 on 2024-03-08 10:45

from django.db import migrations, models
import system.models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0036_alter_task_containerboatid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='ContainerBoatID',
            field=models.CharField(max_length=200, unique=True, verbose_name=system.models.ContainerBoat),
        ),
    ]
