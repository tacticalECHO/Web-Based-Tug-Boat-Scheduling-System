# Generated by Django 4.2.7 on 2024-02-28 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0022_alter_task_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='State',
            field=models.CharField(choices=[('Scheduled', 'Scheduled'), ('Unscheduled', 'Unscheduled'), ('Completed', 'Completed'), ('Expired', 'Expired')], default='Unscheduled', max_length=100),
        ),
    ]
