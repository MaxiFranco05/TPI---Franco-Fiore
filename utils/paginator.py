from utils.utils import terminal_size

def paginar(lista: list[dict], por_pagina: int = 10):
    """
    Parámetros:
        lista (list[dict]): Lista de países o elementos a mostrar.
        por_pagina (int): Cantidad de elementos por página (por defecto, 10).
    """
    if not lista:
        print("\n⚠️  No hay datos para mostrar.")
        return

    total = len(lista)
    inicio = 0
    pagina = 1
    total_paginas = (total + por_pagina - 1) // por_pagina  

    while inicio < total:
        fin = inicio + por_pagina
        bloque = lista[inicio:fin]

    
        print("\n" + " Resultados ".center(terminal_size(), "~"))
        print(f"Página {pagina}/{total_paginas} | Mostrando {inicio + 1}-{min(fin, total)} de {total} países".center(terminal_size()))
        print("~" * terminal_size())


        for i, item in enumerate(bloque, start=inicio + 1):
            nombre = item.get("nombre", "Desconocido")
            poblacion = item.get("poblacion", "N/D")
            superficie = item.get("superficie", "N/D")
            continente = item.get("continente", "N/D")
            print(f"📍  {i}. {nombre}")
            print(f"     Población: {poblacion:,} habitantes")
            print(f"     Superficie: {superficie:,} km²")
            print(f"     Continente: {continente}")
            print("-" * terminal_size())

        
        if fin >= total:
            print("\n📘 Fin de la lista. Total de países mostrados:", total)
            break

        print("~" * terminal_size())
        print("➡️  Enter = siguiente página | 🔙 'a' = anterior | ❌ 's' = salir")
        print("~" * terminal_size())

        opcion = input("Seleccione una opción: ").lower().strip()

    
        if opcion == 's':
            print("\n👋  Saliendo del paginador...\n")
            break


        elif opcion == 'a':
            if pagina > 1:
                pagina -= 1
                inicio -= por_pagina
                if inicio < 0:
                    inicio = 0
            else:
                print("\n⚠️  Ya estás en la primera página.")
                input("Presione Enter para continuar...")
                continue

    
        elif opcion == '':
            pagina += 1
            inicio += por_pagina

        else:
            print(f"\n⚠️  Opción '{opcion}' no válida. Use Enter, 'a' o 's'.")
            input("Presione Enter para continuar...")
