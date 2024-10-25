personajes= {}
def agregar_personajes():
    nombre = input("Ingrese el nombre del personaje: ")
    raza = input("Ingrese la raza del personaje: ")
    faccion = input("Ingrese la faccion del personaje: ")
    ubicacion = input("Ingrese la ubicacion del personaje: ")
    equipamiento = input("Ingrese el equipamiento: ")
    relaciones = input("Ingrese la relaciones: ")
    personajes[nombre] = {
        "raza": raza,
        "faccion": faccion,
        "ubicacion": ubicacion,
        "equipamiento": equipamiento,
        "relaciones": relaciones
    }
def añadir_equipamiento(nombre_personaje,nombre_arma):
    print("Añade un arma al personaje si es que el arma existe")
    if nombre_personaje in personajes:
        if nombre_arma in armas:
            personajes[nombre_personaje]["equipamiento"].append(armas[nombre_arma])
            print(f"{nombre_arma} ha sido añadido al personaje: {nombre_personaje}")

    else:
        print(f"El personaje {nombre_personaje} no existe")
def equipar_arma(nombre_personaje,nombre_arma):
    print("Equipa un arma en el inventario del personaje")
    if nombre_personaje in personajes:
        if nombre_arma in armas:
            if armas[nombre_arma] in personajes[nombre_personaje]["equipamiento"]:
                personajes[nombre_personaje]["arma equipada"]=armas[nombre_arma]
                print(f"El personaje {nombre_personaje} ha cambiado de arma {armas[nombre_arma]}")
            else:
                print(f"{nombre_personaje} no tiene arma {nombre_arma} equipada")
        else:
            print(f"El arma{nombre_arma} no existe en el diccionario de armas")
    else:
        print(f"El personaje {nombre_personaje} no existe")

def simular_batalla():
    print("Queda estoooo")
armas={
    "Andúril":{
        "tipo": "Espada",
        "potencia": 80,
        "descripcion": "La espada legendaria de Aragorn, forjada de los fragmentos de Narsil."
    },
    "Arco de Galadriel": {
        "tipo": "Arco",
        "potencia": 70,
        "descripcion":"El arco de Legolas, dado como un regalo por la dama Galadriel."
    },
    "Hacha de Gimli": {
        "tipo": "Hacha",
        "potencia": 75,
        "descripcion": "El arma favorita del enano Gimli, eficaz en combate cuerpo a cuerpo."
    },
    "Daga de Frodo": {
        "tipo": "Daga",
        "potencia": 40,
        "descripcion": "Daga élfica que Frodo lleva durante su viaje."
    },
    "Báculo de Saruman": {
        "tipo": "Bastón",
        "potencia": 90,
        "descripcion": "Un bastón de poder usado por el mago Saruman."
    },
    "Anillo Único": {
        "tipo": "Objeto especial",
        "potencia": 100,
        "descripcion": "El Anillo creado por Sauron para gobernar todos los demás."
    },
    "Espada de Boromir": {
        "tipo": "Espada",
        "potencia": 70,
        "descripcion": "El arma usada por Boromir, capitán de Gondor."
    }
}

