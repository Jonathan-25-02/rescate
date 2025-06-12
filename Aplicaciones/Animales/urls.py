from django.urls import path
from . import views

urlpatterns = [

    # ===================== ESPECIE =====================
    path('especies/', views.lista_especies),
    path('nuevaEspecie/', views.nueva_especie),
    path('guardarEspecie/', views.guardar_especie),
    path('editarEspecie/<id>/', views.editar_especie),
    path('actualizarEspecie/<id>/', views.actualizar_especie),
    path('eliminarEspecie/<id>/', views.eliminar_especie),




    # ===================== RESCATE =====================
    path('', views.rescate),
    path('rescate/', views.rescate),
    path('nuevoRescate/', views.nuevoRescate),
    path('guardarRescate/', views.guardarRescate),
    path('eliminarRescate/<id>', views.eliminarRescate),
    path('editarRescate/<id>', views.editarRescate),
    path('procesarEdicionRescate/<id>', views.procesarEdicionRescate),

    # ===================== EQUIPO DE RESCATE =====================
    path('equipos/', views.equipo),
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
