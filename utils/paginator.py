from utils.utils import console_size

def paginar(data: list[dict], page_size: int = 5, ):
    """
    Parámetros:
        data (list[dict]): data de países o elementos a mostrar.
        page_size (int): Cantidad de elementos por página (por defecto, 10).
    """
    if not data:
        print("⚠️  No hay datos para mostrar.")
        return

    total = len(data)
    inicio = 0
    pagina = 1
    total_paginas = (total + page_size - 1) // page_size  

    while inicio < total:
        fin = inicio + page_size
        bloque = data[inicio:fin]

    
        print("\n" + " Resultados ".center(console_size(), "~"))
        print(f"Página {pagina}/{total_paginas} | Mostrando {inicio + 1}-{min(fin, total)} de {total} países".center(console_size()))
        print("~" * console_size())


        for i, item in enumerate(bloque, start=inicio + 1):
            nombre = item.get("nombre", "Desconocido")
            poblacion = item.get("poblacion", "N/D")
            superficie = item.get("superficie", "N/D")
            continente = item.get("continente", "N/D")
            print(f"\n📍  {i}. {nombre}")
            print(f"     Población: {poblacion:,} habitantes")
            print(f"     Superficie: {superficie:,} km²")
            print(f"     Continente: {continente}")

        
        if fin >= total:
            print("\n📘 Fin de la lista. Total de países mostrados:", total)
            break

        print("~" * console_size())
        print(" ➡️  Enter = siguiente página | 🔙 'a' = anterior | ❌ 's' = salir ".center(console_size()))
        print("~" * console_size())

        opcion = input("Seleccione una opción: ").lower().strip()

    
        if opcion == 's':
            print("\n👋  Saliendo del paginador...\n")
            break


        elif opcion == 'a':
            if pagina > 1:
                pagina -= 1
                inicio -= page_size
                if inicio < 0:
                    inicio = 0
            else:
                print("\n⚠️  Ya estás en la primera página.")
                input("Presione Enter para continuar...")
                continue

    
        elif opcion == '':
            pagina += 1
            inicio += page_size

        else:
            print(f"\n⚠️  Opción '{opcion}' no válida. Use Enter, 'a' o 's'.")
            input("Presione Enter para continuar...")
