from django.db import models
from django.utils import timezone

class Equipment(models.Model):
    name = models.CharField(max_length=100)  
    description = models.TextField(null=True, blank=True) 
    image = models.ImageField(upload_to='equipment_images/', blank=True, null=True)  
    status_choices = [
        ('libre', 'Libre'),
        ('occupé', 'Occupé'),
        ('réservé', 'Réservé'),
    ]
    status = models.CharField(max_length=10, choices=status_choices, default='libre')
    reservation_date = models.DateTimeField(null=True, blank=True)  
    last_maintenance = models.DateField(null=True, blank=True)
    reserved_by = models.CharField(max_length=100, blank=True, null=True)  # Nom de la personne
    reservation_time = models.DateTimeField(blank=True, null=True) 
    category = models.CharField(max_length=50, choices=[('cardio', 'Cardio'), ('musculation', 'Musculation')])

    def __str__(self):
        return self.name


    def is_available(self):
        return self.status == 'libre' or (self.status == 'réservé' and self.reservation_date > timezone.now())


class Athlete(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    current_equipment = models.ForeignKey(Equipment, on_delete=models.SET_NULL, null=True, blank=True)
    equipment_reservation_time = models.DateTimeField(null=True, blank=True) 
    objective = models.CharField(max_length=100, blank=True)
    is_using_machine = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


