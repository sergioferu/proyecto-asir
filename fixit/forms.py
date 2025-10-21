from django import forms
from django.core.exceptions import ValidationError
from .models import PerfilUsuario

CURSOS = PerfilUsuario.CURSOS

class RegistroUsuarioForm(forms.Form):
    first_name = forms.CharField(label="Nombre", max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label="Apellidos", max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Correo electrónico", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    
    password1 = forms.CharField(
        label="Contraseña (min. 8 caracteres)",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        min_length=8,
    )
    password2 = forms.CharField(
        label="Repetir contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        min_length=8
    )

    fecha_nacimiento = forms.DateField(
        label="Fecha de nacimiento (DD-MM-YYYY)",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DD-MM-YYYY'}),
        input_formats=['%d-%m-%Y']
    )
    curso = forms.ChoiceField(label="Curso escolar", choices=CURSOS, widget=forms.Select(attrs={'class': 'form-control'}))

    def clean(self):
        cleaned_data = super().clean()
        pw1 = cleaned_data.get("password1")
        pw2 = cleaned_data.get("password2")
        if pw1 != pw2:
            raise ValidationError("Las contraseñas no coinciden")
        return cleaned_data
