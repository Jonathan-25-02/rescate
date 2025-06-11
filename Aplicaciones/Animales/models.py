from django.db import models

class EquipoRescate(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=200)
    foto_equipo = models.ImageField(upload_to='equipos/', null=True, blank=True)

    def __str__(self):
        return self.nombre

class Rescate(models.Model):
    fecha = models.DateTimeField()
    ubicación = models.CharField(max_length=200)
    foto_rescate = models.ImageField(upload_to='rescates/', null=True, blank=True)
    equipos = models.ManyToManyField(EquipoRescate, through='ReporteRescate')

    def __str__(self):
        return f'Rescate #{self.id} - {self.ubicación}'

class ReporteRescate(models.Model):
    rescate = models.OneToOneField(Rescate, on_delete=models.CASCADE)
    equipo = models.ForeignKey(EquipoRescate, on_delete=models.CASCADE)
    observaciones = models.TextField()
    pdf_informe = models.FileField(upload_to='reportes/', null=True, blank=True)

    def __str__(self):
        return f'Reporte de Rescate #{self.rescate.id} por {self.equipo.nombre}'
