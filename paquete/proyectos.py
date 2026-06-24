from .validaciones import *

def crear_proyecto(nombre:str) -> dict:
    """
    Crea un proyecto vacío.

    Retorna:
    dict -> proyecto creado.
    """

    proyecto = {
        "nombre": nombre,
        "columnas": [],
        "tabla": []
    }

    return proyecto

def seleccionar_proyecto(proyectos:list) -> dict:

    for i in range(len(proyectos)):
        print(f"{i}) {proyectos[i]['nombre']}")

    indice = get_indice(
        "Seleccione el proyecto: ",
        0,
        len(proyectos)-1
    )

    return proyectos[indice]