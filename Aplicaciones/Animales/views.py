from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Rescate, EquipoRescate, ReporteRescate

# ========================== RESCATES ==============================

def rescate(request):
    rescates = Rescate.objects.all()
    return render(request, "rescate.html", {'rescates': rescates})

def nuevoRescate(request):
    return render(request, "nuevoRescate.html")

def guardarRescate(request):
    fecha = request.POST["fecha"]
    ubicacion = request.POST["ubicacion"]
    foto_rescate = request.FILES.get("foto_rescate")
    
    Rescate.objects.create(fecha=fecha, ubicación=ubicacion, foto_rescate=foto_rescate)
    messages.success(request, "Rescate guardado exitosamente")
    return redirect("/rescates")

def eliminarRescate(request, id):
    rescate = Rescate.objects.get(id=id)
    rescate.delete()
    return redirect("/rescates")

def editarRescate(request, id):
    rescate = Rescate.objects.get(id=id)
    return render(request, "editarRescate.html", {'rescateEditar': rescate})

def actualizarRescate(request, id):
    rescate = Rescate.objects.get(id=id)
    rescate.fecha = request.POST["fecha"]
    rescate.ubicación = request.POST["ubicacion"]
    rescate.foto_rescate = request.FILES.get("foto_rescate", rescate.foto_rescate)
    rescate.save()
    messages.success(request, "Rescate actualizado exitosamente")
    return redirect("/rescates")

# ========================== EQUIPOS ==============================

def equipo(request):
    equipos = EquipoRescate.objects.all()
    return render(request, "equipo.html", {'equipos': equipos})

def nuevoEquipo(request):
    return render(request, "nuevoEquipo.html")

def guardarEquipo(request):
    nombre = request.POST["nombre"]
    especialidad = request.POST["especialidad"]
    foto_equipo = request.FILES.get("foto_equipo")

    EquipoRescate.objects.create(nombre=nombre, especialidad=especialidad, foto_equipo=foto_equipo)
    messages.success(request, "Equipo guardado exitosamente")
    return redirect("/equipos")

def eliminarEquipo(request, id):
    equipo = EquipoRescate.objects.get(id=id)
    equipo.delete()
    return redirect("/equipos")

def editarEquipo(request, id):
    equipo = EquipoRescate.objects.get(id=id)
    return render(request, "editarEquipo.html", {'equipoEditar': equipo})

def actualizarEquipo(request, id):
    equipo = EquipoRescate.objects.get(id=id)
    equipo.nombre = request.POST["nombre"]
    equipo.especialidad = request.POST["especialidad"]
    equipo.foto_equipo = request.FILES.get("foto_equipo", equipo.foto_equipo)
    equipo.save()
    messages.success(request, "Equipo actualizado exitosamente")
    return redirect("/equipos")

# ========================== REPORTES ==============================

def reporte(request):
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
    pdf_informe = request.FILES.get("pdf_informe")

    rescate = Rescate.objects.get(id=rescate_id)
    equipo = EquipoRescate.objects.get(id=equipo_id)

    ReporteRescate.objects.create(rescate=rescate, equipo=equipo, observaciones=observaciones, pdf_informe=pdf_informe)
    messages.success(request, "Reporte guardado exitosamente")
    return redirect("/reportes")

def eliminarReporte(request, id):
    reporte = ReporteRescate.objects.get(id=id)
    reporte.delete()
    return redirect("/reportes")

def editarReporte(request, id):
    reporte = ReporteRescate.objects.get(id=id)
    rescates = Rescate.objects.all()
    equipos = EquipoRescate.objects.all()
    return render(request, "editarReporte.html", {'reporteEditar': reporte, 'rescates': rescates, 'equipos': equipos})

def actualizarReporte(request, id):
    reporte = ReporteRescate.objects.get(id=id)
    reporte.rescate = Rescate.objects.get(id=request.POST["rescate"])
    reporte.equipo = EquipoRescate.objects.get(id=request.POST["equipo"])
    reporte.observaciones = request.POST["observaciones"]
    reporte.pdf_informe = request.FILES.get("pdf_informe", reporte.pdf_informe)
    reporte.save()
    messages.success(request, "Reporte actualizado exitosamente")
    return redirect("/reportes")
