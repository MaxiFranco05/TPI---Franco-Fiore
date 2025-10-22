import shutil, os

def eliminar_tildes(texto:str):
    """Elimina las tildes del texto ingresado. 
        Parámetros:
            texto (str): Texto a quitar tildes.\n
        Retorna:
            str: Texto sin tildes.
    """
    tildes = (
        ("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"),
        ("Á", "A"), ("É", "E"), ("Í", "I"), ("Ó", "O"), ("Ú", "U")
    )
    try:
        for a, b in tildes:
            texto = texto.replace(a, b)
        return texto
    except (AttributeError, TypeError, ValueError):
        return None

def console_size():
    """
    Obtiene el ancho de la consola de forma segura.\n
    Retorna:\n
        Devuelve 50 si no puede detectarlo.
    """
    try:
        size = shutil.get_terminal_size()
        return size.columns
    except Exception: 
        return 50
    
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')