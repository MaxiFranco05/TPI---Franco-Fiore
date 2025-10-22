from utils.utils import console_size

def menu() -> str:
    """
    Devuelve la lista de opciones.
    """
    options = ("Buscar país", "Filtrar países", "Ordenar países", "Mostrar estadísticas", "Salir")
    print(" Gestión de Datos de Países ".center(console_size(), "-"))
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    print("-"*console_size())
    #print("◠◡"*(console_size()//2))
    return

def select_option():
    """
    Solicita la opción.\n
    Retorna:\n
    int: Número de la opción elegida.
    """
    while True:
        option = input("Ingrese una opcion: ")
        if not option.isdigit():
            print("⚠️  Ingrese un numero válido.")
        else:
            try:
                option = int(option)
                return option
            except ValueError:
                print("⚠️  Ingrese un numero válido")