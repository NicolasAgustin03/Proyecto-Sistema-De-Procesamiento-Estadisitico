def separar(caracteres: str,separador: str = ",")-> list:

    """
    Separa una cadena de
    caracteres utilizando
    un separador determinado.

    Retorno:
    list -> lista con las
    cadenas obtenidas.
    """

    
    lista_palabras = []
    palabra_actual = ""

    for letra in caracteres:
        
        if letra != separador and ord(letra) != 10:
            palabra_actual += letra       
        else:
            lista_palabras.append(palabra_actual)
            palabra_actual = ""

    if len(palabra_actual) > 0:        
        lista_palabras.append(palabra_actual)

    return lista_palabras