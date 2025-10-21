from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import PerfilUsuario
from .forms import RegistroUsuarioForm
from .utils import generar_username  # Para la función de generación de username
from datetime import date

def registro_usuario(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]

            username = generar_username(first_name, last_name)

            user = User.objects.create_user(
                username=username,
                password=form.cleaned_data["password1"],
                email=form.cleaned_data["email"],
                first_name=first_name,
                last_name=last_name
            )
            PerfilUsuario.objects.create(
                usuario=user,
                fecha_nacimiento=form.cleaned_data["fecha_nacimiento"],
                curso=form.cleaned_data["curso"]
            )
            return redirect("login")
    else:
        form = RegistroUsuarioForm()
    return render(request, "registro.html", {"form": form})

def home(request):
    return render(request, 'home.html')