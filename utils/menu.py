"""Menú de opciones y captura segura de la opción del usuario."""

from utils.utils import console_size

def menu() -> str:
    """
    Devuelve la lista de opciones.
    """
    # Opciones del menú principal
    options = ("Buscar país", "Filtrar países", "Ordenar países", "Mostrar estadísticas", "Opciones de Desarrollador", "Salir")
    print(" Gestión de Datos de Países ".center(console_size(), "-"))
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    print("-"*console_size())
    return

def select_option():
    """
    Solicita la opción.\n
    Retorna:\n
    int: Número de la opción elegida.
    """
    while True:
        # Solicita y valida que la opción sea numérica
        option = input("Ingrese una opcion: ")
        if not option.isdigit():
            print("⚠️  Ingrese un numero válido.")
        else:
            try:
                option = int(option)
                return option
            except ValueError:
                print("⚠️  Ingrese un numero válido")