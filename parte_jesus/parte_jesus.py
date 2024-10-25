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
            opcion = int(input("Seleccione una opcion: "))
            if (opcion < 1 and opcion > 10):
                raise ValueError("Opcion no válida")
            else:
                match opcion:
                    case 1:
                        return
                    case 2:
                        return
                    case 3:
                        return
                    case 4:
                        return
                    case 5:
                        return
                    case 6:
                        return
                    case 7:
                        listar_personajes_faccion()
                    case 8:
                        buscar_personajes_equipamiento()
                    case 9:
                        return
                    case 10:
                        print("Saliendo del juego")
                        es_valido = False
        except ValueError as e:
            print(f"Error: {e}")

def listar_personajes_faccion():
    pass

def buscar_personajes_equipamiento():
    pass

