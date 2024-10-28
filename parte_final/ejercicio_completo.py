

razas_personaje =['humana', 'elfo', 'enano', 'hobbit']
facciones = ['mordor', 'riverdale', 'outerbanks', 'isengard']
personajes = {}
ubicaciones = ['rivendel', 'hobbiton', 'minastirith', 'mordor', 'isengard', 'bosquenegro', 'lothlórien']
armas={
    "anduril":{
        "nombre": "Anduril",
        "tipo": "Espada",
        "potencia": 80,
        "descripcion": "La espada legendaria de Aragorn, forjada de los fragmentos de Narsil."
    },
    "arcodegaladriel": {
        "nombre": "Arco de Galadriel",
        "tipo": "Arco",
        "potencia": 70,
        "descripcion":"El arco de Legolas, dado como un regalo por la dama Galadriel."
    },
    "hachadegimli": {
        "nombre": "Hacha de Gimli",
        "tipo": "Hacha",
        "potencia": 75,
        "descripcion": "El arma favorita del enano Gimli, eficaz en combate cuerpo a cuerpo."
    },
    "dagadefrodo": {
        "nombre": "Daga de frodo",
        "tipo": "Daga",
        "potencia": 40,
        "descripcion": "Daga élfica que Frodo lleva durante su viaje."
    },
    "baculodesaruman": {
        "nombre": "Baculo de Saruman",
        "tipo": "Bastón",
        "potencia": 90,
        "descripcion": "Un bastón de poder usado por el mago Saruman."
    },
    "anillounico": {
        "nombre": "Anillo Unico",
        "tipo": "Objeto especial",
        "potencia": 100,
        "descripcion": "El Anillo creado por Sauron para gobernar todos los demás."
    },
    "espadadeboromir": {
        "nombre": "Espada de Borimir",
        "tipo": "Espada",
        "potencia": 70,
        "descripcion": "El arma usada por Boromir, capitán de Gondor."
    }
}


def is_nombre(nombre):
    while nombre.lower() not in personajes:
        print("El nombre no existe o está vacío. Intente nuevamente.")
        nombre = input("Ingrese el nombre: ")

    return nombre

def is_ubicacion(ubicacion):
    while ubicacion.lower() not in ubicaciones:
        print("El ubicacion no existe")
        ubicacion = input("Ingrese nuevamente la ubicación: ")

    return ubicacion

