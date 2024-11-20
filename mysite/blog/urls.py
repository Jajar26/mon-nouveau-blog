from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from blog import views

urlpatterns = [
    path('equipment/', views.equipment_list, name='equipment_list'),
    path('athlete/<str:name>/', views.athlete_detail, name='athlete_detail'),
    path('', views.equipment_list, name='equipment_list'),
    path('equipment/<int:equipment_id>/', views.equipment_detail, name='equipment_detail'),
    path('equipment/<int:equipment_id>/update-status/', views.update_equipment_status, name='update_equipment_status'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
