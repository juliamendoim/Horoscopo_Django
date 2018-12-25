from django.db import models
from django.forms import ModelForm
from prediccion.models import Horoscope

class CargarForm(ModelForm):
    
    class Meta:
        model =  Horoscope
        fields = ('signo', 'palabra')

   