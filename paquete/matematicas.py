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

def calcular_varianza(lista:list) -> float:

    promedio = calcular_promedio(lista)

    suma = 0

    for i in range(len(lista)):

        diferencia = lista[i] - promedio

        suma += diferencia ** 2

    varianza = suma / len(lista)

    return varianza

def calcular_desvio_estandar(lista:list) -> float:

    varianza = calcular_varianza(lista)

    desvio = varianza ** 0.5

    return desvio

def calcular_coeficiente_variacion(lista:list) -> float:

    promedio = calcular_promedio(lista)

    desvio = calcular_desvio_estandar(lista)

    coeficiente = (desvio / promedio) * 100

    return coeficiente

def ordenar_ascendente(lista:list) -> list:

    for i in range(len(lista) - 1):

        for j in range(len(lista) - 1 - i):

            if lista[j] > lista[j + 1]:

                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux

    return lista

def calcular_mediana(lista:list) -> float:

    cantidad = len(lista)

    if cantidad % 2 != 0:

        mediana = lista[cantidad // 2]

    else:

        medio1 = lista[(cantidad // 2) - 1]
        medio2 = lista[cantidad // 2]

        mediana = (medio1 + medio2) / 2

    return mediana

def calcular_cuartiles(lista:list) -> tuple:

    mitad_inferior = []
    mitad_superior = []

    medio = len(lista) // 2

    if len(lista) % 2 == 0:

        for i in range(medio):
            mitad_inferior.append(lista[i])

        for i in range(medio, len(lista)):
            mitad_superior.append(lista[i])

    else:

        for i in range(medio):
            mitad_inferior.append(lista[i])

        for i in range(medio + 1, len(lista)):
            mitad_superior.append(lista[i])

    q1 = calcular_mediana(mitad_inferior)
    q2 = calcular_mediana(lista)
    q3 = calcular_mediana(mitad_superior)

    return q1, q2, q3
    
        

    




