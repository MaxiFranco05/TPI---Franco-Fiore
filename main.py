from utils import menu, read_csv, search_pais, filtrar_paises, ordenar_paises, mostrar_estadisticas

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
        path_csv = "paises_mundo.csv"
        df_csv = read_csv(path_csv)
        

        match opcion:
            case 1:
                pais_buscado = input("Ingrese el nombre del país: ")
                print(search_pais(df_csv, pais_buscado.strip()))
                pass
            case 2:
                filtros = ("continente", "poblacion", "superficie")
                filtro_tipo = input(f"Selecciona la opción por la cual filtrar {filtros}: ")
                if filtro_tipo.lower().strip() in filtros:
                    if filtro_tipo.lower() == "continente":
                        continentes = ["asia", "america del sur", "america del norte", "africa", "europa"]
                        filtro_opcion = input(f"Ingrese el continente ({', '.join(i.title() for i in continentes)}): ")
                        if filtro_opcion.lower().replace("é", "e").replace("á","a") in continentes: 
                            print(f"--------------Paises filtrados por {filtro_opcion.title()}--------------")
                            filtrar_paises(df_csv, filtro_tipo, filtro_opcion)
                            print("-------------------------------------------------------------")
                    else:
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
                            filtrar_paises(df_csv, filtro_tipo, filtro_valor)
                            print("-----------------------------------------------------------------------")
                else:
                    print("⚠️ Opción inválida")
            case 3:
                ordenar_paises(df_csv)
                pass
            case 4:
                mostrar_estadisticas(df_csv)
            case 5:
                print("👋 Gracias por usar el sistema de paises. ¡Hasta pronto!")
                break 
            case _:
                print("⚠️ Opción inválida. Intente de nuevo")
                continue

main()