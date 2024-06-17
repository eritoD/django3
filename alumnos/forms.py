from django import forms
from .models import Ramo, Seccion, Alumno

from django.forms import ModelForm

class RamoForm(ModelForm):
    class Meta:
        model=Ramo
        fields= "__all__"

class SeccionForm(ModelForm):
    class Meta:
        model=Seccion
        fields= "__all__"

class AlumnoForm(ModelForm):
    class Meta:
        model=Alumno
        fields= "__all__"