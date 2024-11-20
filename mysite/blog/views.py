from django.shortcuts import render, get_object_or_404, redirect
from .forms import EquipmentUseForm
from .models import Athlete, Equipment
from django.forms import modelformset_factory

def athlete_detail(request, name):
    athlete = get_object_or_404(Athlete, name=name)
    message = ''

    if request.method == "POST":
        form = EquipmentUseForm(request.POST, instance=athlete)
        if form.is_valid():
            form.save()
            return redirect('athlete_detail', name=name)

    else:
        form = EquipmentUseForm(instance=athlete)

    return render(request, 'blog/athlete_detail.html', {
        'athlete': athlete,
        'form': form,
        'message': message
    })

def equipment_list(request):
    all_equipments = Equipment.objects.all()
    total_athletes = Athlete.objects.count()

    if request.method == 'POST':
        equipment_id = request.POST.get('equipment_id')
        new_status = request.POST.get('status')
        reserved_by = request.POST.get('reserved_by', None) 
        reservation_time = request.POST.get('reservation_time', None)

        if equipment_id and new_status in ['libre', 'occupé', 'réservé']:
            equipment = get_object_or_404(Equipment, id=equipment_id)
            equipment.status = new_status
            if new_status == 'réservé':
                equipment.reserved_by = reserved_by
                equipment.reservation_time = reservation_time
            else:
                equipment.reserved_by = None
                equipment.reservation_time = None
            equipment.save()

    return render(request, 'blog/equipment_list.html', {
        'all_equipments': all_equipments,
        'total_athletes': total_athletes,
    })


def equipment_detail(request, equipment_id):
    equipment = get_object_or_404(Equipment, id=equipment_id)
    return render(request, 'blog/equipment_detail.html', {'equipment': equipment})


def update_equipment_status(request, equipment_id):
    equipment = get_object_or_404(Equipment, id=equipment_id)
    
    if request.method == 'POST':
        new_status = request.POST.get('status')  
        
        if new_status in ['libre', 'occupé', 'réservé']:  
            equipment.status = new_status  
            equipment.save()  
            
        return redirect('equipment_detail', equipment_id=equipment.id)  
    
    
    
def use_equipment(request, athlete_id):
    athlete = Athlete.objects.get(pk=athlete_id)
    if request.method == 'POST':
        form = EquipmentUseForm(request.POST, instance=athlete)
        if form.is_valid():
            form.save()  
            return redirect('success_page') 
    else:
        form = EquipmentUseForm(instance=athlete)
    
    return render(request, 'use_equipment.html', {'form': form, 'athlete': athlete})