from functions import read_csv, search_pais, filtro


def menu():
    print("\n--- Gestión de Datos de Países ---")
    print("1. Cargar datos desde CSV")
    print("2. Buscar país")
    print("3. Filtrar países")
    print("4. Ordenar países")
    print("5. Mostrar estadísticas")
    print("6. Salir") 

def main():
    while True:
        menu()
        opcion = input("Ingrese una opcion: ")
        if not opcion.isdigit():
            print("⚠️ Error: Ingrese un numero entero")
            continue
        opcion = int(opcion)

        match opcion:
            case 1:
                df_csv = read_csv()
                pass
            case 2:
                pais_buscado = input("Ingrese el nombre del país: ")
                print(search_pais(df_csv, pais_buscado.strip()))
                pass
            case 3:
                filtros = ("continente", "poblacion", "superficie")
                filtro_opcion = input(f"Selecciona la opción por la cual filtrar ({filtros}): ")
                if filtro_opcion.lower() in filtros:
                    if filtro_opcion.lower() == "continente":
                        continentes = ["asia", "america del sur", "america del norte", "africa", "europa"]
                        filtro_tipo = input(f"Ingrese el continente ({', '.join(i.title() for i in continentes)}): ")
                        if filtro_tipo.lower().replace("é", "e").replace("á","a") in continentes: 
                            print(filtro(df_csv, filtro_tipo, filtro_tipo))
                    else:
                        filtro_tipo = input(f"Ingrese el filtro (País o Población): ")
                        if filtro_tipo.lower().strip().replace("í","i").replace("ó","o") in ("pais","poblacion"):
                            filtro_valor = []
                            for i in range(2):
                                valores = input(f"Ingrese el valor N°{i}: ")
                                try:
                                    filtro_valor.append(int(valores))
                                except ValueError:
                                    print("⚠️ Valor inválido.")
                                    break

                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                print("👋 Gracias por usar el sistema de paises. ¡Hasta pronto!")
                break 
            case _:
                print("⚠️ Opción inválida. Intente de nuevo")
                continue
main()