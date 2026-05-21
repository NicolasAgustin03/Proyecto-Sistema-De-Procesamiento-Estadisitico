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

def es_multiplo (num1:int , num2:int) -> bool:

    """
    Determina si un numero es 
    multiplo de otro. Retorna
    true si es multiplo y 
    false si no lo es
    """

    if num1 % num2 == 0:
        return True
    else:
        return False
    

def es_primo (num:int):

    """
    Determina si un numero es 
    primo.
    Retorno:
    true -> primo
    false -> NO primo

    """

    if num <= 1:
        return False
    
    divisores = 0

    for i in range(1, num + 1):
        if num % i == 0:
            divisores += 1

    if divisores == 2:
        return True
    else:
        return False
    




