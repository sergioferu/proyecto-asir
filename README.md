# 💻 Proyecto ASIR - **FixIt**

## 📌 Descripción
Este proyecto consiste en el desarrollo de una **aplicación web de gestión de incidencias**. El objetivo es ofrecer una plataforma donde los usuarios puedan **registrar incidencias detalladas** del problema.

## ⚙️ Funcionamiento
1. **Inicio de sesión / registro**  
   - El usuario accede al portal y, si ya tiene una cuenta, inicia sesión.  
   - Si no tiene cuenta, puede **registrarse** desde el apartado correspondiente.

2. **Registro de incidencias**  
   Una vez iniciado sesión, el usuario puede **crear una incidencia** completando un formulario con los siguientes datos:
   - **Localización** de la incidencia
   - **Dispositivo** afectado
   - **Descripción detallada** de los hechos
     
     > El usuario va a tener la posibilidad de poder añadir ficheros como logs o imágenes para apoyar la descripción de la incidencia
   - **Nivel de importancia** del hecho

3. **Notificación y gestión**  
   - Al enviar el formulario, el técnico recibe una **alerta en su panel de control**.  
   - Según el nivel de importancia, la incidencia se mostrará más arriba o más abajo en la lista, permitiendo priorizar la atención.
   
      - **Nivel 0** → Crítico (requiere atención inmediata)  
      - **Nivel 1** → Alto  
      - **Nivel 2** → Medio  
      - **Nivel 3** → Bajo  
      - **Nivel 4** → Informativo / seguimiento  

El usuario podrá **eliminar la incidencia** si es que se ha solucionado, evitando así, el sobretrabajo del técnico.

---

## 💡 Beneficios
- Priorización automática de incidencias según su gravedad
- Registro detallado que facilita el diagnóstico y resolución
- Comunicación clara entre usuarios y técnicos
- Mejora la eficiencia en la gestión de incidencias y soporte técnico

---

## 🚀 Despliegue
Para lanzar el proyecto lo primero que se debe hacer es descargar el repositorio:
```
git clone https://github.com/sergioferu/proyecto-asir
cd proyecto-asir
```

Dentro del repositorio encontramos el directorio `bin/activate`. Este directorio permite lanzar el entorno virtual en el que tenemos las dependecias descargadas necesarias para el proyecto.
> Para acceder al entorno virtual, previamente debemos poner en la consola `bin/activate`

Importante: Si es la primera vez que configuras el proyecto o si el entorno virtual no tiene las dependencias instaladas, debes instalar las librerías del archivo `requirements.txt`:
```
pip install -r requirements.txt
```
> Para verificar que las dependencias se han instalado correctamente, ejecutamos el siguiente comando: `pip list`

Una vez dentro del entorno virtual y con las dependencias instaladas, lanzamos los siguientes comandos:
```
cd proyecto-asir
python3 manage.py runserver
```
