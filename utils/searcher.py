from utils.utils import eliminar_tildes

def search_pais(data: list) -> str:
    """Busca el país dentro de una lista de diccionarios.
    Parámetros:\n
        data (list): Lista de paises en diccionarios.
        pais_busc (str): Nombre del país a buscar.
    Retorna:\n
        str: País con sus características (Población, Superficie, Continente).
    """
    searched_pais = input("Ingrese el nombre del país: ")
    for item in data:
        if eliminar_tildes(searched_pais).strip().lower() == eliminar_tildes(item["nombre"]).lower():
            return print(f"País: {item["nombre"]}\nPoblación: {item["poblacion"]:,} habitantes\nSuperficie: {item["superficie"]:,} km²\nContinente: {item["continente"]}")
    return print("⚠️   País no encontrado")