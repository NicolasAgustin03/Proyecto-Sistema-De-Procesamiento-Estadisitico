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

    