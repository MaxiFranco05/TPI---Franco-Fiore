"""Aplicación de consola para gestionar datos de países.

Coordina el flujo principal del programa: muestra el menú, solicita la
opción del usuario y delega en utilidades de búsqueda, filtrado,
ordenamiento, estadísticas y opciones de desarrollo.

Notas:
- Requiere el archivo `data/paises_mundo.csv`.
- Si no existe, puede ser creado por las utilidades correspondientes.
"""

from utils.menu import menu, select_option
from utils.csv_options import read_csv, dev_options
from utils.searcher import search_pais
from utils.filter import filter
from utils.sorter import sorter
from utils.statistics import statistics
from utils.utils import clear_console

def main():
    path = "data/paises_mundo.csv"
    # Carga inicial de datos desde CSV
    data_csv = read_csv(path)
    while True:
        # Muestra el menú principal y solicita la opción
        menu()
        option = select_option()
        if not data_csv and option not in (5, 1):
            print("⚠️  Primero ingrese datos al CSV o intente con uno nuevo.")
            option = 5

        match option:
            case 1:  # Buscar país
                search_pais(data_csv)
            case 2:  # Filtrar países
                filter(data_csv)
            case 3:  # Ordenar países
                sorter(data_csv)
            case 4:  # Mostrar estadísticas
                statistics(data_csv)
            case 5:  # Opciones de desarrollador (Modificaciones de CSV)
                dev_options(data_csv, path)
            case 6:  # Salida
                print("👋  Gracias por usar el sistema de paises. ¡Hasta pronto!")
                break 
            case _:
                print("⚠️  Opción inválida. Intente de nuevo")
        input("Presione Enter para continuar...")
        clear_console()

if __name__ == "__main__":
    main()