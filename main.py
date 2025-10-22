from utils.menu import menu, select_option
from utils.csv_options import read_csv
from utils.searcher import search_pais
from utils.filter import filter
from utils.sorter import sorter
from utils.statistics import statistics

def main():
    data_csv = read_csv("paises_mundo.csv")
    if not data_csv:
        return
    while True:
        menu()
        opcion = select_option()

        match opcion:
            case 1:
                search_pais(data_csv)
            case 2:
                filter(data_csv)
            case 3:
                sorter(data_csv)
            case 4:
                statistics(data_csv)
            case 5:
                print("👋  Gracias por usar el sistema de paises. ¡Hasta pronto!")
                break 
            case _:
                print("⚠️  Opción inválida. Intente de nuevo")
        input("Presione Enter para continuar...")

main()