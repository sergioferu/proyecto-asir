from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from fixit.models import Incidencia, PerfilUsuario, Tecnico


# Vistas del modelo Incidencia
class Incidencias_View(ListView):
    model = Incidencia
    context_object_name = "Vista del contenido de la tabla Incidencias"
    template_name = "fixit/incidencia/list.html"

class IncidenciaCreateView(CreateView):
    model = Incidencia
    fields = '__all__'
    template_name = "fixit/incidencia/form.html"
    success_url = reverse_lazy('incidencias_list')

class IncidenciaUpdateView(UpdateView):
    model = Incidencia
    fields = '__all__'
    template_name = "fixit/incidencia/form.html"
    success_url = reverse_lazy('incidencias_list')

class IncidenciaDeleteView(DeleteView):
    model = Incidencia
    template_name = "fixit/incidencia/confirm_delete.html"
    success_url = reverse_lazy('incidencias_list')

# Vistas del modelo PerfilUsuario
class PerfilUsuario_View(ListView):
    model = PerfilUsuario
    context_object_name = "Vista del contenido de la tabla PerfilUsuario"
    template_name = "fixit/perfilusuario/list.html"

class PerfilUsuarioCreateView(CreateView):
    model = PerfilUsuario
    fields = '__all__'
    template_name = "fixit/perfilusuario/form.html"
    success_url = reverse_lazy('perfilusuario_list')

class PerfilUsuarioUpdateView(UpdateView):
    model = PerfilUsuario
    fields = '__all__'
    template_name = "fixit/perfilusuario/form.html"
    success_url = reverse_lazy('perfilusuario_list')

class PerfilUsuarioDeleteView(DeleteView):
    model = PerfilUsuario
    template_name = "fixit/perfilusuario/confirm_delete.html"
    success_url = reverse_lazy('perfilusuario_list')

# Vistas del modelo Tecnico
class Tecnico_View(ListView):
    model = Tecnico
    context_object_name = "Vista del contenido de la tabla Tecnico"
    template_name = "fixit/tecnico/list.html"

class TecnicoCreateView(CreateView):
    model = Tecnico
    fields = '__all__'
    template_name = "fixit/tecnico/form.html"
    success_url = reverse_lazy('tecnico_list')

class TecnicoUpdateView(UpdateView):
    model = Tecnico
    fields = '__all__'
    template_name = "fixit/tecnico/form.html"
    success_url = reverse_lazy('tecnico_list')

class TecnicoDeleteView(DeleteView):
    model = Tecnico
    template_name = "fixit/tecnico/confirm_delete.html"
    success_url = reverse_lazy('tecnico_list')