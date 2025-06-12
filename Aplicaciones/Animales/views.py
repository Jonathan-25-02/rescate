from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Rescate, EquipoRescate, ReporteRescate, Especie

def rescate(request):
    rescates = Rescate.objects.all()
    return render(request, "rescate.html", {'rescates': rescates})

def nuevoRescate(request):
    especies = Especie.objects.all()
    return render(request, "nuevoRescate.html", {'especies': especies})

def guardarRescate(request):
    fecha = request.POST["fecha"]
    ubicacion = request.POST["ubicacion"]
    especie_id = request.POST["especie"]
    foto = request.FILES.get("foto_rescate")
    especie= Especie.objects.get(id=especie_id)
    Rescate.objects.create(fecha=fecha, ubicacion=ubicacion, especie=especie, foto_rescate=foto)
    messages.success(request, "Rescate guardado exitosamente")
    return redirect('/rescates/')

def eliminarRescate(request, id):
    rescate = get_object_or_404(Rescate, id=id)
    rescate.delete()
    messages.success(request, "Rescate eliminado correctamente")
    return redirect('/rescates/')

def editarRescate(request, id):
    rescateEditar = get_object_or_404(Rescate, id=id)
    especies = Especie.objects.all()
    return render(request, "editarRescate.html", {'rescateEditar': rescateEditar, 'especies': especies})

def procesarEdicionRescate(request, id):
    rescate = get_object_or_404(Rescate, id=id)
    rescate.fecha = request.POST["fecha"]
    rescate.ubicacion = request.POST["ubicacion"]
    especie_id = request.POST["especie"]
    rescate.especie = Especie.objects.get(id=especie_id)
    rescate.foto_rescate = request.FILES.get("foto_rescate", rescate.foto_rescate)
    rescate.save()
    messages.success(request, "Rescate actualizado correctamente")
    return redirect('/rescates/')


def equipo(request):
    equipos = EquipoRescate.objects.all()
    return render(request, "equipo.html", {'equipos': equipos})

def nuevoEquipo(request):
    return render(request, "nuevoEquipo.html")

def guardarEquipo(request):
    nombre = request.POST["nombre"]
    especialidad = request.POST["especialidad"]
    foto = request.FILES.get("foto_equipo")

    EquipoRescate.objects.create(nombre=nombre, especialidad=especialidad, foto_equipo=foto)
    messages.success(request, "Equipo guardado exitosamente")
    return redirect('/equipo')

def eliminarEquipo(request, id):
    equipo = get_object_or_404(EquipoRescate, id=id)
    equipo.delete()
    messages.success(request, "Equipo eliminado correctamente")
    return redirect('/equipo')

def editarEquipo(request, id):
    equipoEditar = get_object_or_404(EquipoRescate, id=id)
    return render(request, "editarEquipo.html", {'equipoEditar': equipoEditar})

def procesarEdicionEquipo(request, id):
    equipo = get_object_or_404(EquipoRescate, id=id)
    equipo.nombre = request.POST["nombre"]
    equipo.especialidad = request.POST["especialidad"]
    equipo.foto_equipo = request.FILES.get("foto_equipo", equipo.foto_equipo)
    equipo.save()
    messages.success(request, "Equipo actualizado correctamente")
    return redirect('/equipo')

def reportes(request):
    reportes = ReporteRescate.objects.all()
    return render(request, "reporte.html", {'reportes': reportes})

def nuevoReporte(request):
    rescates = Rescate.objects.all()
    equipos = EquipoRescate.objects.all()
    return render(request, "nuevoReporte.html", {'rescates': rescates, 'equipos': equipos})

def guardarReporte(request):
    rescate_id = request.POST["rescate"]
    equipo_id = request.POST["equipo"]
    observaciones = request.POST["observaciones"]
    pdf = request.FILES.get("pdf_informe")

    ReporteRescate.objects.create(
        rescate_id=rescate_id,
        equipo_id=equipo_id,
        observaciones=observaciones,
        pdf_informe=pdf
    )
    messages.success(request, "Reporte guardado exitosamente")
    return redirect('/reportes/')

def eliminarReporte(request, id):
    reporte = get_object_or_404(ReporteRescate, id=id)
    reporte.delete()
    messages.success(request, "Reporte eliminado correctamente")
    return redirect('/reportes/')

def editarReporte(request, id):
    reporteEditar = get_object_or_404(ReporteRescate, id=id)
    rescates = Rescate.objects.all()
    equipos = EquipoRescate.objects.all()
    return render(request, "editarReporte.html", {
        'reporteEditar': reporteEditar,
        'rescates': rescates,
        'equipos': equipos
    })

def procesarEdicionReporte(request, id):
    reporte = get_object_or_404(ReporteRescate, id=id)
    reporte.rescate_id = request.POST["rescate"]
    reporte.equipo_id = request.POST["equipo"]
    reporte.observaciones = request.POST["observaciones"]
    reporte.pdf_informe = request.FILES.get("pdf_informe", reporte.pdf_informe)
    reporte.save()
    messages.success(request, "Reporte actualizado correctamente")
    return redirect('/reportes/')

def listaEspecies(request):
    especies = Especie.objects.all()
    return render(request, 'especie.html', {'especies': especies})

def nuevaEspecie(request):
    return render(request, 'nuevaEspecie.html')

def guardarEspecie(request):
    nombre = request.POST["nombre"]
    descripcion = request.POST["descripcion"]
    Especie.objects.create(nombre=nombre, descripcion=descripcion)
    messages.success(request, "Especie guardada exitosamente")
    return redirect('/especies/')

def editarEspecie(request, id):
    especie = get_object_or_404(Especie, id=id)

    return render(request, 'editarEspecie.html', {'especie': especie})

def actualizarEspecie(request, id):
    especie = get_object_or_404(Especie, id=id)
    especie.nombre = request.POST["nombre"]
    especie.descripcion = request.POST["descripcion"]
    especie.save()
    messages.success(request, "Especie actualizada correctamente")
    return redirect('/especies/')

def eliminarEspecie(request, id):
    especie = get_object_or_404(Especie, id=id)
    especie.delete()
    messages.success(request, "Especie eliminada correctamente")
    return redirect('/especies/')