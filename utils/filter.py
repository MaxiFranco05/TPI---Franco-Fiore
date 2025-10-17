from utils.utils import eliminar_tildes

def filter(data: list):
    """Devuelve los paises filtrados
        Parámetros:\n
            data (list): Lista de paises en diccionarios.
        Retorna:\n
            str: Paises filtrados.
    """
    filters = ("continente", "poblacion", "superficie")
    filter_type = input(f"Selecciona la opción por la cual filtrar {filters}: ").lower().strip()
    if filter_type not in filters:
        return print("⚠️   Su opción no se encuentra entre los filtros.")
    if filter_type == "continente":
        continents = ("asia", "america del sur", "america del norte", "africa", "europa")
        filter_option = input(f"Ingrese el continente ({', '.join(i.title() for i in continents)}): ").lower().strip()
        if eliminar_tildes(filter_option) in continents: 
            print("-"*14,f"Paises filtrados por {filter_option.title()}","-"*14)
            filter_paises(data, filter_type, filter_option)
            print("-"*50)
        else: 
            return print("❌   Continente no válido.")
    else:
        filter_value = []
        for i in ("primer", "segundo"):
            valores = input(f"Ingrese el {i} valor: ")
            try:
                filter_value.append(int(valores))
            except ValueError:
                return print("⚠️   Valor inválido.")
        if filter_value[1] > filter_value[0] >= 0:
            print("-"*14,f"Paises filtrados por {filter_type.title()} (entre {filter_value[0]:,} y {filter_value[1]:,})","-"*14)
            filter_paises(data, filter_type, filter_value)
            print("-"*80)
        else:
            return print("⚠️   Valores inválidos.")


def filter_paises(data:list, tipo:str, value:str | list) -> list:
    """Filtra los paises por tipo (continente, poblacion, superficie).
    Parámetros:\n
        data (list): Lista de paises en diccionarios.\n
        tipo (str): Tipo de dato para filtrar.\n
        value (str | list): Valor o valores por los que filtrar. \n
    Retorna:\n
        list: Lista de países filtrados.
    """
    paises_filtrados = []

    if tipo.lower().strip() == "continente":
        for item in data:
            if eliminar_tildes(item["continente"]).lower() == eliminar_tildes(value).lower():
                paises_filtrados.append(item)

    else:
        for item in data:
            if value[0] <= item[f"{tipo}"] <= value[1]:
                paises_filtrados.append(item)

    if len(paises_filtrados) == 0:
        return print("⚠️   Ningun país encontrado bajo el filtrado...")
    else:
        for i in paises_filtrados:
            print(f"📍  País: {i['nombre']} | 👨‍👩‍👧‍👦  Población: {i['poblacion']:,} | 🗺️  Superficie: {i['superficie']:,} | 🌎  Continente: {i['continente']}")
        return
