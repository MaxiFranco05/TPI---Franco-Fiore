from utils.utils import eliminar_tildes, terminal_size

def filter(data: list[dict]):
    """Devuelve los paises filtrados
        Parámetros:\n
            data (list): Lista de paises en diccionarios.
        Retorna:\n
            None: Imprime en consola los países filtrados.
    """
    filters = ("continente", "poblacion", "superficie") # Filtros principales
    filter_type = input(f"Selecciona la opción por la cual filtrar ({' - '.join(i.title() for i in filters)}): ").lower().strip() # El usuario ingresa la opción por filtrar
    if filter_type not in filters: # Si el usuario no ingresa alguna opción, se vuelve al menú.
        print("⚠️  Su opción no se encuentra entre los filtros.")
        return

    if filter_type == "continente": # Ejectuta si la opción es 'continente'.
        continents = ("asia", "america del sur", "america del norte", "africa", "europa")
        filter_option = input(f"Ingrese el continente ({' - '.join(i.title() for i in continents)}): ").lower().strip()
        if eliminar_tildes(filter_option) in continents: 
            print(f" Paises filtrados por {filter_option.title()} ".center(terminal_size(), "~"))
            filter_paises(data, filter_type, filter_option)
        else: 
            print("⚠️  Continente no válido.")
            return
    
    else: # Ejectuta si la opción es 'población' o 'superficie'.
        filter_value = []
        for i in ("minimo", "máximo"):
            try:
                filter_value.append(int(input(f"Ingrese el valor {i}: ").strip()))
            except ValueError:
                return print("⚠️  Valor inválido.")

        if filter_value[1] > filter_value[0] >= 0:
            print(f" Paises filtrados por {filter_type.title()} (entre {filter_value[0]:,} y {filter_value[1]:,}) ".center(terminal_size(), "~"))
            filter_paises(data, filter_type, filter_value)
        else:
            return print("⚠️  Valores inválidos.")


def filter_paises(data:list, tipo:str, value:str | list[int]) -> list:
    """Filtra los paises por tipo (continente, poblacion, superficie).
    Parámetros:\n
        data (list): Lista de paises en diccionarios.
        tipo (str): Tipo de dato para filtrar.
        value (str | list): Valor o valores por los que filtrar. 
    Retorna:\n
        none: Unicamente imprime en consola los paises filtrados.
    """
    paises_filtrados = []

    if tipo.lower().strip() == "continente":
        paises_filtrados = [pais for pais in data if eliminar_tildes(pais["continente"]).lower() == eliminar_tildes(value).lower()]

    else:
        paises_filtrados = [pais for pais in data if value[0] <= pais[f"{tipo}"] <= value[1]]


    if len(paises_filtrados) == 0:
        return print("⚠️  Ningun país encontrado bajo el filtrado...")
    else:

        for i in paises_filtrados:
            if tipo == 'continente':
                print(f"📍  {i['nombre']}\nPoblacion: {i['poblacion']} habitantes\nSuperficie: {i['superficie']} km²")
            else:
                print(f"{i['nombre']} - {i[tipo]:,} {'habitantes' if tipo == 'poblacion' else 'km²'}")
        print("~"*terminal_size())
        return
    

