def validar_rango(num:int , minimo:int , maximo:int) -> bool:
    """
    Determina si un numero se encuentra
    entre un valor minimo y un valor maximo.
    """

    retorno = False

    if num >= minimo and num <= maximo:
        retorno = True

    return retorno
    

def es_numero(cadena:str) -> bool:
    valido = True

    if cadena == "":
        valido = False

    for i in range (len(cadena)):
        if ord(cadena[i]) < 48 or ord(cadena[i]) > 57:
            valido = False
    
    return valido

def get_int(mensaje:str) -> int:

    numero = input(mensaje)

    while es_numero(numero) == False:
        print("Error. Ingrese un numero entero")
        numero = input(mensaje)
    
    numero = int(numero)

    return numero

def get_indice(mensaje:str, minimo:int, maximo:int) -> int:

    indice = get_int(mensaje)

    while validar_rango(indice, minimo, maximo) == False:
        print("Indice invalido")
        indice = get_int(mensaje)

    return indice
