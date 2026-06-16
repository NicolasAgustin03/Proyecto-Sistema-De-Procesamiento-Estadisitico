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

    """
    Determina si una cadena
    contiene solamente caracteres
    numericos.

    Retorno:
    true -> cadena numerica.
    false -> cadena NO numerica.
    """
     
    valido = True

    if cadena == "":
        valido = False

    for i in range (len(cadena)):
        if ord(cadena[i]) < 48 or ord(cadena[i]) > 57:
            valido = False
    
    return valido

def get_int(mensaje:str) -> int:

    """
    Solicita el ingreso de un
    numero entero validando
    la informacion ingresada.

    Retorno:
    int -> numero entero validado.
    """

    numero = input(mensaje)

    while es_numero(numero) == False:
        print("Error. Ingrese un numero entero")
        numero = input(mensaje)
    
    numero = int(numero)

    return numero

def get_indice(mensaje:str, minimo:int, maximo:int) -> int:

    """
    Solicita el ingreso de un
    indice dentro de un rango
    determinado.

    Retorno:
    int -> indice validado.
    """

    indice = get_int(mensaje)

    while validar_rango(indice, minimo, maximo) == False:
        print("Indice invalido")
        indice = get_int(mensaje)

    return indice
