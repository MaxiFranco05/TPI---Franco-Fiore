from utils.utils import console_size, eliminar_tildes
import csv, os, time, random


def dev_options(data: list[dict], path: str):
    """Devuelve las opciones y ejecuta la opción solicitada.
    Parámetros:\n
        data (list[dict]): Lista con el contenido del CSV.
        path (str): Ruta del archivo CSV.
    """
    options = ["Agregar país","Editar país","Eliminar país","Salir"]
    while True:
        print(" Opciones de Desarrollador ".center(console_size(), "-"))
        for i, opt in enumerate(options):
            print(f"{i+1}. {opt}")
        print("-"*console_size())
        try:
            option = int(input("Ingrese el número de la opción: ").strip())
        except ValueError:
            print("⚠️  Ingrese un número valido.")
            continue
    
        if not data and option not in (1, 4):
            print("⚠️  Primero ingrese datos al CSV o intente con uno nuevo.")
            option = 1

        match option:
            case 1:
                post_pais(path)
            case 2:
                put_pais(path)
            case 3:
                del_pais(path)
            case 4:
                break
            case _:
                print("⚠️  Ingrese una opción válida.")
        input("Presione Enter para continuar...")


def read_csv(path: str) -> list:
    """Devuelve el contenido del CSV en diccionarios.
    Parámetros:\n
        path (str): La ruta del CSV.
    Retorna:\n
        list: Lista del contenido del CSV en diccionarios.
    """
    paises = []

    if not isinstance(path, str):
        raise Exception(f"⚠️  La ruta '{path}' es inválida.")

    try:
        with open(path, mode="r", encoding="utf-8") as file:
            csv_read = csv.DictReader(file)
            cols = csv_read.fieldnames
            for pais in csv_read:
                try:
                    pais_dict = {
                        "nombre": pais[cols[0]],
                        "poblacion": int(pais[cols[1]]),
                        "superficie": int(pais[cols[2]]),
                        "continente": pais[cols[3]]
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
        print("⚠️  Archivo no encontrado.")
        create_csv(path)
        return read_csv(path) 


def create_csv(path: str):
    if not os.path.isdir(os.path.dirname(path)):
        os.mkdir(os.path.dirname(path))

    with open(path, mode="w", encoding="utf-8", newline="") as file:
        headers = ["nombre","poblacion","superficie","continente"]
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for i in range(0, 101, 20):
            print("=" * round((i/100) * console_size() if not i == 0 else 1))
            print(f" {i}% completado ".center(console_size(), " "))
            time.sleep(0.75)

        print("-"*console_size()," ✔️  Archivo creado correctamente. ".center(console_size()))
    return


def post_pais(path: str):
    """Crea un nuevo registro a partir de los datos del usuario.
    Parámetros:\n
        path (str): Ruta del archivo CSV.
    """
    # Lista de columnas
    headers = ["nombre", "poblacion", "superficie", "continente"]
    # Lista de continentes
    continents = ("América del Sur", "América del Norte", "África", "Asia", "Oceanía")
    # Abre el CSV en modo Escritura y Lectura (a+)
    with open(path, mode="a+", encoding="utf-8", newline="") as file:
        file.seek(0)  # Vuelve al inicio para leer el contenido
        reader = csv.DictReader(file)
        new_nombre = input("Ingrese el nombre del país a agregar: ").strip().title()

        # Verifica si el input ingresado está vacío
        if not new_nombre:
            print("⚠️  Nombre vacío.")
            return
        
        # Verifica si el país ingresado ya existe
        if any(row.get("nombre", "").strip().lower() == new_nombre.lower() for row in reader):
            print("⚠️  País con mismo nombre ya existe.")
            return
        
        try: 
            new_poblacion = int(input("Ingrese la población: ").strip())
            new_superficie = int(input("Ingrese la superficie: ").strip())
            # Verifica que los valores sean mayores a 0.
            if new_poblacion < 0 or new_superficie < 0:
                raise ValueError("Valores menores a 0.")

            new_continente = input(f"Ingrese el continente {continents}: ").strip().title()
            # Verifica si el continente escrito por el usuario esta dentro de la lista de continentes, si no es así, ejecuta una excepción que captura el error
            match = next(
                (continent for continent in continents if eliminar_tildes(new_continente).lower() == eliminar_tildes(continent).lower()), None  # Valor por defecto si no hay coincidencias
            )

            if match is None:
                raise ValueError("El continente no se encuentra dentro de las opciones.")
            
        except (ValueError, TypeError) as e:
            print(f"⚠️  Valores incorrectos o inválidos ({e})")
            return

        # Se asegura de escribir en el final y que haya un salto de línea antes si hace falta
        file.seek(0, os.SEEK_END)
        if file.tell() > 0:
            # Lee último carácter y si no es '\n' escribirlo
            file.seek(file.tell() - 1)
            last_char = file.read(1)
            if last_char != "\n":
                file.write("\n")

        writer = csv.DictWriter(file, fieldnames=headers)
        try:
            # Escribe los valores de los campos al final del archivo
            writer.writerow({
                "nombre": new_nombre,
                "poblacion": new_poblacion,
                "superficie": new_superficie,
                "continente": match
            })
            print("✔️  País agregado con éxito.")
            print("~"*console_size())
            print(f"📍  {new_nombre}\nPoblación: {new_poblacion:,} habitantes\nSuperficie: {new_superficie:,} km²\nContinente: {match}")
            print("~"*console_size())

        except FileNotFoundError as e:
            print(f"⚠️  Archivo no encontrado ({path}). ({e})")
        except (IOError,OSError) as e:
            print(f"⚠️  Un error ocurrió al leer el archivo. ({e})")
        except csv.Error as e:
            print(f"⚠️  Error del módulo csv. ({e})")
            return
        except Exception as e:
            print(f"⚠️  Error inesperado al escribir CSV. ({e})")
            return


def put_pais(path: str):
    """Edita un registro del CSV.
    Parámetros:\n
        path (str): Ruta del archivo CSV.
    """
    # Lista de continentes
    continents = ("América del Sur", "América del Norte", "África", "Asia", "Oceanía")
    options = ("poblacion", "superficie", "continente", "todo")

    # Abre el CSV en modo Lectura y guarda los dict en registers en forma de lista
    try:
        with open(path, mode="r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            registers = list(reader)
    except FileNotFoundError as e:
        print(f"⚠️  Archivo no encontrado ({path}). ({e})")
    except (IOError,OSError) as e:
        print(f"⚠️  Un error ocurrió al leer el archivo. ({e})")
    except csv.Error as e:
            print(f"⚠️  Error del módulo csv. ({e})")
            return
    except Exception as e:
            print(f"⚠️  Error inesperado al escribir CSV. ({e})")
            return
    
    new_nombre = input("Ingrese el nombre del país a editar: ").strip().lower()

    # Verifica si el input ingresado está vacío
    if not new_nombre:
        print("⚠️  Nombre vacío.")
        return
    
    # Verifica si el país ingresado existe, utilizamos un flag para el index y verificar
    index = None
    for i, pais in enumerate(registers):
        if eliminar_tildes(pais["nombre"].lower()) == new_nombre:
            index = i
            break

    # Si no se encontró un resultado, retorna y termina el proceso
    if index is None:
        print(f"⚠️  No se encontró ningun pais con ese nombre. ({new_nombre.title()})")
        return
    
    # Consulta el campo especifico a modificar o todos
    fields_options = input(f"Ingrese el campo que quiere modificar ({"/".join(options)}): ").strip().lower()
    # Comprueba si el input corresponde a las opciones
    if fields_options not in options:
        print("⚠️  Opción inválida o incorrecta.")
        return
    # Comprueba si el input es población o superficie
    if fields_options in ("poblacion", "superficie"):
        try:
            field_value = int(input(f"Ingrese el valor del campo '{fields_options.title()}': "))
            registers[index][fields_options] = field_value
        except (ValueError,TypeError) as e:
            print(f"⚠️  Valor inválido o incorrecto ({e})") 
    elif fields_options == "continente":
        try:
            new_continente = input(f"Ingrese el continente {continents}: ").strip().title()
            # Verifica si el continente escrito por el usuario esta dentro de la lista de continentes, si no es así, ejecuta una excepción que captura el error
            match = next(
                    (continent for continent in continents if eliminar_tildes(new_continente).lower() == eliminar_tildes(continent).lower()), None  # Valor por defecto si no hay coincidencias
                )

            if match is None:
                    raise ValueError("El continente no se encuentra dentro de las opciones")
            
        except (ValueError, TypeError) as e:
            print(f"⚠️  Valores incorrectos o inválidos ({e})")
            return
        registers[index][fields_options] = match
    else:
        try: 
            new_poblacion = int(input("Ingrese la cantidad de 'Población': ").strip())
            new_superficie = int(input("Ingrese la cantidad de 'Superficie': ").strip())
            # Verifica que los valores sean mayores a 0.
            if new_poblacion < 0 or new_superficie < 0:
                raise ValueError("Valores menores a 0.")

            new_continente = input(f"Ingrese el continente {continents}: ").strip().title()
            # Verifica si el continente escrito por el usuario esta dentro de la lista de continentes, si no es así, ejecuta una excepción que captura el error
            match = next(
                (continent for continent in continents if eliminar_tildes(new_continente).lower() == eliminar_tildes(continent).lower()), None  # Valor por defecto si no hay coincidencias
            )

            if match is None:
                raise ValueError("El continente no se encuentra dentro de las opciones")
        
        except (ValueError, TypeError) as e:
            print(f"⚠️  Valores incorrectos o inválidos ({e})")
            return

        registers[index]["poblacion"] = new_poblacion
        registers[index]["superficie"] = new_superficie
        registers[index]["continente"] = new_continente

    fields = registers[0].keys()

    try:
        with open(path, mode="w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            writer.writerows(registers)
    except FileNotFoundError as e:
        print(f"⚠️  Archivo no encontrado ({path}). ({e})")
        return
    except (IOError,OSError) as e:
        print(f"⚠️  Un error ocurrió al escribir el archivo. ({e})")
        return
    except csv.Error as e:
        print(f"⚠️  Error del módulo csv. ({e})")
        return
    except Exception as e:
        print(f"⚠️  Error inesperado al escribir CSV. ({e})")
        return
    
    print("✔️  País modificado con éxito.")
    print("~"*console_size())
    print(f"📍  {registers[index]["nombre"]}\nPoblación: {registers[index]["poblacion"]:,} habitantes\nSuperficie: {registers[index]["superficie"]:,} km²\nContinente: {registers[index]["continente"]}")
    print("~"*console_size())


def del_pais(path: str):
    # Abre el CSV en modo Lectura y guarda los dict en registers en forma de lista
    try:
        with open(path, mode="r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            registers = list(reader)
    except FileNotFoundError as e:
        print(f"⚠️  Archivo no encontrado ({path}). ({e})")
    except (IOError,OSError) as e:
        print(f"⚠️  Un error ocurrió al leer el archivo. ({e})")
    except csv.Error as e:
            print(f"⚠️  Error del módulo csv. ({e})")
            return
    except Exception as e:
            print(f"⚠️  Error inesperado al escribir CSV. ({e})")
            return
    
    new_nombre = input("Ingrese el nombre del país a editar: ").strip().lower()

    # Verifica si el input ingresado está vacío
    if not new_nombre:
        print("⚠️  Nombre vacío.")
        return
    
    # Verifica si el país ingresado existe, utilizamos un flag para el index y verificar
    index = None
    for i, pais in enumerate(registers):
        if eliminar_tildes(pais["nombre"].lower()) == new_nombre:
            index = i
            delete_pais = pais
            break

    # Si no se encontró un resultado, retorna y termina el proceso
    if index is None:
        print(f"⚠️  No se encontró ningun pais con ese nombre. ({new_nombre.title()})")
        return
    
    print(f"Pais a eliminar:")
    print("~"*console_size())
    try:
        print(f"📍  {delete_pais["nombre"]}\nPoblación: {int(delete_pais["poblacion"]):,} habitantes\nSuperficie: {int(delete_pais["superficie"]):,} km²\nContinente: {delete_pais["continente"]}")
        print("~"*console_size())
        verif_value = random.choice(list(delete_pais.values()))
        
        if eliminar_tildes(input(f"Ingrese el siguiente texto '{verif_value}' para eliminar el país: ").strip().lower()) != eliminar_tildes(verif_value.strip().lower()):
            print(f"⚠️  El texto no coincide con '{verif_value}.")
            return
        
        del registers[index]
    except (ValueError,TypeError) as e:
        print(f"⚠️  Ocurrió un error de valor. ({e})")
        return
    
    fields = registers[0].keys()

    try:
        with open(path, mode="w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            writer.writerows(registers)
        print("✔️  País eliminado con éxito.")
        return
    except FileNotFoundError as e:
        print(f"⚠️  Archivo no encontrado ({path}). ({e})")
        return
    except (IOError,OSError) as e:
        print(f"⚠️  Un error ocurrió al escribir el archivo. ({e})")
        return
    except csv.Error as e:
        print(f"⚠️  Error del módulo csv. ({e})")
        return
    except Exception as e:
        print(f"⚠️  Error inesperado al escribir CSV. ({e})")
        return