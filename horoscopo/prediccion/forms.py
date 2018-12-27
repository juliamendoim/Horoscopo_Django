from django.db import models
from django.forms import ModelForm
from prediccion.models import Horoscope, Usuario
from django import forms

class CargarUsuario(ModelForm):

    class Meta:
        model = Usuario
        fields = ('name', 'email')

class CargarForm(ModelForm):
    
    class Meta:
        model =  Horoscope
        fields = ('signo', 'palabra' )


    





   