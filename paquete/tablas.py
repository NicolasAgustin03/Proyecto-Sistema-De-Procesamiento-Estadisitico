from paquete.validaciones import es_numero

#Creacion-------------------------------------------------------------------------------------------------------------------------#

def generar_matriz(filas:int , columnas:int , default) -> list:

    """
    Genera una matriz con una
    cantidad determinada de
    filas y columnas.

    Retorno:
    list -> matriz inicializada
    con el valor por defecto.
    """

    matriz = []

    for i in range(filas):

        fila = []

        for j in range(columnas):
            fila.append(default)

        matriz.append(fila)
    
    return matriz

def crear_columnas(cantidad:int) -> list:

    """
    Solicita los nombres de las
    columnas de una tabla.

    Retorno:
    list -> lista con los nombres
    de las columnas.
    """

    columnas = []

    for i in range(cantidad):

        nombre = input(f"Ingrese el nombre de la columna {i + 1}: ")

        while nombre == "":
            nombre = input(f"No se acepta cadena vacia. Ingrese el nombre de la columna {i + 1}: ")

        columnas.append(nombre)

    return columnas



#---------------------------------------------------------------------------------------------------------------------------------#



#Cargas---------------------------------------------------------------------------------------------------------------------------#

def cargar_matriz(matriz:list) -> list:

    """
    Permite cargar los datos
    de una matriz. Si el dato
    ingresado es numerico se
    almacena como entero, de
    lo contrario se almacena
    como cadena.

    Retorno:
    list -> matriz cargada.
    """

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):

            dato = input(f"Ingrese el valor de fila {i}, columna {j}: ")

            while dato == "":
                dato = input(
                    f"No se acepta cadena vacia. Ingrese el valor de fila {i}, columna {j}: "
                )

            if es_numero(dato) == True:
                matriz[i][j] = int(dato)
            else:
                matriz[i][j] = dato

    return matriz

def carga_distribuida(matriz:list, fila:int, columna:int):

    """
    Permite modificar un valor
    especifico de una matriz
    indicando fila y columna.
    """

    dato = input(f"Ingrese el nuevo valor de fila {fila} , columna {columna}: ")

    if es_numero(dato):
        matriz[fila][columna] = int(dato)
    else:
        matriz[fila][columna] = dato

#-------------------------------------------------------------------------------------------------------------------------------#



#Mostrar------------------------------------------------------------------------------------------------------------------------#

def mostrar_matriz(columnas:list, matriz:list):

    """
    Muestra por pantalla una
    matriz junto con los nombres
    de sus columnas.
    """

    print("|", end=" ")

    for i in range(len(columnas)):
        print(columnas[i], end=" | ")

    print()

    for i in range(len(matriz)):

        print("|", end=" ")

        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" | ")

        print()

def mostrar_fila(matriz:list, fila:int):

    """
    Muestra por pantalla una
    fila determinada de una
    matriz.
    """

    print("|", end=" ")

    for i in range(len(matriz[fila])):
        print(matriz[fila][i], end=" | ")

    print()

def mostrar_columna(matriz:list, columna:int):

    """
    Muestra por pantalla una
    columna determinada de
    una matriz.
    """

    for i in range(len(matriz)):
        print(matriz[i][columna])

def filtrar_contenido(matriz:list , fila:int , columna:int):

    """
    Muestra el contenido de una
    posicion especifica de la
    matriz indicando fila y
    columna.
    """

    print(f"Fila {fila} , columna {columna} = {matriz[fila][columna]}")

#----------------------------------------------------------------------------------------------------------------------------------#


#Modificacion----------------------------------------------------------------------------------------------------------------------#

def modificar_fila(matriz:list , fila:int):

    """
    Permite modificar todos los
    elementos de una fila
    determinada de la matriz.
    """

    for i in range(len(matriz[fila])):
        matriz[fila][i] = input(f"Ingrese el nuevo valor de la columna {i}: ")

def modificar_columna(matriz:list , columna:int):

    """
    Permite modificar todos los
    elementos de una columna
    determinada de la matriz.
    """

    for i in range (len(matriz)):
        matriz[i][columna] = input(f"Ingrese el nuevo valor de la fila {i}: ")

#-----------------------------------------------------------------------------------------------------------------------------------#
        
def es_columna_numerica(matriz:list, columna:int) -> bool:

    """
    Determina si todos los
    elementos de una columna
    son numericos.

    Retorno:
    true -> columna numerica.
    false -> columna NO numerica.
    """

    retorno = True

    for i in range(len(matriz)):
        if type(matriz[i][columna]) != int:
            retorno = False

    return retorno


def obtener_columna(matriz:list, columna:int) -> list:

    """
    Obtiene los elementos de una
    columna determinada de una
    matriz.

    Retorno:
    list -> elementos de la
    columna seleccionada.
    """

    lista = []

    for i in range(len(matriz)):
        lista.append(matriz[i][columna])

    return lista





