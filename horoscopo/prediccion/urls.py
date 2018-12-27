from django.conf.urls import url
from prediccion import views

urlpatterns = [
    url(r"^resultado/$", views.prediccion, name="resultado"),
    url(r"^home/$", views.cargar_valores, name="cargar valores"),
    url(r"^$", views.cargar_usuario, name="cargar usuario"),  
 
]