from paquete.matematicas import *
from paquete.validaciones import *


usuario1 = ""
contraseña1 = ""
usuario_creado = False
login = False

while login == False:

    cuenta = input("Ingrese 'registrarse' o 'iniciar sesion': ")

    while cuenta != "registrarse" and cuenta != "iniciar sesion":
        cuenta = input("Por favor , Ingrese 'registrarse' o 'iniciar sesion': ")

    if cuenta == "registrarse":
        usuario1 = input("Cree su nombre de usuario: ")
        contraseña1 = input("Cree su contraseña: ")
        usuario_creado = True
        print("Registro exitoso")
        print("Inicie sesion\n")
        usuario = input ("Ingrese su nombre de usuario: ") 
        contraseña = input ("Ingrese su contraseña: ") 
        
        while usuario != usuario1 or contraseña != contraseña1: 
            print ("Usuario o contraseña incorrectos , intente de nuevo")             
            usuario = input ("Ingrese su nombre de usuario: ")
            contraseña = input ("Ingrese su contraseña: ")
            
        print("Inicio de sesion exitoso")
        login = True
            

    elif cuenta == "iniciar sesion":
        if usuario_creado == False:
            print("No existen usuarios creados , debe registrarse primero")
        else:
            usuario = input("Ingrese su nombre de usuario: ")
            contraseña = input("Ingrese su contraseña: ")

            while usuario != usuario1 or contraseña != contraseña1:
                print("Usuario o contraseña incorrectos, intente de nuevo")
                usuario = input("Ingrese su nombre de usuario: ")
                contraseña = input("Ingrese su contraseña: ")

            print("Inicio de sesion exitoso")
            login = True


menu = 0
while menu != 6 :

    menu = int(input(
        "Menu De Seleccion: \n \n"
        "1) Proyectos \n" 
        "2) Tablas \n" 
        "3) Variables \n" 
        "4) Mostrar \n" 
        "5) Estadistica \n" 
        "6) Salir \n"))

    while validar_rango(menu , 1 , 6) == False:
        print("Valor invalido , Ingrese un valor correcto \n")
        menu = int(input(
            "Menu de seleccion: \n \n" 
            "1) Proyectos \n" 
            "2) Tablas \n" 
            "3) Variables \n" 
            "4) Mostrar \n" 
            "5) Estadistica \n" 
            "6) Salir \n"))


    if menu == 1:
        print("Generación y gestión de proyectos \n")

    elif menu == 2:
        print("Creación y modificación de tablas \n")

    elif menu == 3:
        print("Creación, carga y modificación de variables \n")

    elif menu == 4:
        print("Mostrar por pantalla información disponible en una tabla \n")

    elif menu == 5:
        print("Conteos o frecuencias. Máximos y mínimos. Medidas de tendencia central: promedios aritméticos y geométricos. Medidas de dispersión. Medidas de posición. \n")

    elif menu == 6:
        print("Finalizar la ejecución del programa \n")





