def menu() -> str:
    """
    Devuelve la lista de opciones.
    """
    options = ("Buscar país", "Filtrar países", "Ordenar países", "Mostrar estadísticas", "Salir")
    print("\n" + "="*10 + " Gestión de Datos de Países " + "="*10 )
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    print("="*50)
    return

def select_option():
    """
    Solicita la opción.\n
    Retorna:\n
    int: Número de la opción elegida.
    """
    option = input("Ingrese una opcion: ")
    if not option.isdigit():
        print("⚠️   Ingrese un numero entero")
        return None
    try:
        option = int(option)
    except ValueError:
        print("⚠️   Ingrese un numero válido")
        return None
    finally:
        return option