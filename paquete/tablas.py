from paquete.validaciones import es_numero
from .validaciones import *

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

def crear_tabla_proyecto(proyecto:dict):

    nombre_tabla = input("Ingrese el nombre de la tabla: ")

    filas = get_int("Ingrese la cantidad de filas: ")

    while filas <= 0:
        print("Debe ingresar una cantidad mayor a 0")
        filas = get_int("Ingrese la cantidad de filas: ")

    columnas = get_int("Ingrese la cantidad de columnas: ")

    while columnas <= 0:
        print("Debe ingresar una cantidad mayor a 0")
        columnas = get_int("Ingrese la cantidad de columnas: ")

    nombre_columnas = crear_columnas(columnas)

    tabla = generar_matriz(filas, columnas, "")

    cargar_matriz(tabla, nombre_columnas)

    nueva_tabla = {
        "nombre": nombre_tabla,
        "nombre_columnas": nombre_columnas,
        "tabla": tabla
    }

    proyecto["tablas"].append(nueva_tabla)

    print("Tabla creada correctamente")



#---------------------------------------------------------------------------------------------------------------------------------#



#Cargas---------------------------------------------------------------------------------------------------------------------------#

def cargar_matriz(matriz:list , nombre_columnas:list) -> list:

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

            dato = input(f"Ingrese el valor de {nombre_columnas[j]} {i+1}: ")

            while dato == "":
                dato = input(
                    f"No se acepta cadena vacia. Ingrese el valor de fila {i}, columna {j}: "
                )

            if es_numero(dato) == True:
                matriz[i][j] = int(dato)
            else:
                matriz[i][j] = dato

    return matriz

def cargar_distribuido(matriz:list, fila:int, columna:int):

    """
    Permite modificar un valor
    especifico de una matriz
    indicando fila y columna.
    """

    dato = input(f"Ingrese el nuevo valor de fila {fila}, columna {columna}: ")

    while dato == "":
        dato = input(f"No se acepta cadena vacia. Ingrese el nuevo valor de fila {fila}, columna {columna}: ")

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

def mostrar_informacion_tabla(proyecto:dict):

    """
    Permite visualizar la
    informacion de una tabla,
    mostrando la tabla completa,
    una fila, una columna o el
    contenido de una posicion
    especifica.
    """

    nombre_columnas = proyecto["nombre_columnas"]
    tabla = proyecto["tabla"]

    mostrar_matriz(nombre_columnas,tabla)

    submenu_2 = 1

    while submenu_2 != 4:

                submenu_2 = get_indice("Menu: \n"
                                "1) Visualizar fila\n" 
                                "2) Visualizar columna\n"
                                "3) Filtrar Contenido\n" 
                                "4) Volver al menu principal\n",
                                1,
                                4)
                
                match submenu_2:

                    case 1:

                        fila = get_indice("Ingrese la fila que desea visualizar: ",
                              0,
                              len(tabla)-1
                              )
                        mostrar_fila(tabla , fila)

                    case 2:

                        columna = get_indice("Ingrese la columna que desea visualizar: ",
                                 0,
                                 len(tabla[0])-1
                                 )
            
                        mostrar_columna(tabla , columna)

                    case 3:

                        fila = get_indice("Ingrese la fila que desea filtrar : ",
                              0,
                              len(tabla)-1
                              )
            
                        columna = get_indice("Ingrese la columna que desea filtrar : ",
                                 0,
                                 len(tabla[0])-1
                                 )
            
                        filtrar_contenido(tabla , fila , columna)
            


#----------------------------------------------------------------------------------------------------------------------------------#


#Modificacion----------------------------------------------------------------------------------------------------------------------#

def modificar_fila(matriz:list , fila:int):

    """
    Permite modificar todos los
    elementos de una fila
    determinada de la matriz.
    """

    for i in range(len(matriz[fila])):

        dato = input(f"Ingrese el nuevo valor de la columna {i}: ")

        while dato == "":
            dato = input(f"No se acepta cadena vacía. Ingrese el nuevo valor de la columna {i}: ")

        if es_numero(dato):
            matriz[fila][i] = int(dato)
        else:
            matriz[fila][i] = dato

def modificar_columna(matriz:list , columna:int):

    """
    Permite modificar todos los
    elementos de una columna
    determinada de la matriz.
    """

    for i in range(len(matriz)):

        dato = input(f"Ingrese el nuevo valor de la fila {i}: ")

        while dato == "":
            dato = input(f"No se acepta cadena vacia. Ingrese el nuevo valor de la fila {i}: ")

        if es_numero(dato):
            matriz[i][columna] = int(dato)
        else:
            matriz[i][columna] = dato

def gestionar_variables(proyecto:dict):

    """
    Permite gestionar la
    modificacion de los datos
    de una tabla, pudiendo
    modificar filas completas,
    columnas completas o un
    valor especifico.
    """

    nombre_columnas = proyecto["nombre_columnas"]
    tabla = proyecto["tabla"]

    submenu = 1

    while submenu != 4:

        submenu = get_indice(
            "Menu: \n"
            "1) Modificar fila\n"
            "2) Modificar columna\n"
            "3) Carga distribuida\n"
            "4) Salir\n",
            1,
            4
        )

        match submenu:

            case 1:

                mostrar_matriz(nombre_columnas, tabla)

                fila = get_indice(
                    "Ingrese la fila: ",
                    0,
                    len(tabla) - 1
                )

                modificar_fila(tabla, fila)

                mostrar_matriz(nombre_columnas, tabla)

            case 2:

                mostrar_matriz(nombre_columnas, tabla)

                columna = get_indice(
                    "Ingrese la columna: ",
                    0,
                    len(tabla[0]) - 1
                )

                modificar_columna(tabla, columna)

                mostrar_matriz(nombre_columnas, tabla)

            case 3:

                mostrar_matriz(nombre_columnas, tabla)

                fila = get_indice(
                    "Ingrese la fila: ",
                    0,
                    len(tabla) - 1
                )

                columna = get_indice(
                    "Ingrese la columna: ",
                    0,
                    len(tabla[0]) - 1
                )

                cargar_distribuido(tabla, fila, columna)

                mostrar_matriz(nombre_columnas, tabla)

#-----------------------------------------------------------------------------------------------------------------------------------#
        

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

def seleccionar_columna(nombre_columnas:list) -> int:

    """
    Permite seleccionar una
    columna de una tabla a
    partir de su indice.

    Retorno:
    int -> indice de la
    columna seleccionada.
    """

    for i in range(len(nombre_columnas)):
        print(f"{i}) {nombre_columnas[i]}")

    columna = get_indice(
        "Seleccione la columna: ",
        0,
        len(nombre_columnas)-1
    )

    return columna


    





