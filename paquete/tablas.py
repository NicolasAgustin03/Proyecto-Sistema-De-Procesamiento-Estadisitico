from paquete.validaciones import es_numero

#Creacion-------------------------------------------------------------------------------------------------------------------------#

def generar_matriz(filas:int , columnas:int , default) -> list:

    matriz = []

    for i in range(filas):

        fila = []

        for j in range(columnas):
            fila.append(default)

        matriz.append(fila)
    
    return matriz

def crear_columnas(cantidad:int) -> list:

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

    dato = input(f"Ingrese el nuevo valor de fila {fila} , columna {columna}: ")

    if es_numero(dato):
        matriz[fila][columna] = int(dato)
    else:
        matriz[fila][columna] = dato

#-------------------------------------------------------------------------------------------------------------------------------#



#Mostrar------------------------------------------------------------------------------------------------------------------------#

def mostrar_matriz(columnas:list, matriz:list):

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

    print("|", end=" ")

    for i in range(len(matriz[fila])):
        print(matriz[fila][i], end=" | ")

    print()

def mostrar_columna(matriz:list, columna:int):

    for i in range(len(matriz)):
        print(matriz[i][columna])

def filtrar_contenido(matriz:list , fila:int , columna:int):
    print(f"Fila {fila} , columna {columna} = {matriz[fila][columna]}")

#----------------------------------------------------------------------------------------------------------------------------------#


#Modificacion----------------------------------------------------------------------------------------------------------------------#

def modificar_fila(matriz:list , fila:int):

    for i in range(len(matriz[fila])):
        matriz[fila][i] = input(f"Ingrese el nuevo valor de la columna {i}: ")

def modificar_columna(matriz:list , columna:int):
    for i in range (len(matriz)):
        matriz[i][columna] = input(f"Ingrese el nuevo valor de la fila {i}: ")

#-----------------------------------------------------------------------------------------------------------------------------------#
        
def es_columna_numerica(matriz:list, columna:int) -> bool:

    retorno = True

    for i in range(len(matriz)):
        if type(matriz[i][columna]) != int:
            retorno = False

    return retorno


def obtener_columna(matriz:list, columna:int) -> list:

    lista = []

    for i in range(len(matriz)):
        lista.append(matriz[i][columna])

    return lista