def is_arma(arma):
    arma_sinespacios = arma.replace(" ", "").lower()
    while arma_sinespacios not in armas:
        print("El arma no existe.")
        arma_sinespacios = input("Ingrese nuevamente el arma: ").replace(" ","")

    return arma_sinespacios

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
    while nombre=="":
        nombre = input("Ingrese el nombre del personaje correctamente: ").strip().lower()

    raza = is_raza(input("Ingrese la raza del personaje: "))
    faccion = is_faccion(input("Ingrese la faccion del personaje: "))
    ubicacion = is_ubicacion(input("Ingrese la ubicacion del personaje: "))


    personajes[nombre] = {
        "raza": raza.lower(),
        "faccion": faccion.lower(),
        "ubicacion": ubicacion.lower(),
        "equipamiento": [],
        "relaciones": [],
        "arma_equipada": ""
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
            print("Equipamiento:")
            for equipamiento in datos["equipamiento"]:
                print(f"    -Nombre: {equipamiento['nombre']}")
                print(f"    -Tipo: {equipamiento['tipo']}")
                print(f"    -Potencia: {equipamiento['potencia']}")
                print(f"    -Descripcion: {equipamiento['descripcion']}\n")

        else:
            print("Equipamiento: Ninguno")

        if datos["relaciones"]:
            print("Relaciones:")
            for relacion in datos["relaciones"]:
                print(f"    -Nombre: {relacion['nombre_relacionado']}")
                print(f"    -Raza: {relacion['tipo']}")
                print(f"    -Faccion: {relacion['nivel_confianza']}\n")
        else:
            print("Relaciones: Ninguno")

        if datos["arma_equipada"]:
            print("Arma equipada:", datos["arma_equipada"]["nombre"], "\n")
        print()

def cambiar_localizacion():
    nombre_personaje = input("Ingrese el nombre del personaje: ").lower()
    if nombre_personaje not in personajes:
        raise ValueError("Nombre no existe")

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

def anadir_equipamiento():
    nombre_personaje = is_nombre(input("Indique el nombre del personaje: "))

    print("Añade un arma al personaje si es que el arma existe")

    nombre_arma = is_arma((input("Indique el nombre del arma: ")))

    personajes[nombre_personaje]["equipamiento"].append({
        'nombre': armas[nombre_arma]['nombre'],
        'tipo': armas[nombre_arma]['tipo'],
        'potencia': armas[nombre_arma]['potencia'],
        'descripcion': armas[nombre_arma]['descripcion'],
    })
    print(f"El arma: {armas[nombre_arma]['nombre']} ha sido añadido al personaje: {nombre_personaje.capitalize()}")

def equipar_arma():
    nombre_personaje = is_nombre(input("Indique el nombre del personaje: "))
    esta_inventario = True
    nombre_arma = is_arma(input("Indique el nombre del arma: "))
    while esta_inventario:
        for equipamiento in personajes[nombre_personaje]["equipamiento"]:
            if equipamiento["nombre"] == armas[nombre_arma]['nombre']:
                personajes[nombre_personaje]["arma_equipada"] = armas[nombre_arma]
                print(f"El personaje {nombre_personaje} ha equipado el arma: {armas[nombre_arma]['nombre']}\n")
                esta_inventario = False

        raise ValueError(f"El arma {armas[nombre_arma]["nombre"]} no está en el inventario de {nombre_personaje.capitalize()}")


    print(f"El personaje {nombre_personaje} no tiene ese arma\n")

def simular_batalla():
    personaje1= is_nombre(input("Introduzca el nombre del primer personaje: "))
    arma1 = personajes[personaje1]["arma_equipada"]
    if arma1 == "":
        raise ValueError(f"El personaje {personaje1} no tiene arma equipada")

    personaje2= is_nombre(input("Introduzca el nombre del segundo personaje: "))
    arma2 = personajes[personaje2]["arma_equipada"]
    if arma2 == "":
        raise ValueError(f"El personaje {personaje2} no tiene arma equipada")

    potencia1=armas[arma1]["potencia"]
    potencia2=armas[arma2]["potencia"]

    probabilidad_ganar1=potencia1/(potencia1+potencia2)
    probabilidad_ganar2 = potencia2 / (potencia2 + potencia1)

    if probabilidad_ganar1 > probabilidad_ganar2:
        ganador = personaje1
    elif probabilidad_ganar2 > probabilidad_ganar1:
        ganador = personaje2

    print(f"El ganador \n")


def menu():
    es_valido = True
    while es_valido:
        try:
            print("""--- Menú de Gestión de la Tierra Media ---
            1. Registrar un nuevo personaje
            2. Añadir equipamiento a un personaje
            3. Equipar un arma a un personaje
            4. Establecer relaciones entre personajes
            5. Mover un personaje a una nueva localización
            6. Simular una batalla entre dos personajes
            7. Listar personajes por facción
            8. Buscar personajes por equipamiento
            9. Mostrar todos los personajes
            10. Salir""")

            opcion = int(input("Seleccione una opción: "))
            if opcion < 1 or opcion > 10:
                raise ValueError("Opción no válida")

            # Bloque match-case
            match opcion:
                case 1:
                    agregar_personajes()
                case 2:
                    anadir_equipamiento()
                case 3:
                    equipar_arma()
                case 4:
                    establecer_relaciones()
                case 5:
                    cambiar_localizacion()
                case 6:
                    simular_batalla()
                case 7:
                    listar_personajes_faccion()
                case 8:
                    buscar_personajes_equipamiento(armas)
                case 9:
                    mostrar_personajes(personajes)
                case 10:
                    confirmacion = input("¿Está seguro que desea salir? (s/n): ").strip().lower()
                    if confirmacion == 's':
                        print("Saliendo del juego...")
                        es_valido = False
        except ValueError as e:
            print(f"Error: {e}")

def listar_personajes_faccion():
    faccion = is_faccion(input("Ingrese la facción que desea listar: "))

    personajes_faccion = [nombre for nombre, datos in personajes.items() if datos["faccion"] == faccion]

    if personajes_faccion:
        print(f"Personajes de la facción '{faccion.capitalize()}':")
        for nombre in personajes_faccion:
            print(nombre.capitalize())

    else:
        print(f"No hay personajes en la facción '{faccion}'.")

def buscar_personajes_equipamiento(armas):
    nombre_arma = is_arma(input("Ingrese el nombre del arma que desea buscar en los personajes: "))

    personajes_con_arma = []
    for nombre, datos in personajes.items():
        for equipo in datos["equipamiento"]:
            if equipo == armas[nombre_arma]:
                personajes_con_arma.append(nombre)
                break

    if personajes_con_arma:
        print(f"Personajes que tienen el arma '{armas[nombre_arma]["nombre"]}':")
        for nombre in personajes_con_arma:
            print("- " + nombre)
    else:
        print(f"No se encontraron personajes con el arma '{armas[nombre_arma]["nombre"]}'.")

menu()
