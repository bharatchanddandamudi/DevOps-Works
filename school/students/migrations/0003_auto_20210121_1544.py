# Generated by Django 2.2.17 on 2021-01-21 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20210121_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='qualications',
            field=models.CharField(choices=[('G4', 'Grade4'), ('G5', 'Grade5'), ('G7', 'Grade7'), ('G3', 'Grade3'), ('G9', 'Grade9'), ('G8', 'Grade8'), ('G10', 'Grade10'), ('G6', 'Grade6'), ('G2', 'Grade2'), ('G1', 'Grade1')], max_length=2),
        ),
    ]
