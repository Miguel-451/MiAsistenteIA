# MiAsistenteIA

Proyecto de aprendizaje y desarrollo: construir progresivamente un asistente de inteligencia artificial que funcione en local en Windows.

## Objetivo

Crear un asistente de escritorio capaz de conversar con un modelo de IA local, conservar memoria entre sesiones y, en fases posteriores, interactuar mediante voz y realizar acciones autorizadas en el ordenador.

Este repositorio también documenta el aprendizaje y las decisiones técnicas tomadas durante el desarrollo.

## Estado actual

**Fase:** preparación y fundamentos.  
**Nivel inicial:** Python básico; experiencia previa con Java, C#, .NET, SQL y automatización con Python.  
**Disponibilidad estimada:** 5-7 horas semanales.

Todavía no se ha confirmado la instalación o el uso de Ollama ni la experiencia práctica con APIs REST.

## Documentación

- [Documento maestro del proyecto](DOCUMENTACION/PROYECTO.md)
- [Ruta de aprendizaje](DOCUMENTACION/APRENDIZAJE.md)
- [Arquitectura prevista](DOCUMENTACION/ARQUITECTURA.md)
- [Registro de cambios y avances](DOCUMENTACION/REGISTRO_CAMBIOS.md)
- [Decisiones técnicas](DOCUMENTACION/DECISIONES.md)

## Tecnologías previstas

La selección es provisional y se validará durante el aprendizaje:

- Python: lenguaje principal inicial.
- Ollama: ejecución local de modelos LLM.
- SQLite: almacenamiento local de conversaciones y memoria.
- PySide6: interfaz gráfica de escritorio.
- APIs HTTP/REST y JSON: comunicación entre componentes.
- Git y GitHub: control de versiones y colaboración.

## Cómo empezar

1. Lee `DOCUMENTACION/PROYECTO.md`.
2. Sigue el orden de `DOCUMENTACION/APRENDIZAJE.md`.
3. Trabaja en una rama para cada funcionalidad o bloque relevante.
4. Actualiza el registro cuando completes un avance verificable.
5. No marques una tecnología como aprendida solo por haber seguido un tutorial: intenta explicar y modificar un ejemplo por tu cuenta.

## Principios del proyecto

- Aprender comprendiendo, no copiando código sin entenderlo.
- Construir en incrementos pequeños y comprobables.
- No añadir dependencias sin una razón.
- No subir contraseñas, tokens, claves API, bases de datos personales ni modelos descargados.
- Las acciones sensibles del asistente requerirán permisos y confirmación.
- La documentación debe reflejar el estado real, incluidos errores y limitaciones.
