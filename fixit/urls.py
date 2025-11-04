from django.urls import path
from fixit.views import (
    Incidencias_View, PerfilUsuario_View, Tecnico_View,
    IncidenciaCreateView, IncidenciaUpdateView, IncidenciaDeleteView,
    PerfilUsuarioCreateView, PerfilUsuarioUpdateView, PerfilUsuarioDeleteView,
    TecnicoCreateView, TecnicoUpdateView, TecnicoDeleteView,
)
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="fixit/home.html"), name="home"),

    path("incidencias/", Incidencias_View.as_view(), name="incidencias_list"),
    path("incidencias/create/", IncidenciaCreateView.as_view(), name="incidencia_create"),
    path("incidencias/<int:pk>/update/", IncidenciaUpdateView.as_view(), name="incidencia_update"),
    path("incidencias/<int:pk>/delete/", IncidenciaDeleteView.as_view(), name="incidencia_delete"),

    path("perfil_usuario/", PerfilUsuario_View.as_view(), name="perfilusuario_list"),
    path("perfil_usuario/create/", PerfilUsuarioCreateView.as_view(), name="perfilusuario_create"),
    path("perfil_usuario/<int:pk>/update/", PerfilUsuarioUpdateView.as_view(), name="perfilusuario_update"),
    path("perfil_usuario/<int:pk>/delete/", PerfilUsuarioDeleteView.as_view(), name="perfilusuario_delete"),

    path("perfil_tecnico/", Tecnico_View.as_view(), name="tecnico_list"),
    path("perfil_tecnico/create/", TecnicoCreateView.as_view(), name="tecnico_create"),
    path("perfil_tecnico/<int:pk>/update/", TecnicoUpdateView.as_view(), name="tecnico_update"),
    path("perfil_tecnico/<int:pk>/delete/", TecnicoDeleteView.as_view(), name="tecnico_delete"),
]