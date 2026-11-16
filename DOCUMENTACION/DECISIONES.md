# Registro de decisiones técnicas

Registrar aquí decisiones relevantes, su motivo y si siguen vigentes.

## D-001 — Python como lenguaje principal inicial

- **Estado:** aceptada para el prototipo de consola; revisable en etapas posteriores.
- **Decisión:** utilizar Python para la primera versión.
- **Motivo:** ecosistema amplio para IA local, automatización y prototipado.
- **Alternativas consideradas:** C#/.NET para la aplicación completa o una arquitectura mixta.
- **Revisión:** reconsiderar si aparecen limitaciones concretas.

## D-002 — Ollama para ejecutar modelos locales

- **Estado:** propuesta, pendiente de instalación y prueba.
- **Motivo:** ofrece una forma accesible de ejecutar modelos y comunicarse con ellos localmente.
- **Condición:** comprobar compatibilidad y rendimiento con el hardware disponible.

## D-003 — SQLite para persistencia inicial

- **Estado:** propuesta, próxima etapa de aprendizaje; no implementada.
- **Motivo:** almacenamiento local sencillo, sin necesidad de administrar un servidor de base de datos.
- **Condición:** aprender primero los fundamentos relacionales y SQL.

## D-004 — PySide6 para la interfaz

- **Estado:** propuesta.
- **Motivo:** permite desarrollar una interfaz de escritorio con Python.
- **Alternativas:** WPF con C#/.NET.
- **Revisión:** elegir definitivamente cuando llegue el bloque de interfaz.

## D-005 — Primer gestor en memoria antes de persistencia

- **Estado:** aplicada al prototipo pedagógico (16/11/2026).
- **Decisión:** practicar el gestor de conversaciones con una lista de diccionarios y funciones antes de incorporar una base de datos.
- **Motivo:** consolidar estructuras de datos, reutilización de funciones, `return`, `None` y validación de entradas.
- **Consecuencia:** los datos se pierden al terminar el proceso; SQLite queda como siguiente bloque.

## Plantilla de decisión

### D-XXX — Título

- **Estado:** propuesta / aceptada / sustituida.
- **Fecha:**
- **Contexto:**
- **Decisión:**
- **Motivos:**
- **Alternativas:**
- **Consecuencias:**
