# Generated by Django 4.2.9 on 2024-03-10 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0038_alter_task_containerboatid'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='TaskManual',
            field=models.IntegerField(default=0),
        ),
    ]
