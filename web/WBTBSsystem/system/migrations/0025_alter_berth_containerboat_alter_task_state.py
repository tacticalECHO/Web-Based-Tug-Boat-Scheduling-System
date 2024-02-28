# Generated by Django 5.0.2 on 2024-02-28 20:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0024_alter_task_options_alter_berth_containerboat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='berth',
            name='ContainerBoat',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='berth', to='system.containerboat'),
        ),
        migrations.AlterField(
            model_name='task',
            name='State',
            field=models.CharField(choices=[('Scheduled', 'Scheduled'), ('Unscheduled', 'Unscheduled')], default='Unscheduled', max_length=100),
        ),
    ]