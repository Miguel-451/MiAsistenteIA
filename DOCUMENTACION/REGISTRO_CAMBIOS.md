# Registro de cambios y avances

Usar este documento para registrar avances verificables. Añadir entradas nuevas al principio.

## 2026-11-16 — Primer prototipo de conversaciones en consola

- **Objetivo:** combinar fundamentos de Python en un programa de consola con menú.
- **Qué he aprendido:** funciones, parámetros y `return`; lista de diccionarios; `None`; bucles; validaciones; `try/except ValueError`.
- **Qué he implementado:** `codigo/Conversaciones.py` con creación y búsqueda de conversaciones, prevención de IDs duplicados, añadido y consulta de mensajes, listado, menú y salida.
- **Cómo lo he probado:** sesión manual en Windows: conversación ID 1; dos mensajes (`hola` y `adios`) recuperados en orden; listado del diccionario; rechazo de entradas no numéricas en opciones 1, 2 y 4; consulta del ID 99; salida con opción 5.
- **Problemas encontrados:** llamada a una función sin paréntesis, uso de `None` tras conversiones fallidas, petición de mensajes antes de validar la conversación y errores duplicados.
- **Soluciones aplicadas:** invocar `pedir_entero()`, condicionar las acciones a que el ID sea válido y comprobar existencia antes de pedir el mensaje.
- **Alcance pendiente:** los datos aún viven solo en memoria; faltan pruebas adicionales y repaso de fundamentos.
- **Siguiente paso:** bases de datos relacionales y SQLite (todavía no implementado).

## Preparación y ejercicios previos al prototipo

- El usuario confirmó la instalación inicial del entorno de trabajo y la primera subida del repositorio a GitHub.
- Se realizaron y revisaron ejercicios de variables, tipos, `input()`, condicionales, bucles `while` y `for`, y funciones con parámetros.

## 2026-11-05 — Planificación inicial

**Estado:** proyecto definido; todavía no hay implementación funcional.

- Definido el objetivo de crear un asistente IA local.
- Identificadas las áreas de aprendizaje.
- Registrado el nivel inicial y la disponibilidad semanal.
- Elegida provisionalmente la combinación Python, Ollama, SQLite y PySide6.
- Preparada la estructura inicial de documentación.

**Siguiente paso:** comenzar fundamentos de Python y diseñar el menú del gestor de conversaciones en memoria.

## Plantilla para futuras entradas

### AAAA-MM-DD — Título del avance

- **Objetivo:**
- **Qué he aprendido:**
- **Qué he implementado:**
- **Cómo lo he probado:**
- **Problemas encontrados:**
- **Soluciones aplicadas:**
- **Qué puedo explicar sin consultar apuntes:**
- **Siguiente paso:**
