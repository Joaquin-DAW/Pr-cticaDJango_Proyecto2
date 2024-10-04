from django.contrib import admin

# Register your models here.
from .models import Dinosaurio, Paleontologo, Excavacion

admin.site.register(Dinosaurio)
admin.site.register(Paleontologo)
admin.site.register(Excavacion)
