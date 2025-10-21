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
                except KeyError as e:
                    print(f"⚠️  Campo no encontrado. ({e} no es un campo del CSV)")
                    continue
                except (ValueError, AttributeError) as e:
                    print(f"⚠️  Valor inválido. ({e})")
                    continue
        if not paises:
            print("⚠️  No se cargaron datos válidos del CSV.")
        return paises
    except FileNotFoundError:
        raise Exception("⚠️  CSV no encontrado. Verifica por favor el documento.")