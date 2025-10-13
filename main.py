from utils import menu, read_csv, search_pais, filtrar_paises, ordenar_paises

def main():
    while True:
        menu()
        opcion = input("Ingrese una opcion: ")
        if not opcion.isdigit():
            print("⚠️ Ingrese un numero entero")
            continue
        try:
            opcion = int(opcion)
        except ValueError:
            print("⚠️ Ingrese un numero válido")

        match opcion:
            case 1:
                path_csv = "paises_mundo.csv"
                df_csv = read_csv(path_csv)
                pass
            case 2:
                pais_buscado = input("Ingrese el nombre del país: ")
                print(search_pais(df_csv, pais_buscado.strip()))
                pass
            case 3:
                filtros = ("continente", "poblacion", "superficie")
                filtro_opcion = input(f"Selecciona la opción por la cual filtrar ({filtros}): ")
                if filtro_opcion.lower().strip() in filtros:
                    if filtro_opcion.lower() == "continente":
                        continentes = ["asia", "america del sur", "america del norte", "africa", "europa"]
                        filtro_tipo = input(f"Ingrese el continente ({', '.join(i.title() for i in continentes)}): ")
                        if filtro_tipo.lower().replace("é", "e").replace("á","a") in continentes: 
                            print(f"--------------Paises filtrados por Continente--------------")
                            print(filtrar_paises(df_csv, filtro_opcion, filtro_tipo))
                            print("-------------------------------------------------------------")
                    else:
                        filtro_tipo = input(f"Ingrese el filtro (País o Población): ")
                        if filtro_tipo.lower().strip().replace("í","i").replace("ó","o") in ("pais","poblacion"):
                            filtro_valor = []
                            for i in ("primer", "segundo"):
                                valores = input(f"Ingrese el {i} valor: ")
                                try:
                                    filtro_valor.append(int(valores))
                                except ValueError:
                                    print("⚠️ Valor inválido.")
                                    pass
                            if filtro_valor[1] > filtro_valor[0]:
                                print(f"--------------Paises filtrados por {filtro_tipo.title()}--------------")
                                print(filtrar_paises(df_csv, filtro_opcion, filtro_valor))
                                print("-----------------------------------------------------------------------")
            case 4:
                ordenar_paises()
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