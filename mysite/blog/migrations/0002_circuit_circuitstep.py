# Generated by Django 5.1.3 on 2024-11-19 17:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Circuit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CircuitStep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.PositiveIntegerField(help_text='Duration in seconds')),
                ('rest_time', models.PositiveIntegerField(default=0, help_text='Rest time in seconds')),
                ('athlete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.athlete')),
                ('circuit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='steps', to='blog.circuit')),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.equipment')),
            ],
        ),
    ]
