# Generated by Django 4.2.7 on 2024-03-03 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0029_remove_containerboat_arrivaltime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduleentry',
            name='EndTime',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='scheduleentry',
            name='PublishTime',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='scheduleentry',
            name='StartTime',
            field=models.DateTimeField(),
        ),
    ]
