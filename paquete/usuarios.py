def registrar_usuario() -> list:
    """
    Permite registrar un usuario
    y una contraseña.
    """

    datos_usuario = []

    usuario = input("Cree su nombre de usuario: ")
    contraseña = input("Cree su contraseña: ")

    datos_usuario.append(usuario)
    datos_usuario.append(contraseña)

    print("Registro exitoso")

    return datos_usuario

def iniciar_sesion(usuario_registrado:str, contraseña_registrada:str):
    """
    Permite iniciar sesion
    validando usuario y contraseña.
    """

    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    while usuario != usuario_registrado or contraseña != contraseña_registrada:

        print("Usuario o contraseña incorrectos, intente de nuevo")

        usuario = input("Ingrese su nombre de usuario: ")
        contraseña = input("Ingrese su contraseña: ")

    print("Inicio de sesion exitoso")

    