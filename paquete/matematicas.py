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

    """
    Calcula el promedio aritmetico
    de una lista numerica.

    Retorno:
    float -> promedio de la lista.
    """

    suma = 0

    for i in range(len(lista)):
        suma += lista[i]

    promedio = suma / len(lista)

    return promedio

def calcular_maximo(lista:list):

    """
    Determina el valor maximo
    de una lista numerica.

    Retorno:
    int -> valor maximo.
    """
    
    for i in range (len(lista)):
        if i == 0:
            may = lista[i]
        elif lista[i] > may:
            may = lista[i]

    return may    

def calcular_minimo(lista:list):

    """
    Determina el valor minimo
    de una lista numerica.

    Retorno:
    int -> valor minimo.
    """
    
    for i in range (len(lista)):
        if i == 0:
            men = lista[i]
        elif lista[i] < men:
            men = lista[i]

    return men

def calcular_frecuencia(lista:list, valor) -> int:

    """
    Calcula la frecuencia de un
    valor dentro de una lista.

    Retorno:
    int -> cantidad de apariciones.
    """

    contador = 0

    for i in range(len(lista)):
        if lista[i] == valor:
            contador += 1

    return contador

def calcular_promedio_geometrico(lista:list) -> float:

    """
    Calcula el promedio geometrico
    de una lista numerica.

    Retorno:
    float -> promedio geometrico.
    """

    producto = 1

    for i in range(len(lista)):
        producto *= lista[i]

    promedio = producto ** (1 / len(lista))

    return promedio

def calcular_rango(lista:list) -> int:

    """
    Calcula el rango de una lista
    numerica.

    Retorno:
    int -> diferencia entre el
    valor maximo y el minimo.
    """

    maximo = calcular_maximo(lista)
    minimo = calcular_minimo(lista)

    rango = maximo - minimo

    return rango
    
        

    




