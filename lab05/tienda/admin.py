from django.contrib import admin

# Register your models here.
from .models import Empleados
admin.site.register(Empleados)

from .models import Cliente
admin.site.register(Cliente)