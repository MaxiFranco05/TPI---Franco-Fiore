from utils.menu import menu, select_option
from utils.csv_options import read_csv, dev_options
from utils.searcher import search_pais
from utils.filter import filter
from utils.sorter import sorter
from utils.statistics import statistics

def main():
    path = "data/paises_mundo.csv"
    data_csv = read_csv(path)
    while True:
        menu()
        option = select_option()
        if not data_csv and option not in (5, 1):
            print("⚠️  Primero ingrese datos al CSV o intente con uno nuevo.")
            option = 5

        match option:
            case 1:
                search_pais(data_csv)
            case 2:
                filter(data_csv)
            case 3:
                sorter(data_csv)
            case 4:
                statistics(data_csv)
            case 5:
                dev_options(data_csv, path)
            case 6:
                print("👋  Gracias por usar el sistema de paises. ¡Hasta pronto!")
                break 
            case _:
                print("⚠️  Opción inválida. Intente de nuevo")
        input("Presione Enter para continuar...")

main()