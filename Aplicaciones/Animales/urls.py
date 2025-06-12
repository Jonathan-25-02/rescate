from django.urls import path
from . import views

urlpatterns = [

    # ===================== ESPECIE =====================
    path('', views.listaEspecies),
    path('especies/', views.listaEspecies),
    path('nuevaEspecie/', views.nuevaEspecie),
    path('guardarEspecie/', views.guardarEspecie),
    path('editarEspecie/<id>/', views.editarEspecie),
    path('actualizarEspecie/<id>/', views.actualizarEspecie),
    path('eliminarEspecie/<id>/', views.eliminarEspecie),


    # ===================== RESCATE =====================
    
    path('rescates/', views.rescate),
    path('nuevoRescate/', views.nuevoRescate),
    path('guardarRescate/', views.guardarRescate),
    path('eliminarRescate/<id>', views.eliminarRescate),
    path('editarRescate/<id>', views.editarRescate),
    path('procesarEdicionRescate/<id>', views.procesarEdicionRescate),

    # ===================== EQUIPO DE RESCATE =====================
    path('equipo/', views.equipo),
    path('nuevoEquipo/', views.nuevoEquipo),
    path('guardarEquipo/', views.guardarEquipo),
    path('eliminarEquipo/<id>', views.eliminarEquipo),
    path('editarEquipo/<id>', views.editarEquipo),
    path('procesarEdicionEquipo/<id>', views.procesarEdicionEquipo),

    # ===================== REPORTE DE RESCATE =====================
    path('reportes/', views.reportes),
    path('nuevoReporte/', views.nuevoReporte),
    path('guardarReporte/', views.guardarReporte),
    path('eliminarReporte/<id>', views.eliminarReporte),
    path('editarReporte/<id>', views.editarReporte),
    path('procesarEdicionReporte/<id>', views.procesarEdicionReporte),
]
