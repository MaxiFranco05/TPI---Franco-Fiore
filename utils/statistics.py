def estadisticas(data: list):
    """Devuelve las estadisticas mundiales. 
        Parámetros:\n
            data (list): Lista de paises en diccionarios.
        Retorna:\n
            str: Todas las estadisticas solicitadas.
    """
    total_pobl = 0
    total_superf = 0

    for pais in data:
        total_pobl += pais["poblacion"]
        total_superf += pais["superficie"]

    prom_pobl = total_pobl / len(data)
    prom_superf = total_superf / len(data)

    pais_mayor = data[0]
    pais_menor = data[0]

    for pais in data:
        if pais["poblacion"] > pais_mayor["poblacion"]:
            pais_mayor = pais
        if pais["poblacion"] < pais_menor["poblacion"]:
            pais_menor = pais

    cant_por_continente = {}
    for pais in data:
        cont = pais["continente"]
        if cont in cant_por_continente:
            cant_por_continente[cont] += 1
        else:
            cant_por_continente[cont] = 1

    print("-"*15,"Estadísticas","-"*15)
    print(f"Promedio de población: {prom_pobl:,.2f}")
    print(f"Promedio de superficie: {prom_superf:,.2f}")
    print(f"País con mayor población: {pais_mayor['nombre']} → {pais_mayor['poblacion']:,} habitantes.")
    print(f"País con menor población: {pais_menor['nombre']} → {pais_menor['poblacion']:,} habitantes.")
    print(f"Cantidad de países por continente:")
    print("-"*50)
    return