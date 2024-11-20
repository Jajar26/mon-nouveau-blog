# Generated by Django 5.1.3 on 2024-11-20 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_equipment_description_equipment_last_maintenance_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='athlete',
            name='equipment_reservation_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='equipment',
            name='reservation_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='equipment_images/'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='status',
            field=models.CharField(choices=[('libre', 'Libre'), ('occupé', 'Occupé'), ('réservé', 'Réservé')], default='libre', max_length=10),
        ),
    ]
