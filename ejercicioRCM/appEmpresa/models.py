from django.db import models
from django.core.validators import RegexValidator
from datetime import date

alphanumeric = RegexValidator(r'^[0-9a-zA-Z\.\-]*$', 'Solo se permiten letras, números, guión y punto.')


class Empresa(models.Model):
    NOMBRE_EMPRESA  = models.CharField(max_length=30)
    RUT_EMPRESA     = models.CharField(max_length=12, validators=[alphanumeric])
    DIRECCIÓN       = models.CharField(max_length=100)
    REGION          = models.IntegerField(default=0)
    PROVINCIA       = models.IntegerField(default=0)
    COMUNA          = models.IntegerField(default=0)

    def __str__(self):
        return self.RUT_EMPRESA


class Contacto(models.Model):
    NOM_CONTACTO    = models.CharField(max_length=50)
    RUT_CONTACTO    = models.CharField(max_length=12, validators=[alphanumeric])  
    APELLP_CONTACTO = models.CharField(max_length=50)
    APELLM_CONTACTO = models.CharField(max_length=50)
    TELEFONO        = models.IntegerField(default=0)
    EMAIL           = models.CharField(max_length=80)
    DIRECCIÓN       = models.CharField(max_length=100)
    REGION          = models.IntegerField(default=0)
    PROVINCIA       = models.IntegerField(default=0)
    COMUNA          = models.IntegerField(default=0)


    def __str__(self):
        return self.RUT_CONTACTO

class Relaciones(models.Model):
    ID_EMPRESA      = models.IntegerField(default=0)
    ID_CONTACTO     = models.IntegerField(default=0)

