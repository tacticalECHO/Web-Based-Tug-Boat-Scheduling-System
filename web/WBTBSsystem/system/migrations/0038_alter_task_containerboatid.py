# Generated by Django 4.2.7 on 2024-03-08 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0037_alter_task_containerboatid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='ContainerBoatID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.containerboat'),
        ),
    ]
