from django.db import models
from django.forms import ModelForm
from prediccion.models import Horoscope
from django import forms

class CargarForm(ModelForm):
    
    class Meta:
        model =  Horoscope
        fields = ('signo', 'palabra' )


    





   