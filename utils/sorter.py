"""Ordenamiento de países por nombre, población o superficie.

Solicita al usuario el criterio y sentido de ordenación y muestra los
resultados con paginación cuando corresponde.
"""

from utils.utils import eliminar_tildes, console_size
from utils.paginator import paginar  

def sorter(data:list):
    """Ordenar paises por nombre, población o superficie.\n
    Parámetros:\n
        data (list): Lista de paises en diccionarios.
    Retorna:\n
        list: Lista de países ordenados.
    """
    # Campos disponibles para ordenar
    sorters = ("nombre","poblacion","superficie")
    sorter_type = input(f"Selecciona la opción por la cual ordenar {sorters}: ")
    if eliminar_tildes(sorter_type).lower().strip() not in sorters:
        return print("❌   Opción inválida.")
    # Órdenes aceptados (ascendente/descendente)
    orders = ("asc", "desc", "ascendente", "descendente")
    sorter_order = input("Selecciona el orden por el cual ordenar (Asc - Desc): ")
    if sorter_order.lower().strip() not in orders:
        return print("❌   Opción inválida.")
    print(f" Paises ordenados por {sorter_type.title()} (en orden {sorter_order.title().strip()}) ".center(console_size(), "~"))
    sort_paises(data, sorter_type, sorter_order)
    print("~"*console_size())


def sort_paises(data:list, tipo: str, orden: bool) -> list:
    """Ordenar paises por nombre, población o superficie e imprime en la consola.\n
    Parámetros:\n
        data (list): Lista de paises en diccionarios.
        tipo (str): Tipo de dato para ordenar.
        orden (str): Define el orden.
    """
    # Determina sentido de orden (reverse=True para descendente)
    orden = False if orden in ("asc", "ascendente") else True
    paises_ordenados = sorted(data, key=lambda x: x[tipo], reverse=orden)
    paginar(paises_ordenados)