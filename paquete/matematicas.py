def es_par (num:int) -> bool:

    """
    Determina si un numero es 
    par. Retorna true
    si es par o false si
    es impar
    """

    if num == 0:
        return True
    elif num == 1:
        return False
    
    return es_par(num - 2)

def es_multiplo(num1:int , num2:int) -> bool:

    """
    Determina si un numero es
    multiplo de otro. Retorna
    true si es multiplo y
    false si no lo es
    """

    retorno = False

    if num1 % num2 == 0:
        retorno = True

    return retorno
    

def es_primo(num:int) -> bool:

    """
    Determina si un numero es
    primo.

    Retorno:
    true -> primo
    false -> NO primo
    """

    retorno = False

    if num > 1:

        divisores = 0

        for i in range(1, num + 1):
            if num % i == 0:
                divisores += 1

        if divisores == 2:
            retorno = True

    return retorno

def calcular_promedio(lista:list) -> float:

    suma = 0

    for i in range(len(lista)):
        suma += lista[i]

    promedio = suma / len(lista)

    return promedio

def calcular_maximo(lista:list):
    
    for i in range (len(lista)):
        if i == 0:
            may = lista[i]
        elif lista[i] > may:
            may = lista[i]

    return may    

def calcular_minimo(lista:list):
    
    for i in range (len(lista)):
        if i == 0:
            men = lista[i]
        elif lista[i] < men:
            men = lista[i]

    return men
    
        

    




