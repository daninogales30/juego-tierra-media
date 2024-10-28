from parte_dani.parte_dani import establecer_relaciones, mostrar_personajes, cambiar_localizacion
from parte_dario.parte3_dario import agregar_personajes, añadir_equipamiento, equipar_arma, simular_batalla

facciones = ["La Comunidad del Anillo", "Mordor", "Isengard", "Rivendel", "Lothlórien"]
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
                    añadir_equipamiento()
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
                    buscar_personajes_equipamiento()
                case 9:
                    mostrar_personajes()
                case 10:
                    print("Saliendo del juego")
                    es_valido = False
        except ValueError as e:
            print(f"Error: {e}")


def listar_personajes_faccion():
    faccion = input("Inserte la facción:")
    if faccion.lower() in facciones:
        for personaje in faccion:
            print(personaje)
    else:
        raise ValueError("Esa faccion no existe")



def buscar_personajes_equipamiento():
    print("Buscando personajes por equipamiento...")


menu()