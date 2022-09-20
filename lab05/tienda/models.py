from django.db import models

# Create your models here.
class Empleados(models.Model):
    apellido= models.CharField(max_length=30)
    dni= models.CharField(max_length=9)
    direccion= models.CharField(max_length=40)
    fecha= models.DateField('Fecha Ingreso')

    def __str__(self):
        return self.apellido

class Cliente(models.Model):
    nombres= models.CharField(max_length=40)
    apellidos= models.CharField(max_length=40)
    dni= models.CharField(max_length=8)
    telefono= models.CharField(max_length=9)
    direccion= models.CharField(max_length=40)
    email= models.CharField(max_length=40)
    fecha_nacimiento= models.DateField('Fecha de nacimiento')
    fecha_publicacion= models.DateField('Fecha de publicacion')

    def __str__(self):
        return self.nombres + ", " +self.apellidos