from django.shortcuts import render
from .models import Dinosaurio, Paleontologo, Excavacion

# Create your views here.
def dinosaurio_list(request):
    posts = Dinosaurio.objects.all()
    return render(request, 'Dinosaurios/dinosaurio_list.html',{"dinosaurio_mostrar":posts})

def paleontologo_list(request):
    posts = Paleontologo.objects.all()
    return render(request, 'Paleontologos/paleontologo_list.html',{"paleontologo_mostrar":posts})

def excavacion_list(request):
    posts = Excavacion.objects.all()
    return render(request, 'Excavaciones/excavacion_list.html',{"excavacion_mostrar":posts})