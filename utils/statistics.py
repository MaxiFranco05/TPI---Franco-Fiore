from utils.utils import terminal_size

def statistics(data: list[dict]):
    """Devuelve las estadisticas mundiales. 
        Parámetros:\n
            data (list): Lista de paises en diccionarios.
    """
    prom_pobl = sum(p["poblacion"] for p in data) / len(data)
    prom_superf = sum(p["superficie"] for p in data) / len(data)
    pais_mayor = max(data, key=lambda p: p["poblacion"])
    pais_menor = min(data, key=lambda p: p["poblacion"])

    cant_por_continente = {}
    for pais in data:
        cont = pais["continente"]
        if cont in cant_por_continente:
            cant_por_continente[cont] += 1
        else:
            cant_por_continente[cont] = 1

    print(" Estadísticas ".center(terminal_size(), "~"))
    print(f"🗺️   Promedio de superficie: {prom_superf:,.2f} km²")
    print(f"👨  Promedio de población: {prom_pobl:,.2f} habitantes")
    print(f"👨  País con mayor población: {pais_mayor['nombre']} → {pais_mayor['poblacion']:,} habitantes.")
    print(f"👨  País con menor población: {pais_menor['nombre']} → {pais_menor['poblacion']:,} habitantes.")
    print(f"🌎  Cantidad de países por continente:")
    for cont, cant in cant_por_continente.items():
        print(f"                                    • {cont}: {cant} paises")
    print("~"*terminal_size())
    return