from django.contrib import admin

# Register your models here.
from .models import Rescate, EquipoRescate, ReporteRescate
admin.register(Rescate)
admin.register(EquipoRescate)
admin.register(ReporteRescate)
