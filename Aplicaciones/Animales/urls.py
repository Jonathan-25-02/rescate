from django.urls import path
from . import views

urlpatterns = [
    # ===================== RESCATES =====================
    path('', views.rescate),  # página principal
    path('nuevoRescate', views.nuevoRescate),
    path('guardarRescate', views.guardarRescate),
    path('eliminarRescate/<id>', views.eliminarRescate),
    path('editarRescate/<id>', views.editarRescate),
    path('actualizarRescate/<id>', views.actualizarRescate),

    # ===================== EQUIPOS =====================
    path('equipos', views.equipo),
    path('nuevoEquipo', views.nuevoEquipo),
    path('guardarEquipo', views.guardarEquipo),
    path('eliminarEquipo/<id>', views.eliminarEquipo),
    path('editarEquipo/<id>', views.editarEquipo),
    path('actualizarEquipo/<id>', views.actualizarEquipo),

    # ===================== REPORTES =====================
    path('reportes', views.reporte),
    path('nuevoReporte', views.nuevoReporte),
    path('guardarReporte', views.guardarReporte),
    path('eliminarReporte/<id>', views.eliminarReporte),
    path('editarReporte/<id>', views.editarReporte),
    path('actualizarReporte/<id>', views.actualizarReporte),
]
