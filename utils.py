import csv, os

def menu() -> str:
    """
    Devuelve la lista de opciones.
    """
    opciones = ("Cargar datos desde CSV", "Buscar país", "Filtrar países", "Ordenar países", "Mostrar estadísticas", "Salir")
    print("\n--- Gestión de Datos de Países ---")
    for i, opcion in enumerate(opciones):
        print(f"{i+1}. {opcion}")


def read_csv(path: str) -> list:
    """Devuelve el contenido del csv.

    Parámetros:
        path (str): El primer número.

    Retorna:
        list: Lista del contenido de csv en diccionarios.
    """
    paises = []
    with open(path, mode="r", encoding="utf-8-sig") as csv_open:
        csv_read = csv.DictReader(csv_open)
        for pais in csv_read:
            try:
                pais_dict = {
                    "nombre": pais["nombre"],
                    "poblacion": int(pais["poblacion"]),
                    "superficie": int(pais["superficie"]),
                    "continente": pais["continente"]
                }
                paises.append(pais_dict)
            except ValueError:
                print("⚠️ Valor inválido.")
                return "Error"
    return paises

def search_pais(df: list, pais_busc: str) -> str:
    """Busca el país dentro de una lista de diccionarios.
    
    Parámetros:
        df (list): Lista de paises en diccionarios.\n
        pais_busc (str): Nombre del país a buscar.\n

    Retorna:
        str: País con sus características (Población, Superficie, Continente).
    """
    for item in df:
        if pais_busc.lower() == item["nombre"].lower():
            return f"País: {item["nombre"]}\nPoblación: {item["poblacion"]} habitantes\nSuperficie: {item["superficie"]}km2\nContinente: {item["continente"]}"
        return "⚠️ País no encontrado"
    
def filtrar_paises(df:list, tipo:str, value:str | list) -> list:
    """Filtra los paises por tipo (continente, poblacion, superficie).

    Parámetros:
        df (list): Lista de paises en diccionarios.\n
        tipo (str): Tipo de dato para filtrar.\n
        value (str | list): Valor o valores por los que filtrar. \n

    Retorna:
        list: Lista de países filtrados.
    """
    paises_filtrados = []

    if tipo == "continente":
        for item in df:
            if item["continente"] == value:
                paises_filtrados.append(item)

    else:
        for item in df:
            if value[0] < item[f"{tipo}"] < value[1]:
                paises_filtrados.append(item)

    if len(paises_filtrados) == 0:
        return "⚠️ Ningun país encontrado bajo el filtrado..."
    else:
        return paises_filtrados

def ordenar_paises(df:list, tipo: str, orden: bool) -> list:
    """Ordenar paises por nombre, población o superficie. 

    Parámetros:
        df (list): Lista de paises en diccionarios.\n
        tipo (str): Tipo de dato para ordenar.\n
        orden (str): Define el orden.\n
    Retorna:
        list: Lista de países ordenados.
    """

    return df.sort(key = lambda x: x[tipo], reverse = orden)


def mostrar_estadisticas(paises):


    if len(paises) == 0:
        print("No hay datos cargados.")
        return


    total_poblacion = 0
    total_superficie = 0

    for p in paises:
        total_poblacion += p["poblacion"]
        total_superficie += p["superficie"]

    promedio_poblacion = total_poblacion / len(paises)
    promedio_superficie = total_superficie / len(paises)


    pais_mayor = paises[0]
    pais_menor = paises[0]

    for p in paises:
        if p["poblacion"] > pais_mayor["poblacion"]:
            pais_mayor = p
        if p["poblacion"] < pais_menor["poblacion"]:
            pais_menor = p


    cantidad_por_continente = {}
    for p in paises:
        cont = p["continente"]
        if cont in cantidad_por_continente:
            cantidad_por_continente[cont] += 1
        else:
            cantidad_por_continente[cont] = 1


    print("\n--- Estadísticas ---")
    print(f"Promedio de población: {promedio_poblacion:,.2f}")
    print(f"Promedio de superficie: {promedio_superficie:,.2f}")
    print(f"País con mayor población: {pais_mayor['nombre']} → {pais_mayor['poblacion']:,}")
    print(f"País con menor población: {pais_menor['nombre']} → {pais_menor['poblacion']:,}")
    print("\nCantidad de países por continente:")
    