from parte_dario.parte3_dario import *

razas_personaje =['humana', 'elfo', 'enano', 'hobbit']
facciones = ['mordor', 'riverdale', 'outerbanks', 'isengard']
personajes = {}
ubicaciones = ['rivendel', 'hobbiton', 'minastirith', 'mordor', 'isengard', 'bosquenegro', 'lothlórien']



def is_nombre(nombre):
    while nombre.lower().strip() not in personajes.keys():
        print("El nombre no existe")
        nombre = input("Ingrese el nombre: ")

    return nombre

def is_ubicacion(ubicacion):
    while ubicacion.lower() not in ubicaciones:
        print("El ubicacion no existe")
        ubicacion = input("Ingrese nuevamente la ubicación: ")

    return ubicacion

def is_arma(arma):
    while arma.lower() not in armas:
        print("El arma no existe")
        arma = input("Ingrese nuevamente la faccion: ")

    return arma

def is_faccion(faccion):
    while faccion.strip().lower() not in facciones:
        print("La faccion no existe")
        faccion = input("Ingrese nuevamente la faccion: ")

    return faccion


def is_raza(raza):
    while raza.lower() not in razas_personaje:
        print("La raza no existe")
        raza= input("Ingrese nuevamente la raza: ")

    return raza

def agregar_personajes():
    nombre = input("Ingrese el nombre del personaje: ").strip().lower()
    raza = is_raza(input("Ingrese la raza del personaje: "))
    faccion = is_faccion(input("Ingrese la faccion del personaje: "))
    ubicacion = is_ubicacion(input("Ingrese la ubicacion del personaje: "))


    personajes[nombre] = {
        "raza": raza.lower(),
        "faccion": faccion.lower(),
        "ubicacion": ubicacion.lower(),
        "equipamiento": [],
        "relaciones": []
    }
    print("Personaje añadido\n")

def mostrar_personajes(personajes_diccionario):
    if not personajes_diccionario:
        print("Esta vacío")

    for nombre, datos in personajes_diccionario.items():
        print("Nombre:", nombre.capitalize())
        print("Raza:", datos["raza"].capitalize())
        print("Faccion:", datos["faccion"].capitalize())
        print("Ubicacion:", datos["ubicacion"].capitalize())

        if datos["equipamiento"]:
            print("Equipamiento:", ", ".join(datos["equipamiento"]))
        else:
            print("Equipamiento: Ninguno")

        if datos["relaciones"]:
            print("Relaciones:")
            for relacion in datos["relaciones"]:
                print(f"- Nombre: {relacion['nombre_relacionado']}")
                print(f"- Raza: {relacion['tipo']}")
                print(f"- Faccion: {relacion['nivel_confianza']}\n")
        else:
            print(f"Sin relaciones")
        print()

def cambiar_localizacion():
    nombre_personaje = is_nombre(input("Ingrese el nombre del personaje: "))

    ubicacion_nueva = is_ubicacion(input("Ingrese la nueva ubicacion: "))

    try:
        personajes[nombre_personaje]["ubicacion"] = ubicacion_nueva
        print("La ubicacion se ha cambiado correctamente\n")
    except KeyError:
        print(f"Error: El personaje '{nombre_personaje}' no existe en la lista.")


def establecer_relaciones():
    nombre_personaje = is_nombre(input("Ingrese el nombre del personaje: "))

    nombre_personaje_relacionado = is_nombre(input("Ingrese el nombre del personaje relacionado: "))

    tipo_relacion = input(f"Ingrese el tipo de relacion entre {nombre_personaje} y {nombre_personaje_relacionado}: ")
    while tipo_relacion.lower() not in ["amigo", "enemigo", "neutral"]:
        print("Tipo de relacion no existe")
        tipo_relacion = input(f"Ingrese el tipo de relacion entre {nombre_personaje} y {nombre_personaje_relacionado}: ")

    nivel_confianza = int(input(f"Ingrese la nivel confianza entre {nombre_personaje} y {nombre_personaje_relacionado}: "))
    while nivel_confianza not in range(1,11):
        print("El nivel confianza no existe")
        nivel_confianza = int(input(f"Ingrese la nivel confianza entre {nombre_personaje} y {nombre_personaje_relacionado}: "))

    personajes[nombre_personaje]["relaciones"].append({
        "nombre_relacionado": nombre_personaje_relacionado,
        "tipo": tipo_relacion,
        "nivel_confianza": nivel_confianza
    })

    personajes[nombre_personaje_relacionado]["relaciones"].append({
        "nombre_relacionado": nombre_personaje,
        "tipo": tipo_relacion,
        "nivel_confianza": nivel_confianza
    })

    print("Relacion establecida con éxito")


