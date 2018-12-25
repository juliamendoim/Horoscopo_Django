from django.db import models


class Horoscope(models.Model):
    signo =  models.CharField(max_length = 20)
    palabra = models.CharField(max_length = 20)

    #def __str__(self):
     #   return ('<%s => %s: %s>' % (self.__class__.__name__, self.signo, self.palabra))