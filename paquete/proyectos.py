from .validaciones import *

def crear_proyecto(nombre:str) -> dict:

    """
    Crea un proyecto vacio
    con el nombre ingresado.

    Retorno:
    dict -> proyecto creado.
    """

    proyecto = {
        "nombre": nombre,
        "tablas": []
    }

    return proyecto

def seleccionar_proyecto(proyectos:list) -> dict:

    """
    Permite seleccionar un
    proyecto de una lista
    de proyectos.

    Retorno:
    dict -> proyecto
    seleccionado.
    """

    for i in range(len(proyectos)):
        print(f"{i}) {proyectos[i]['nombre']}")

    indice = get_indice(
        "Seleccione el proyecto: ",
        0,
        len(proyectos)-1
    )

    return proyectos[indice]

def seleccionar_tabla(proyecto:dict) -> dict:

    """
    Permite seleccionar una
    tabla perteneciente a un
    proyecto.

    Retorno:
    dict -> tabla
    seleccionada.
    """

    tablas = proyecto["tablas"]

    for i in range(len(tablas)):
        print(f"{i}) {tablas[i]['nombre']}")

    indice = get_indice(
        "Seleccione la tabla: ",
        0,
        len(tablas)-1
    )

    return tablas[indice]