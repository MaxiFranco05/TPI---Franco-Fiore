from utils.utils import eliminar_tildes, terminal_size

def search_pais(data: list) -> str:
    """Busca el país dentro de una lista de diccionarios.
    Parámetros:\n
        data (list): Lista de paises en diccionarios.
        pais_busc (str): Nombre del país a buscar.
    Retorna:\n
        str: País con sus características (Población, Superficie, Continente).
    """

    searched_pais = input("Ingrese el nombre del país: ").strip().lower()
    match_paises = [item for item in data if eliminar_tildes(searched_pais) == eliminar_tildes(item["nombre"].lower())]
    print("~-"*(terminal_size()//2))
    if len(match_paises) == 0:
        return print("⚠️  País no encontrado")
    else:
        for item in match_paises:
            print(f"📍  {item['nombre']}\nPoblación: {item['poblacion']:,} habitantes\nSuperficie: {item['superficie']:,} km²\nContinente: {item['continente']}")
        print("~-"*(terminal_size()//2))
        return