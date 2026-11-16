# Arquitectura prevista

**Estado:** arquitectura objetivo en planificación; existe un primer gestor de conversaciones en consola, sin base de datos ni conexión a IA.

## Implementación actual — consola (16/11/2026)

- [`codigo/Conversaciones.py`](../codigo/Conversaciones.py) contiene un prototipo monolítico y pedagógico en Python.
- El menú recibe datos con `input()` y llama a funciones de creación, búsqueda y mensajes.
- Los datos residen en una lista de diccionarios; no hay persistencia al cerrar el programa.
- Hay validación básica de identificadores (`try/except ValueError`), ID duplicado y conversación inexistente.
- **No están implementados todavía** SQLite, Ollama, cliente LLM, interfaz gráfica, voz ni herramientas.

La separación en módulos es un objetivo posterior; no confundir el esquema siguiente con arquitectura ya programada.

## 1. Idea general

La aplicación tendrá componentes separados:

- Interfaz: muestra mensajes y recibe entradas del usuario.
- Orquestador: coordina la conversación y los componentes.
- Cliente LLM: se comunica con Ollama.
- Persistencia: guarda conversaciones, mensajes y preferencias.
- Herramientas: ejecutan acciones expresamente permitidas.
- Voz: convierte voz en texto y texto en voz, cuando se implemente.

## 2. Flujo básico previsto

1. El usuario escribe un mensaje en la interfaz.
2. La aplicación valida la entrada.
3. El sistema recupera el contexto necesario.
4. El cliente envía la conversación al modelo local.
5. El modelo devuelve una respuesta.
6. La aplicación guarda el intercambio.
7. La interfaz muestra la respuesta.

## 3. Diagrama lógico

```text
Usuario
  |
  v
Interfaz gráfica (futura)
  |
  v
Orquestador de conversación
  |             |
  v             v
Persistencia   Cliente LLM
(SQLite)       |
               v
             Ollama
               |
               v
          Modelo local

Orquestador
  |
  v
Herramientas autorizadas (fase posterior)
```

## 4. Organización futura del código

La estructura concreta se decidirá cuando exista el primer prototipo. Una posible evolución:

```text
codigo/
  main.py
  interfaz/
  aplicacion/
  ia/
  persistencia/
  herramientas/
  voz/
  configuracion/
```

No crear todos estos directorios vacíos por adelantado. Se incorporarán cuando haya una necesidad real.

## 5. Reglas de diseño

- La interfaz no debe contener consultas SQL ni llamadas directas al modelo.
- La comunicación con Ollama debe estar encapsulada en un cliente.
- La persistencia debe estar separada de la lógica de conversación.
- Las herramientas deben tener parámetros explícitos y validados.
- Los errores deben propagarse de forma controlada y mostrarse de manera comprensible.
- Las operaciones lentas no deben bloquear la interfaz.

## 6. Seguridad

El modelo no tendrá acceso libre al sistema operativo. Solo podrá solicitar herramientas definidas por la aplicación. Cada herramienta validará los parámetros y aplicará permisos. Las acciones destructivas o externas requerirán confirmación del usuario.
