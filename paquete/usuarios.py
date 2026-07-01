from .archivos import *

def registrar_usuario(usuarios:list) -> None:
    """
    Permite registrar un usuario
    y una contraseña.
    """

    usuario = input("Cree su nombre de usuario: ")
    contraseña = input("Cree su contraseña: ")

    nuevo_usuario = {
        "usuario": usuario,
        "contraseña": contraseña
    }

    usuarios.append(nuevo_usuario)

    print("Registro exitoso")

def iniciar_sesion(usuarios:list):
    """
    Permite iniciar sesion
    validando usuario y contraseña.
    """

    encontrado = False

    while encontrado == False:

        usuario = input("Ingrese su nombre de usuario: ")
        contraseña = input("Ingrese su contraseña: ")

        for i in range(len(usuarios)):

            if usuarios[i]["usuario"] == usuario and usuarios[i]["contraseña"] == contraseña:

                encontrado = True

        if encontrado == False:
            print("Usuario o contraseña incorrectos")

    print("Inicio de sesion exitoso")

def gestionar_login(usuarios:list, ruta:str) -> None:

    """
    Permite gestionar el inicio
    de sesion o el registro de
    un usuario. En caso de
    registrarse, guarda el nuevo
    usuario en el archivo y luego
    solicita iniciar sesion.
    """

    login = False

    while login == False:

        cuenta = input("Ingrese 'registrarse' o 'iniciar sesion': ")

        while cuenta != "registrarse" and cuenta != "iniciar sesion":
            cuenta = input("Por favor, ingrese 'registrarse' o 'iniciar sesion': ")

        if cuenta == "registrarse":

            registrar_usuario(usuarios)

            guardar_usuarios(
                usuarios,
                ruta
            )

            print("Inicie sesion\n")

            iniciar_sesion(usuarios)

            login = True

        elif cuenta == "iniciar sesion":

            if len(usuarios) == 0:

                print("No existen usuarios creados, debe registrarse primero")

            else:

                iniciar_sesion(usuarios)

                login = True

    