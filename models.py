from django.db import models
from django.contrib.auth.models import User

# Perfil de usuario
class PerfilUsuario(models.Model):
    CURSOS = [
        ("1ASIR", "1º ASIR"),
        ("2ASIR", "2º ASIR"),
        ("1DAM", "1º DAM"),
        ("2DAM", "2º DAM"),
        ("1DAW", "1º DAW"),
        ("2DAW", "2º DAW"),
        ("1SMR_A", "1º SMR A"),
        ("1SMR_B", "1º SMR B"),
    ]

    # Relación OneToOne con el usuario de Django
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    # Resto de campos del perfil de usuario
    fecha_nacimiento = models.DateField(null=False, blank=False, default="2000-01-01")
    curso = models.CharField(max_length=10, choices=CURSOS, null=False, blank=False, default="1ASIR")

    def __str__(self):
        return f"{self.usuario} - {self.get_curso_display()}"


# Tabla de las incidencias
class Incidencia(models.Model):
    NIVEL_CHOICES = [
        (0, "Crítico"),
        (1, "Alto"),
        (2, "Medio"),
        (3, "Bajo"),
        (4, "Informativo"),
    ]

    ESTADO_CHOICES = [
        ("abierta", "Abierta"),
        ("en_proceso", "En proceso"),
        ("resuelta", "Resuelta"),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="incidencias")
    descripcion = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True) # Fecha y hora de creación automática (no va a aperecer en el formulario)
    nivel = models.IntegerField(choices=NIVEL_CHOICES, default=4)
    dispositivo = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default="abierta")
    archivo = models.FileField(upload_to="incidencias/", blank=True, null=True)

    def __str__(self):
        return f"[{self.get_nivel_display()}] {self.fecha} - {self.usuario.username} - [{self.get_estado_display()}]"


# Perfil de los técnicos que atienden las incidencias
class Tecnico(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=100)

    incidencias_asignadas = models.ManyToManyField(Incidencia, blank=True, related_name="tecnicos")

    def __str__(self):
        return f"Técnico: {self.usuario.username} ({self.especialidad})"