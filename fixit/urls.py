from django.urls import path
from fixit.views import Incidencias_View, PerfilUsuario_View, Tecnico_View

urlpatterns = [
    path("incidencias/", Incidencias_View.as_view()),
    path("perfil_usuario/", PerfilUsuario_View.as_view()),
    path("perfil_tecnico/", Tecnico_View.as_view()),
]