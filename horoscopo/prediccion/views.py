from django.shortcuts import render, redirect
from django.http import HttpResponse
from prediccion.models import Horoscope
from prediccion.forms import CargarForm
from django.views.generic import TemplateView


def prediccion(request):
    palabra = Horoscope.objects.all()[:1]  
    print(palabra)
    
    print('esto deberia ser el diccionarioOOOOOOO',palabra)

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