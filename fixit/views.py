from django.views.generic import ListView
from fixit.models import Incidencia, PerfilUsuario, Tecnico


class Incidencias_View(ListView):
    model = Incidencia
    context_object_name = "Vista del contenido de la tabla Incidencias"

class PerfilUsuario_View(ListView):
    model = PerfilUsuario
    context_object_name = "Vista del contenido de la tabla PerfilUsuario"

class Tecnico_View(ListView):
    model = Tecnico
    context_object_name = "Vista del contenido de la tabla Tecnico"