from .validaciones import *
from .tablas import *

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

    """
    Calcula la varianza de
    una lista numerica.

    Retorno:
    float -> varianza de
    la lista.
    """

    promedio = calcular_promedio(lista)

    suma = 0

    for i in range(len(lista)):

        diferencia = lista[i] - promedio

        suma += diferencia ** 2

    varianza = suma / len(lista)

    return varianza

def calcular_desvio_estandar(lista:list) -> float:

    """
    Calcula el desvio
    estandar de una lista
    numerica.

    Retorno:
    float -> desvio
    estandar de la lista.
    """

    varianza = calcular_varianza(lista)

    desvio = varianza ** 0.5

    return desvio

def calcular_coeficiente_variacion(lista:list) -> float:

    """
    Calcula el coeficiente
    de variacion de una
    lista numerica.

    Retorno:
    float -> coeficiente
    de variacion de la
    lista.
    """

    promedio = calcular_promedio(lista)

    desvio = calcular_desvio_estandar(lista)

    coeficiente = (desvio / promedio) * 100

    return coeficiente

def ordenar_ascendente(lista:list) -> list:

    """
    Ordena una lista
    numerica de forma
    ascendente.

    Retorno:
    list -> lista
    ordenada.
    """

    for i in range(len(lista) - 1):

        for j in range(len(lista) - 1 - i):

            if lista[j] > lista[j + 1]:

                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux

    return lista

