from parte_dario.parte3_dario import *

razas_personaje =['humana', 'elfo', 'enano', 'hobbit']
facciones = ['mordor', 'riverdale', 'outerbanks', 'isengard']
personajes = {}
ubicaciones = ['rivendel', 'hobbiton', 'minas tirith', 'mordor', 'isengard', 'bosque negro', 'lothlórien']



def is_nombre(nombre):
    while nombre.lower() not in personajes:
        if nombre.lower() not in personajes:
            print(f"El personaje con nombre {nombre} no existe")

    return nombre

def is_ubicacion(ubicacion):
    while ubicacion.lower() not in ubicaciones:
        if ubicacion.lower() not in ubicaciones:
            print("La ubicacion no existe")

    return ubicacion

def is_arma(arma):
    while arma.lower() not in armas:
        if arma.lower() not in armas:
            print("El arma no existe")

    return arma

def is_faccion(faccion):
    while faccion.strip().lower() not in facciones.items().strip():
        if faccion.lower() not in facciones:
            print("La faccion no existe")

    return faccion


def is_raza(raza):
    while raza.lower() not in razas_personaje:
        print("La raza no existe")
        raza= input("Ingrese nuevamente la raza: ")

    return raza

def agregar_personajes():
    nombre = input("Ingrese el nombre del personaje: ")
    raza = input("Ingrese la raza del personaje: ")
    is_raza(raza)

    faccion = input("Ingrese la faccion del personaje")
    is_faccion(faccion)
    ubicacion = input("Ingrese la ubicacion del personaje")
    is_ubicacion(ubicacion)

    personajes[nombre] = {
        "raza": raza.lower(),
        "faccion": faccion.lower(),
        "ubicacion": ubicacion.lower(),
        "equipamiento": [],
        "relaciones": []
    }

def mostrar_personajes(personajes_diccionario):
    if not personajes_diccionario:
        print("Esta vacío")

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
    nombre_personaje = ""
    is_nombre(nombre_personaje)

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


