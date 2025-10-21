from django.contrib import admin
from .models import PerfilUsuario, Incidencia, Tecnico

# Registrar los modelos abajo de aquí.

admin.site.register(PerfilUsuario)
admin.site.register(Incidencia)
admin.site.register(Tecnico)