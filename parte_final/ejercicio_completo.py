razas_personaje =['humana', 'elfo', 'enano', 'hobbit']
facciones = ['mordor', 'riverdale', 'outerbanks', 'isengard']
personajes = {}
ubicaciones = ['rivendel', 'hobbiton', 'minastirith', 'mordor', 'isengard', 'bosquenegro', 'lothlórien']
armas={
    "anduril":{
        "tipo": "Espada",
        "potencia": 80,
        "descripcion": "La espada legendaria de Aragorn, forjada de los fragmentos de Narsil."
    },
    "arcodegaladriel": {
        "tipo": "Arco",
        "potencia": 70,
        "descripcion":"El arco de Legolas, dado como un regalo por la dama Galadriel."
    },
    "hachadegimli": {
        "tipo": "Hacha",
        "potencia": 75,
        "descripcion": "El arma favorita del enano Gimli, eficaz en combate cuerpo a cuerpo."
    },
    "dagadefrodo": {
        "tipo": "Daga",
        "potencia": 40,
        "descripcion": "Daga élfica que Frodo lleva durante su viaje."
    },
    "baculodesaruman": {
        "tipo": "Bastón",
        "potencia": 90,
        "descripcion": "Un bastón de poder usado por el mago Saruman."
    },
    "anillounico": {
        "tipo": "Objeto especial",
        "potencia": 100,
        "descripcion": "El Anillo creado por Sauron para gobernar todos los demás."
    },
    "espadadeboromir": {
        "tipo": "Espada",
        "potencia": 70,
        "descripcion": "El arma usada por Boromir, capitán de Gondor."
    }
}


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
    arma_sin_espacios = arma.replace(" ","")
    while arma_sin_espacios not in armas:
        print("El arma no existe")
        arma = input("Ingrese nuevamente el arma: ")
        arma_sin_espacios = arma.replace(" ","")

    return arma_sin_espacios

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
            equipamiento_descripciones = [f"{arma['tipo']} - {arma['descripcion']}" for arma in datos["equipamiento"]]
            print("Equipamiento:", ", ".join(equipamiento_descripciones))
        else:
            print("Equipamiento: Ninguno")

        if datos["relaciones"]:
            print("Relaciones:")
            for relacion in datos["relaciones"]:
                print(f"- Nombre: {relacion['nombre_relacionado']}")
                print(f"- Raza: {relacion['tipo']}")
                print(f"- Faccion: {relacion['nivel_confianza']}\n")
        else:
            print("Sin relaciones")
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

def anadir_equipamiento():
    nombre_personaje = is_nombre(input("Indique el nombre del personaje: "))

    print("Añade un arma al personaje si es que el arma existe")

    nombre_arma = is_arma((input("Indique el nombre del arma: ")))

    personajes[nombre_personaje]["equipamiento"].append(armas[nombre_arma])
    print(f"El arma ha sido añadido al personaje: {nombre_personaje}")

def equipar_arma():
    nombre_personaje = ""
    is_nombre(nombre_personaje)

    nombre_arma = ""
    is_arma(nombre_arma)

    if armas[nombre_arma] not in personajes[nombre_personaje]["equipamiento"]:
        raise ValueError(f"Este arma no esta en el equipamiento del personaje {nombre_personaje}")

    personajes[nombre_personaje]["equipamiento"]=armas[nombre_arma]
    print(f"El personaje {nombre_personaje} ha cambiado de arma {armas[nombre_arma]}")


def simular_batalla():
    personaje1=""
    personaje2=""
    arma1=personajes[personaje1]["equipamiento"]
    arma2=personajes[personaje2]["equipamiento"]
    if not arma1 or not arma2:
        print("Ambos personajes necesitan un arma para luchar")
    potencia1=arma1["potencia"]
    potencia2=arma2["potencia"]
    probabilidad_ganar1=potencia1/(potencia1+potencia2)
    probabilidad_ganar2 = potencia2 / (potencia2 + potencia1)
    if probabilidad_ganar1 > probabilidad_ganar2:
        ganador = personaje1
    elif probabilidad_ganar2 > probabilidad_ganar1:
        ganador = personaje2
    print(f"La batalla acaba de empezar entre {personaje1} y {personaje2}")
    print(f"{personaje1}con {arma1['tipo']}vs {personaje2}con {arma2['tipo']}")
    print(f"Y el ganador es:")

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
                    listar_personajes_faccion(personajes)
                case 8:
                    buscar_personajes_equipamiento(armas)
                case 9:
                    mostrar_personajes(personajes)
                case 10:
                    print("Saliendo del juego")
                    es_valido = False
        except ValueError as e:
            print(f"Error: {e}")


def listar_personajes_faccion(personajes):
    faccion = is_faccion(input("Ingrese la facción que desea listar: "))

    personajes_faccion = [nombre for nombre, datos in personajes.items() if datos["faccion"] == faccion]

    if personajes_faccion:
        print(f"Personajes de la facción '{faccion.capitalize()}':")
        for nombre in personajes_faccion:
            print(nombre.capitalize())

    else:
        print(f"No hay personajes en la facción '{faccion}'.")

def buscar_personajes_equipamiento(armas):
    nombre_arma = input("Ingrese el nombre del arma que desea buscar en los personajes: ")


    if nombre_arma not in armas:
        print(f"Error: El arma '{nombre_arma}' no existe.")
        return

    personajes_con_arma = [nombre for nombre, datos in personajes.items()
                           if any(equipo['tipo'] == armas[nombre_arma]["tipo"] for equipo in datos["equipamiento"])]

    if personajes_con_arma:
        print(f"Personajes que tienen el arma '{nombre_arma}':")
        for nombre in personajes_con_arma:
            print("- " + nombre)
    else:
        print(f"No se encontraron personajes con el arma '{nombre_arma}'.")

menu()
