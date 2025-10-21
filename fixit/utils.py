from django.contrib.auth.models import User

def generar_username(first_name, last_name):
    """
    Genera el username como:
    Nombre + primeras 2 letras del primer apellido + primeras 2 letras del segundo apellido
    """
    apellidos = last_name.strip().split()
    if len(apellidos) < 2:
        # Si solo hay un apellido, repetimos las dos letras del mismo
        ap1 = apellidos[0][:2].lower()
        ap2 = apellidos[0][:2].lower()
    else:
        ap1 = apellidos[0][:2].lower()
        ap2 = apellidos[1][:2].lower()
    
    username_base = f"{first_name}{ap1}{ap2}".lower()
    
    # Comprobar si ya existe el username
    username = username_base
    contador = 1
    while User.objects.filter(username=username).exists():
        username = f"{username_base}{contador}"
        contador += 1

    return username
