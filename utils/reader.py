import csv

def read_csv(path: str) -> list:
    """Devuelve el contenido del CSV en diccionarios.
    Parámetros:\n
        path (str): El primer número.
    Retorna:\n
        list: Lista del contenido del CSV en diccionarios.
    """
    paises = []
    try:
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
                    return
        return paises
    except FileNotFoundError:
        print("⚠️   CSV no encontrado.")
        return None