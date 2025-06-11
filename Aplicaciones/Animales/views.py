

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Rescate, EquipoRescate, ReporteRescate

# ==================== RESCATE ====================

def lista_rescates(request):
    rescates = Rescate.objects.all()
    return render(request, "rescate.html", {'rescates': rescates})

def nuevo_rescate(request):
    if request.method == "POST":
        fecha = request.POST["fecha"]
        ubicación = request.POST["ubicación"]
        foto_rescate = request.FILES.get("foto_rescate")
        nuevo = Rescate.objects.create(fecha=fecha, ubicación=ubicación, foto_rescate=foto_rescate)
        messages.success(request, "Rescate guardado exitosamente")
        return redirect('/rescates')
    return render(request, "nuevo Rescate.html")

def editar_rescate(request, id):
    rescate = get_object_or_404(Rescate, id=id)
    return render(request, "editarRescate.html", {"rescate": rescate})

def actualizar_rescate(request, id):
    rescate = get_object_or_404(Rescate, id=id)
    rescate.fecha = request.POST["fecha"]
    rescate.ubicación = request.POST["ubicación"]
    rescate.foto_rescate = request.FILES.get("foto_rescate", rescate.foto_rescate)
    rescate.save()
    messages.success(request, "Rescate actualizado correctamente")
    return redirect('/rescates')

def eliminar_rescate(request, id):
    rescate = get_object_or_404(Rescate, id=id)
    rescate.delete()
    return redirect('/rescates')

# ==================== EQUIPO ====================

def lista_equipos(request):
    equipos = EquipoRescate.objects.all()
    return render(request, "equipo.html", {'equipos': equipos})

def nuevo_equipo(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        especialidad = request.POST["especialidad"]
        foto_equipo = request.FILES.get("foto_equipo")
        EquipoRescate.objects.create(nombre=nombre, especialidad=especialidad, foto_equipo=foto_equipo)
        messages.success(request, "Equipo guardado exitosamente")
        return redirect('/equipos')
    return render(request, "nuevo.Equipo.html")

def editar_equipo(request, id):
    equipo = get_object_or_404(EquipoRescate, id=id)
    return render(request, "editarEquipo.html", {"equipo": equipo})

def actualizar_equipo(request, id):
    equipo = get_object_or_404(EquipoRescate, id=id)
    equipo.nombre = request.POST["nombre"]
    equipo.especialidad = request.POST["especialidad"]
    equipo.foto_equipo = request.FILES.get("foto_equipo", equipo.foto_equipo)
    equipo.save()
    messages.success(request, "Equipo actualizado correctamente")
    return redirect('/equipos')

def eliminar_equipo(request, id):
    equipo = get_object_or_404(EquipoRescate, id=id)
    equipo.delete()
    return redirect('/equipos')

# ==================== REPORTE ====================

def lista_reportes(request):
    reportes = ReporteRescate.objects.all()
    return render(request, "reporte.html", {'reportes': reportes})

def nuevo_reporte(request):
    if request.method == "POST":
        rescate_id = request.POST["rescate"]
        equipo_id = request.POST["equipo"]
        observaciones = request.POST["observaciones"]
        pdf_informe = request.FILES.get("pdf_informe")

        rescate = get_object_or_404(Rescate, id=rescate_id)
        equipo = get_object_or_404(EquipoRescate, id=equipo_id)

        ReporteRescate.objects.create(rescate=rescate, equipo=equipo, observaciones=observaciones, pdf_informe=pdf_informe)
        messages.success(request, "Reporte guardado exitosamente")
        return redirect('/reportes')
    return render(request, "nuevo Resporte.html")

def editar_reporte(request, id):
    reporte = get_object_or_404(ReporteRescate, id=id)
    return render(request, "editarReporte.html", {"reporte": reporte})

def actualizar_reporte(request, id):
    reporte = get_object_or_404(ReporteRescate, id=id)
    reporte.observaciones = request.POST["observaciones"]
    reporte.pdf_informe = request.FILES.get("pdf_informe", reporte.pdf_informe)
    reporte.save()
    messages.success(request, "Reporte actualizado correctamente")
    return redirect('/reportes')

def eliminar_reporte(request, id):
    reporte = get_object_or_404(ReporteRescate, id=id)
    reporte.delete()
    return redirect('/reportes')
