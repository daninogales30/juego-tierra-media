from parte_dario.parte3_dario import armas

equipamiento_lista = []
relaciones_lista = []
personajes = {}
ubicaciones = ['Rivendel', 'Hobbiton', 'Minas Tirith', 'Mordor', 'Isengard', 'Bosque Negro', 'Lothlórien']


def is_nombre(nombre):
    while nombre.lower() not in personajes:
        nombre = input("Ingrese el nombre del personaje: ")
        if nombre.lower() not in personajes:
            print(f"El personaje con nombre {nombre} no existe")

    return nombre

def is_ubicacion(ubicacion):
    while ubicacion.lower() not in ubicaciones:
        ubicacion = input("Ingrese el ubicacion del personaje: ")
        if ubicacion.lower() not in ubicaciones:
            print("La ubicacion no existe")

def is_arma(arma):
    while arma.lower() not in armas:
        arma = input("Ingrese el arma del personaje: ")
        if arma.lower() not in armas:
            print("El arma no existe")

def agregar_personajes():
    nombre = input("Ingrese el nombre del personaje: ")
    raza = input("Ingrese la raza del personaje: ")
    faccion = input("Ingrese la faccion del personaje: ")
    ubicacion = ""
    while ubicacion not in ubicaciones:
        ubicacion = input("Ingrese la ubicacion del personaje: ")
        if ubicacion not in ubicaciones:
            print("Ingrese una válida porfavor.")

    personajes[nombre] = {
        "raza": raza,
        "faccion": faccion,
        "ubicacion": ubicacion,
        "equipamiento": [],
        "relaciones": []
    }

def mostrar_personajes(personajes_diccionario):
    for nombre, datos in personajes_diccionario.items():
        print("Nombre:", nombre)
        print("Raza:", datos["raza"])
        print("Faccion:", datos["faccion"])
        print("Ubicacion:", datos["ubicacion"])

        if datos["equipamiento"]:
            print("Equipamiento:", ", ".join(datos["equipamiento"]))
        else:
            print("Equipamiento: Ninguno")

        if datos["relaciones"]:
            print("Relaciones:")
            for relacion in datos["relaciones"]:
                print(f"- Nombre: {relacion['nombre']}")
                print(f"- Raza: {relacion['tipo']}")
                print(f"- Faccion: {relacion['confianza']}")
        else:
            print(f"Sin relaciones")
        print()

def cambiar_localizacion():
    nombre_personaje = is_nombre(input("Ingrese el nombre del personaje: "))

    ubicacion_nueva = ""
    while ubicacion_nueva.lower() not in ubicaciones:
        ubicacion_nueva = input("Ingrese la nueva ubicacion del personaje: ")
        if ubicacion_nueva.lower() not in ubicaciones:
            print("Ubicacion no válida, porfavor, ingrésela de nuevo.")

    personajes[nombre_personaje]["ubicacion"] = ubicacion_nueva
    print("La ubicacion se ha cambiado correctamente")

def establecer_relaciones():
    nombre_personaje = is_nombre(input("Ingrese el nombre del personaje: "))

    nombre_personaje_relacionado = is_nombre(input("Ingrese el nombre del personaje relacionado: "))

    tipo_relacion = ""
    while tipo_relacion.lower() not in ["amigo", "enemigo", "neutral"]:
        tipo_relacion = input(f"Ingrese el tipo de relacion entre {nombre_personaje} y {nombre_personaje_relacionado}: ")
        if tipo_relacion.lower() not in ["amigo", "enemigo", "neutral"]:
            print("Este tipo de relacion no existe")

    nivel_confianza = ""
    while nivel_confianza not in range(1,11):
        nivel_confianza = int(input(f"Ingrese la nivel confianza entre {nombre_personaje} y {nombre_personaje_relacionado}: "))
        if nivel_confianza not in range(1,11):
            print("El nivel confianza no existe")

    personajes[nombre_personaje]["relaciones"] = {
        "nombre_relacionado": nombre_personaje_relacionado,
        "tipo": tipo_relacion,
        "nivel_confianza": nivel_confianza
    }


