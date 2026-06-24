from .caracteres import *

def cargar_usuarios(ruta:str) -> list:

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

    archivo = open(ruta, "w")

    for usuario in usuarios:

        texto = usuario["usuario"]
        texto += ","
        texto += usuario["contraseña"]

        archivo.write(texto + "\n")

    archivo.close()

    

