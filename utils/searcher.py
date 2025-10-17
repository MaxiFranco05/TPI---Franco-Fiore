from utils.utils import eliminar_tildes

def search_pais(data: list) -> str:
    """Busca el país dentro de una lista de diccionarios.
    Parámetros:\n
        data (list): Lista de paises en diccionarios.
        pais_busc (str): Nombre del país a buscar.
    Retorna:\n
        str: País con sus características (Población, Superficie, Continente).
    """
    searched_pais = input("Ingrese el nombre del país: ").strip().lower()
    print("#"*30)
    for item in data:
        if eliminar_tildes(searched_pais) == eliminar_tildes(item["nombre"]).lower():
            return print(f"📍  País: {item["nombre"]}\n👨‍👩‍👧‍👦  Población: {item["poblacion"]:,} habitantes\n🗺️  Superficie: {item["superficie"]:,} km²\n🌎  Continente: {item["continente"]}\n{"#"*30}")
    return print("⚠️   País no encontrado")