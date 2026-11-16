# Documento maestro — MiAsistenteIA

- **Versión del documento:** 1.1
- **Estado:** primer prototipo de consola completado. El asistente de IA sigue en planificación.
- **Fecha de referencia del avance:** 16/11/2026

## Estado de implementación — 16/11/2026

Se ha completado una primera práctica funcional **sin modelo de IA**: [`codigo/Conversaciones.py`](../codigo/Conversaciones.py).

- Crear conversaciones con identificador único y título.
- Añadir mensajes de texto a una conversación existente.
- Buscar, listar y consultar conversaciones y mensajes mediante un menú de consola.
- Tratar identificadores no numéricos con `try/except ValueError` y evitar operaciones con `None`.
- Comprobar el comportamiento con entradas válidas e inválidas en pruebas manuales.

**Alcance:** los datos se guardan en memoria durante la ejecución. SQLite, las APIs REST, Ollama, la interfaz gráfica, la voz y la automatización siguen pendientes.

## 1. Visión general

MiAsistenteIA es un proyecto personal de aprendizaje cuyo objetivo es desarrollar, paso a paso, un asistente de inteligencia artificial de escritorio que pueda ejecutarse principalmente en local.

La meta no es entrenar un modelo de lenguaje desde cero. Se utilizarán modelos existentes y herramientas de código abierto, y el trabajo de desarrollo consistirá en diseñar la aplicación que los conecta con una interfaz, memoria, voz y herramientas.

## 2. Objetivos

### Objetivo principal

Construir una aplicación de escritorio para Windows que permita conversar con un modelo LLM local y evolucionar hacia un asistente personal con memoria persistente y capacidades controladas.

### Objetivos de aprendizaje

- Consolidar Python desde los fundamentos.
- Reforzar bases de datos relacionales y aprender SQLite.
- Comprender HTTP, APIs REST y JSON.
- Aprender a ejecutar y consultar modelos LLM en local.
- Diseñar una aplicación modular.
- Crear interfaces gráficas de escritorio.
- Incorporar procesamiento de voz.
- Aprender a integrar herramientas de automatización de forma segura.
- Practicar Git, GitHub, pruebas y documentación.

## 3. Funcionalidades previstas

Las funcionalidades se desarrollarán por etapas. No se consideran implementadas hasta que exista código probado y documentado.

### Primera versión funcional (MVP)

- Ejecutarse en Windows.
- Conectarse a un modelo local mediante Ollama.
- Permitir enviar mensajes y mostrar respuestas.
- Mantener el contexto de una conversación durante la sesión.
- Gestionar errores de conexión y mostrar mensajes comprensibles.

### Evolución posterior

- Guardar conversaciones en SQLite.
- Recuperar conversaciones anteriores.
- Incorporar una interfaz gráfica propia.
- Incorporar entrada y salida de voz.
- Gestionar preferencias y memoria persistente.
- Analizar imágenes o capturas de pantalla mediante un modelo compatible.
- Ejecutar herramientas autorizadas, como abrir aplicaciones o consultar archivos.

## 4. Estado inicial del usuario

Información confirmada al iniciar la planificación:

- Tiene experiencia previa con Java y programación orientada a objetos.
- Está aprendiendo C# y .NET, incluyendo interfaces gráficas.
- Ha realizado automatizaciones prácticas con Python, pero se considera principiante en el lenguaje.
- Comenzará a estudiar Python en clase en menos de un mes desde la fecha de esta planificación.
- Tiene conocimientos de SQL/MySQL y SQL Server, pero identifica carencias en bases de datos.
- No ha trabajado todavía con APIs REST.
- No ha instalado ni utilizado Ollama, según su última actualización.
- Puede dedicar aproximadamente 5-7 horas semanales.

No asumir que estos datos siguen vigentes indefinidamente: confirmar cambios en las revisiones.

## 5. Tecnologías previstas

La selección inicial es una propuesta, no una decisión irreversible.

| Área | Tecnología prevista | Motivo |
|---|---|---|
| Lenguaje principal | Python | Ecosistema de IA y automatización |
| Modelo local | Ollama | Ejecutar modelos y ofrecer una API local |
| Comunicación | HTTP, REST y JSON | Conectar la aplicación con el modelo |
| Base de datos | SQLite | Memoria local sencilla y sin servidor |
| Interfaz | PySide6 | Aplicación de escritorio en Python |
| Voz a texto | Whisper o faster-whisper | Reconocimiento de voz |
| Texto a voz | Piper u otra alternativa compatible | Respuestas habladas |
| Versionado | Git y GitHub | Historial y respaldo del código |

Las bibliotecas concretas se elegirán cuando se llegue a cada etapa y se comprobará su compatibilidad con el equipo.

## 6. Plan de desarrollo

1. Fundamentos de Python.
2. Fundamentos de bases de datos y SQLite.
3. HTTP, APIs REST y JSON.
4. Ollama y primer chatbot local.
5. Arquitectura e interfaz gráfica.
6. Memoria e historial persistente.
7. Voz.
8. Herramientas y automatización segura.
9. Integración, pruebas y documentación final.

El orden puede ajustarse según el progreso y el contenido de las clases.

## 7. Criterios de calidad

- El código debe estar dividido en módulos con responsabilidades claras.
- Las operaciones de entrada/salida y llamadas al modelo deben gestionar errores.
- La interfaz no debe bloquearse mientras se espera una respuesta.
- Las conversaciones y preferencias deben almacenarse de forma controlada.
- Las operaciones destructivas o sensibles requieren confirmación.
- No ejecutar directamente instrucciones arbitrarias generadas por el modelo.
- Añadir pruebas para las partes importantes.
- Mantener dependencias y pasos de instalación documentados.

## 8. Límites y seguridad

- No subir claves, contraseñas, tokens ni archivos `.env` reales a GitHub.
- No subir modelos de IA descargados ni bases de datos con conversaciones privadas.
- Limitar el acceso a archivos y aplicaciones a herramientas explícitamente permitidas.
- Pedir confirmación antes de borrar, sobrescribir, enviar o ejecutar acciones sensibles.
- Preferir el funcionamiento local, pero documentar cualquier servicio externo que se utilice.

## 9. Cómo se medirá el progreso

Cada avance debe incluir:

1. Qué se quería conseguir.
2. Qué conceptos se han aprendido.
3. Qué se ha implementado.
4. Cómo se ha probado.
5. Qué errores o dificultades quedan.
6. Cuál es el siguiente paso.

Una fase se considera completada cuando el usuario puede explicar el funcionamiento básico, modificar el ejemplo y demostrar que funciona.

## 10. Próximo objetivo

**Objetivo inmediato:** repasar el prototipo del gestor de conversaciones y comenzar fundamentos de bases de datos relacionales y SQLite.

Diseñar tablas `conversaciones` y `mensajes`, relacionarlas y aprender operaciones básicas para guardar y recuperar el historial entre ejecuciones. La persistencia todavía no está implementada.
