from parte_dani.parte_dani import *
from parte_dario.parte3_dario import *

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


def listar_personajes_faccion():
    faccion = is_faccion(input("Ingrese la facción que desea listar: "))

    personajes_faccion = list(filter(lambda nombre: personajes[nombre]["faccion"] == faccion, personajes))

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
        print(f"Personajes que tienen el arma '{nombre_arma}':")
        for nombre in personajes_con_arma:
            print("- " + nombre)
    else:
        print(f"No se encontraron personajes con el arma '{nombre_arma}'.")