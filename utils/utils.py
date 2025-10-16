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