from utils.utils import eliminar_tildes, console_size
from utils.paginator import paginar

def search_pais(data: list) -> str:
    """Busca el país dentro de una lista de diccionarios.
    Parámetros:\n
        data (list): Lista de paises en diccionarios.
        pais_busc (str): Nombre del país a buscar.
    Retorna:\n
        str: País con sus características (Población, Superficie, Continente).
    """

    searched_pais = input("Ingrese el nombre del país: ").strip().lower()
    match_pais = [item for item in data if eliminar_tildes(searched_pais) == eliminar_tildes(item["nombre"]).lower()]
    if len(match_pais) == 0:
        possible_paises = [item for item in data if eliminar_tildes(searched_pais) in eliminar_tildes(item["nombre"]).lower()]
        possible_paises = sorted(possible_paises, key=lambda x: len(x["nombre"]))
        if len(possible_paises) > 0:
            if len(possible_paises) <= 5:
                print(" Posibles resultados ".center(console_size(), "~"))
                for item in possible_paises:
                    print(f"📍  {item['nombre']}\nPoblación: {item['poblacion']:,} habitantes\nSuperficie: {item['superficie']:,} km²\nContinente: {item['continente']}")
                    print("-"*console_size())
                return
            else:
                paginar(possible_paises)
        print("⚠️ Sin resultados precisos ni parciales.")
    else:
        print("~"*console_size())
        for item in match_pais:
            print(f"📍  {item['nombre']}\nPoblación: {item['poblacion']:,} habitantes\nSuperficie: {item['superficie']:,} km²\nContinente: {item['continente']}")
        print("~"*console_size())
        return
    