from django.urls import path
from . import views

urlpatterns = [
    path('Dinosaurios/', views.dinosaurio_list, name="dinosaurio_list"),
    path('Excavaciones/', views.excavacion_list, name="excavacion_list"),
    path('Paleontogos/', views.paleontologo_list, name="paleontologo_list")
]