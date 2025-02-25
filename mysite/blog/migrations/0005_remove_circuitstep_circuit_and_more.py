# Generated by Django 5.1.3 on 2024-11-20 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_athlete_equipment_reservation_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='circuitstep',
            name='circuit',
        ),
        migrations.RemoveField(
            model_name='circuitstep',
            name='athlete',
        ),
        migrations.RemoveField(
            model_name='circuitstep',
            name='equipment',
        ),
        migrations.AddField(
            model_name='equipment',
            name='reservation_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='equipment',
            name='reserved_by',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='Circuit',
        ),
        migrations.DeleteModel(
            name='CircuitStep',
        ),
    ]
