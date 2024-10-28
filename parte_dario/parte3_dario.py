from parte_dani.parte_dani import *
from parte_jesus.parte_jesus import *

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


def anadir_equipamiento():
    nombre_personaje = is_nombre(input("Indique el nombre del personaje"))

    print("Añade un arma al personaje si es que el arma existe")

    nombre_arma = is_arma((input("Indique el nombre del arma")))

    personajes[nombre_personaje]["equipamiento"].append(armas[nombre_arma])
    print(f"{nombre_arma} ha sido añadido al personaje: {nombre_personaje}")

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