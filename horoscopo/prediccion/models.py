from django.db import models


class Usuario(models.Model):
    name = models.CharField(max_length = 30, unique = True, default = '', primary_key = True)
    email = models.EmailField(max_length = 254, default = 'chicho@gmail.com')

    def __str__(self):
        return self.name

class Horoscope(models.Model):

    usuario = models.ForeignKey(Usuario, default = '', blank = True, null = True)

    ARIES = 'ARIES'
    TAURO = 'TAURO'
    GEMINIS = 'GEMINIS'
    CANCER = 'CANCER'
    LEO = 'LEO'
    VIRGO = 'VIRGO'
    LIBRA = 'LIBRA'
    ESCORPIO = 'ESCORPIO'
    OFIUCO = 'OFIUCO'
    SAGITARIO = 'SAGITARIO'
    CAPRICORNIO = 'CAPRICORNIO'
    ACUARIO = 'ACUARIO'
    PISCIS = 'PISCIS'
    SIGN = (
        (ARIES , 'ARIES'),
        (TAURO , 'TAURO'),
        (GEMINIS , 'GEMINIS'),
        (CANCER , 'CANCER'),
        (LEO , 'LEO'),
        (VIRGO , 'VIRGO'),
        (LIBRA , 'LIBRA'),
        (ESCORPIO , 'ESCORPIO'),
        (OFIUCO , 'OFIUCO'),
        (SAGITARIO , 'SAGITARIO'),
        (CAPRICORNIO , 'CAPRICORNIO'),
        (ACUARIO , 'ACUARIO'),
        (PISCIS , 'PISCIS'),
    )
    signo =  models.CharField(max_length=10, choices=SIGN, default=ARIES)

    AMOR = 'AMOR'
    TRABAJO = 'TRABAJO'
    SALUD = 'SALUD'
    THEME = (
        (AMOR, 'Amor'),
        (TRABAJO, 'Trabajo'),
        (SALUD, 'Salud'),
    )

    palabra = models.CharField(max_length=10, choices=THEME, default=AMOR)






