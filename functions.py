import csv, os

def read_csv():
    paises = []
    path_csv = "paises_mundo.csv"
    with open(path_csv, mode="r", encoding="utf-8-sig") as csv_open:
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

def search_pais(df, pais_busc):
    for item in df:
        if pais_busc.lower() == item["nombre"].lower():
            return f"País: {item["nombre"]}\nPoblación: {item["poblacion"]}\nSuperficie: {item["superficie"]}km2\nContinente: {item["continente"]}"
        return "⚠️ País no encontrado"