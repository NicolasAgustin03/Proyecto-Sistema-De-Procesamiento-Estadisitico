from .caracteres import *
from .validaciones import *

def cargar_usuarios(ruta:str) -> list:

    """
    Carga los usuarios
    almacenados en un
    archivo CSV.

    Retorno:
    list -> lista de
    usuarios cargados.
    """

    lista_usuarios = []

    with open(ruta) as archivo:

        for linea in archivo:

            palabras = separar(linea)

            usuario = {
                "usuario": palabras[0],
                "contraseña": palabras[1]
            }

            lista_usuarios.append(usuario)

    return lista_usuarios

def guardar_usuarios(usuarios:list, ruta:str):

    """
    Guarda la informacion
    de los usuarios en
    un archivo CSV.
    """

    archivo = open(ruta, "w")

    for usuario in usuarios:

        texto = usuario["usuario"]
        texto += ","
        texto += usuario["contraseña"]

        archivo.write(texto + "\n")

    archivo.close()

    

def cargar_proyectos(ruta:str) -> list:

    """
    Carga los proyectos y
    sus tablas desde un
    archivo CSV.

    Retorno:
    list -> lista de
    proyectos cargados.
    """

    lista_proyectos = []

    with open(ruta) as archivo:

        for linea in archivo:

            datos = separar(linea)

            nombre_proyecto = datos[0]
            nombre_tabla = datos[1]

            nombre_columnas = separar(datos[2], "|")

            tabla = []

            filas = separar(datos[3], ";")

            for fila in filas:

                fila_actual = separar(fila, "|")

                for i in range(len(fila_actual)):

                    if es_numero(fila_actual[i]) == True:

                        fila_actual[i] = int(fila_actual[i])

                tabla.append(fila_actual)

            nueva_tabla = {
                "nombre": nombre_tabla,
                "nombre_columnas": nombre_columnas,
                "tabla": tabla
            }

            existe = False

            for proyecto in lista_proyectos:

                if proyecto["nombre"] == nombre_proyecto:

                    proyecto["tablas"].append(nueva_tabla)

                    existe = True

            if existe == False:

                proyecto = {
                    "nombre": nombre_proyecto,
                    "tablas": [nueva_tabla]
                }

                lista_proyectos.append(proyecto)

    return lista_proyectos

def guardar_proyectos(proyectos:list, ruta:str):

    """
    Guarda los proyectos
    y sus tablas en un
    archivo CSV.
    """

    archivo = open(ruta, "w")

    for proyecto in proyectos:

        for tabla in proyecto["tablas"]:

            texto = ""

            texto += proyecto["nombre"]
            texto += ","

            texto += tabla["nombre"]
            texto += ","

            for i in range(len(tabla["nombre_columnas"])):

                texto += tabla["nombre_columnas"][i]

                if i < len(tabla["nombre_columnas"]) - 1:
                    texto += "|"

            texto += ","

            for i in range(len(tabla["tabla"])):

                fila = tabla["tabla"][i]

                for j in range(len(fila)):

                    texto += str(fila[j])

                    if j < len(fila) - 1:
                        texto += "|"

                if i < len(tabla["tabla"]) - 1:
                    texto += ";"

            archivo.write(texto + "\n")

    archivo.close()

    

