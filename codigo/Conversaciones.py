"""Primer prototipo del gestor de conversaciones de MiAsistenteIA.

Las conversaciones se guardan solo en memoria. La persistencia con SQLite
se incorporará en una etapa posterior.
"""

conversaciones = []


def buscarConversacion(conversaciones, identificador):
    for conversacion in conversaciones:
        if conversacion["id"] == identificador:
            return conversacion
    return None


def crear_conversacion(conversaciones, identificador, titulo):
    if identificador is None:
        print("El identificador no es válido")
        return None
    if buscarConversacion(conversaciones, identificador) is not None:
        print("La conversación ya existe")
        return None

    conversacion = {"id": identificador, "titulo": titulo, "mensajes": []}
    conversaciones.append(conversacion)
    return conversacion


def mostrar_conversacion(conversacion):
    if conversacion is None:
        print("La conversación no existe")
    else:
        for clave, valor in conversacion.items():
            print(clave, ":", valor)


def mostrar_conversaciones(conversaciones):
    for conversacion in conversaciones:
        print(conversacion)


def agregar_mensaje(conversaciones, identificador, texto):
    conversacion = buscarConversacion(conversaciones, identificador)
    if conversacion is None:
        print("La conversación no existe, inténtalo de nuevo")
        return False
    conversacion["mensajes"].append(texto)
    print("Mensaje guardado")
    return True


def mostrar_mensajes(conversaciones, identificador):
    conversacion = buscarConversacion(conversaciones, identificador)
    if conversacion is None:
        print("La conversación no existe")
    elif len(conversacion["mensajes"]) == 0:
        print("La conversación", conversacion["id"], "está vacía")
    else:
        print("Mensajes de la conversación:", conversacion["id"])
        for numero, mensaje in enumerate(conversacion["mensajes"], start=1):
            print(numero, ".", mensaje)


def pedir_entero():
    try:
        return int(input("Cuál es el ID a introducir: "))
    except ValueError:
        print("Error: debes introducir un número entero")
        return None


def mostrar_menu():
    print("==== MI ASISTENTE IA ====")
    print("1. Crear conversación")
    print("2. Añadir mensaje")
    print("3. Listar conversaciones")
    print("4. Mostrar mensajes")
    print("5. Salir")


def ejecutar_menu(conversaciones):
    opcion = ""
    while opcion != "5":
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            identificador = pedir_entero()
            if identificador is not None:
                titulo = input("Introduce el título de la nueva conversación: ")
                crear_conversacion(conversaciones, identificador, titulo)

        elif opcion == "2":
            identificador = pedir_entero()
            if identificador is not None:
                if buscarConversacion(conversaciones, identificador) is not None:
                    texto = input("Pregunta a 02: ")
                    agregar_mensaje(conversaciones, identificador, texto)
                else:
                    print("La conversación no existe")

        elif opcion == "3":
            mostrar_conversaciones(conversaciones)

        elif opcion == "4":
            identificador = pedir_entero()
            if identificador is not None:
                mostrar_mensajes(conversaciones, identificador)

        elif opcion == "5":
            print("Has salido")

        else:
            print("Opción no válida")


if __name__ == "__main__":
    ejecutar_menu(conversaciones)
