from django import forms
from .models import Athlete
from django.utils import timezone


class EquipmentUseForm(forms.ModelForm):
    STATUS_CHOICES = (
        ('occupé', 'Occupé maintenant'),
        ('réservé', 'Réservé pour plus tard'),
    )

    status_choice = forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.RadioSelect, required=True)

    class Meta:
        model = Athlete
        fields = ['current_equipment', 'status_choice']

    def save(self, commit=True):
        athlete = super().save(commit=False)
        
        if athlete.current_equipment and athlete.id:
            previous_equipment = Athlete.objects.get(pk=athlete.id).current_equipment
            if previous_equipment:
                previous_equipment.status = 'libre'
                previous_equipment.save()

        if athlete.current_equipment:
            if self.cleaned_data['status_choice'] == 'occupé':
                athlete.current_equipment.status = 'occupé'
                athlete.current_equipment.save()
            elif self.cleaned_data['status_choice'] == 'réservé':
                athlete.current_equipment.status = 'réservé'
                athlete.current_equipment.save()
                athlete.equipment_reservation_time = timezone.now()  
                athlete.save()

        if commit:
            athlete.save()
        return athlete