def calcular_mediana(lista:list) -> float:

    """
    Calcula la mediana de
    una lista numerica
    ordenada.

    Retorno:
    float -> mediana de
    la lista.
    """

    cantidad = len(lista)

    if cantidad % 2 != 0:

        mediana = lista[cantidad // 2]

    else:

        medio1 = lista[(cantidad // 2) - 1]
        medio2 = lista[cantidad // 2]

        mediana = (medio1 + medio2) / 2

    return mediana

def calcular_cuartiles(lista:list) -> tuple:

    """
    Calcula el primer, segundo
    y tercer cuartil de una
    lista numerica ordenada.

    Retorno:
    tuple -> cuartiles Q1,
    Q2 y Q3.
    """

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

def gestionar_estadistica(proyecto:dict):

    """
    Permite gestionar las
    operaciones estadisticas
    sobre una tabla, incluyendo
    frecuencias, medidas de
    tendencia central, medidas
    de dispersion y medidas de
    posicion.
    """

    nombre_columnas = proyecto["nombre_columnas"]
    tabla = proyecto["tabla"]

    submenu_3 = 1

    while submenu_3 != 7:

                submenu_3 = get_indice("Menu: \n"
                                "1) Frecuencias\n" 
                                "2) Maximos y minimos\n"
                                "3) Promedio aritmetico\n"
                                "4) Promedio Geometrico\n" 
                                "5) Medidas de dispersion\n"
                                "6) Medidas de posicion\n"  
                                "7) Volver al menu principal\n",
                                1,
                                7)
                
                match submenu_3:

                    case 1:
                        columna = seleccionar_columna(nombre_columnas)
                        
                        if es_columna_numerica(tabla , columna) == True:

                            lista_columna = obtener_columna(tabla , columna)

                            valor = get_int("Ingrese el valor numerico que desee hallar su frecuencia: ")

                            frecuencia = calcular_frecuencia(lista_columna , valor )

                            print(f"La frecuencia con la cual aparece el numero {valor} es: {frecuencia}  ")

                        else:

                            lista_columna = obtener_columna(tabla , columna)
                            
                            valor = input("Ingrese un valor que desee hallar su frecuencia: ")

                            frecuencia = calcular_frecuencia(lista_columna , valor )

                            print(f"La frecuencia con la cual aparece {valor} es: {frecuencia}  ")


                    case 2:
                        columna = seleccionar_columna(nombre_columnas)
                        
                        if es_columna_numerica(tabla , columna) == True:

                            lista_columna = obtener_columna(tabla , columna)

                            may = calcular_maximo(lista_columna)
                            men = calcular_minimo(lista_columna)

                            print(f"Maximo: {may}")
                            print(f"Men: {men}")

                        else:
                            print("La columna ingresada no es numerica")

                    case 3:
                        columna = seleccionar_columna(nombre_columnas)
                        
                        if es_columna_numerica(tabla , columna) == True:

                            lista_columna = obtener_columna(tabla , columna)

                            promedio = calcular_promedio(lista_columna)

                            print(f"Promedio: {promedio}")

                        else:
                            print("La columna ingresada no es numerica")

                    case 4:
                        columna = seleccionar_columna(nombre_columnas)
                        
                        if es_columna_numerica(tabla , columna) == True:

                            lista_columna = obtener_columna(tabla , columna)

                            promedio = calcular_promedio_geometrico(lista_columna)

                            print(f"Promedio Geometrico: {promedio}")

                        else:
                            print("La columna ingresada no es numerica")

                    case 5:
                        submenu_4 = 1

                        while submenu_4 != 5:

                            submenu_4 = get_indice("Menu(Medidas de dispersion): \n"
                                                   "1) Rango\n" 
                                                   "2) Varianza\n"
                                                   "3) Desvio estandar\n"
                                                   "4) Coeficiente de variacion\n"
                                                   "5) Volver al menu de estadistica\n",
                                                   1,
                                                   5
                                                   )
                            
                            match submenu_4:

                                case 1:
                                    columna = seleccionar_columna(nombre_columnas)
                        
                                    if es_columna_numerica(tabla , columna) == True:

                                        lista_columna = obtener_columna(tabla , columna)

                                        rango = calcular_rango(lista_columna)

                                        print(f"El rango entre el maximo y el minimo es: {rango}")

                                    else:
                                        print("La columna ingresada no es numerica")

                                case 2:
                                    columna = seleccionar_columna(nombre_columnas)
                        
                                    if es_columna_numerica(tabla , columna) == True:

                                        lista_columna = obtener_columna(tabla , columna)

                                        varianza = calcular_varianza(lista_columna)

                                        print(f"La varianza es: {varianza}")

                                    else:
                                        print("La columna ingresada no es numerica")

                                case 3:
                                    columna = seleccionar_columna(nombre_columnas)
                        
                                    if es_columna_numerica(tabla , columna) == True:

                                        lista_columna = obtener_columna(tabla , columna)

                                        desvio_estandar =  calcular_desvio_estandar(lista_columna)

                                        print(f"El desvio estandar es: {desvio_estandar}")

                                    else:
                                        print("La columna ingresada no es numerica")

                                case 4:
                                    columna = seleccionar_columna(nombre_columnas)
                        
                                    if es_columna_numerica(tabla , columna) == True:

                                        lista_columna = obtener_columna(tabla , columna)

                                        coeficiente_variacion = calcular_coeficiente_variacion(lista_columna)

                                        print(f"El coeficiente de variacion es: {coeficiente_variacion}")

                                    else:
                                        print("La columna ingresada no es numerica")

                    case 6:
                        submenu_5 = 1

                        while submenu_5 != 3:

                            submenu_5 = get_indice("Menu(Medidas de posicion): \n"
                                                   "1) Mediana\n" 
                                                   "2) Cuartiles\n"
                                                   "3) Salir\n",
                                                   1,
                                                   3
                                                   )
                            
                            match submenu_5:

                                case 1:

                                    columna = seleccionar_columna(nombre_columnas)
                        
                                    if es_columna_numerica(tabla , columna) == True:

                                        lista_columna = obtener_columna(tabla , columna)

                                        ordenar_ascendente(lista_columna)

                                        mediana = calcular_mediana(lista_columna)

                                        print(f"Mediana: {mediana}")
                                    
                                    else:
                                        print("La columna ingresada no es numerica")

                                case 2:

                                    columna = seleccionar_columna(nombre_columnas)
                        
                                    if es_columna_numerica(tabla , columna) == True:

                                        lista_columna = obtener_columna(tabla , columna)

                                        ordenar_ascendente(lista_columna)

                                        q1, q2, q3 = calcular_cuartiles(lista_columna)

                                        print(f"Q1: {q1}")
                                        print(f"Q2: {q2}")
                                        print(f"Q3: {q3}")
                                    
                                    else:
                                        print("La columna ingresada no es numerica")
    
        

    




