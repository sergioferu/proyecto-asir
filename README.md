# 🚀 Proyecto ASIR - **FixIt**

## 📌 Descripción
Este proyecto consiste en el desarrollo de una **aplicación web de gestión de incidencias**.  
El objetivo es ofrecer una plataforma donde los usuarios puedan **registrar incidencias detalladas**, asignándoles un nivel de importancia del **0 al 4**:

- **Nivel 0** → Crítico (requiere atención inmediata)  
- **Nivel 1** → Alto  
- **Nivel 2** → Medio  
- **Nivel 3** → Bajo  
- **Nivel 4** → Informativo / seguimiento  

Según la gravedad, el técnico recibirá una **alerta proporcional al nivel de la incidencia**, facilitando la priorización y resolución de problemas.

## ⚙️ Funcionamiento
El usuario inicia sesión en el portal inicial (si es que este usuario tiene una cuenta registrada en la base de datos. En su defecto, tendrá que registrarse previamente. Para ello, podrá hacerlo eligiendo el apartado de `registrarse`). Una vez iniciado sesión accederá a un formulario de registro de incidencia en el que tendrá que rellenar un formulario con los siguientes datos:

- Localización de la incidencia
- Fecha de la incidencia
- Descripción de los hechos
- Puesto de trabajo con mayor importancia afectado
- Dispositivo afectado
- Comentarios / Extras

Una vez enviado el formulario, el técnico recibirá en el panel de control una alerta y según la importancia de la incidencia aparecerá más arriba o más abajo.
