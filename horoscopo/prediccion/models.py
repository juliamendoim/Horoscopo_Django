from django.db import models
from django import forms


class Horoscope(models.Model):
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






