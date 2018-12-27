from django.shortcuts import render
from django.http import HttpResponse
from prediccion.models import Horoscope
from prediccion.forms import CargarForm
from django.views.generic import TemplateView
import random


def prediccion(request):
        frases = [
                ['Este fin de semana', 'Este mes', 'Este año', 'Estas fiestas'],
                ['será de muchísimo movimiento', 'es mejor evitar las distracciones', 'es mejor morirse', 'hay que disfrutar de todo al máximo'],
                ['se arruinarán todos tus proyectos.', 'mejor ni esperar nada. Andate a dormir.', 'se cumplirán todos tus deseos.', 'será espectacular.'],
                [' No tomes demasiada Fresita.', 'Abrigate.', 'Espectacular!', 'Adiós para siempre.']
        ]
        palabra = Horoscope.objects.latest('id')
        palabra.tiempo = random.choice(frases[0])
        palabra.possigno = random.choice(frases[1])
        palabra.pospalabra = random.choice(frases[2])
        palabra.cierre = random.choice(frases[3])

        return HttpResponse(render(request,"resultado.html", {'dic': palabra}))

def cargar_valores(request):
    if request.method == 'POST':
        form = CargarForm(request.POST)
        
        if form.is_valid():
            nuevaprediccion = Horoscope(signo=request.POST['signo'], palabra=request.POST['palabra'])
            nuevaprediccion.save(form)
            return prediccion(request)
        
    else:
       form = CargarForm()
    
       return render(request, 'prediccion/home.html', {'form':form})
