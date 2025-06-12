from django.db import models

class Especie(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre

class Rescate(models.Model):
    fecha = models.DateTimeField()
    ubicacion = models.CharField(max_length=255)
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE, default=1)
    foto_rescate = models.ImageField(upload_to='rescates/', null=True, blank=True)

    def __str__(self):
        return f"{self.especie.nombre} - {self.ubicacion} ({self.fecha.date()})"

class EquipoRescate(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    foto_equipo = models.ImageField(upload_to='equipos/', default='equipos/default.jpg')  # Valor por defecto agregado

    def __str__(self):
        return self.nombre

class ReporteRescate(models.Model):
    rescate = models.OneToOneField(Rescate, on_delete=models.CASCADE)
    equipo = models.ForeignKey(EquipoRescate, on_delete=models.CASCADE, default=1)  # Valor por defecto agregado
    observaciones = models.TextField()
    pdf_informe = models.FileField(upload_to='reportes/', default='reportes/default.pdf')  # Valor por defecto agregado

    def __str__(self):
        return f"Reporte de {self.rescate}"
