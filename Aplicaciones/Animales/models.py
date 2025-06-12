from django.db import models

class Especie(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Rescate(models.Model):
    fecha = models.DateTimeField()
    ubicacion = models.CharField(max_length=255)
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE)
    foto_rescate = models.ImageField(upload_to='rescates/')

    def __str__(self):
        return f"{self.especie.nombre} - {self.ubicacion} ({self.fecha.date()})"

class EquipoRescate(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    foto_equipo = models.ImageField(upload_to='equipos/')

    def __str__(self):
        return self.nombre

class ReporteRescate(models.Model):
    rescate = models.OneToOneField(Rescate, on_delete=models.CASCADE)
    equipo = models.ForeignKey(EquipoRescate, on_delete=models.CASCADE)
    observaciones = models.TextField()
    pdf_informe = models.FileField(upload_to='reportes/')

    def __str__(self):
        return f"Reporte de {self.rescate}"
