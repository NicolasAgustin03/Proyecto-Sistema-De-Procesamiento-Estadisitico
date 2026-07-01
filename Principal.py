from paquete import *

RUTA_USUARIOS ="archivos/usuarios.csv"

usuarios = cargar_usuarios(RUTA_USUARIOS)

RUTA_PROYECTOS = "archivos/proyectos.csv"

proyectos = cargar_proyectos(RUTA_PROYECTOS)

gestionar_login(
    usuarios,
    RUTA_USUARIOS
)

menu = 0

while menu != 6:

    menu = get_indice(
        "Menu De Seleccion: \n \n"
        "1) Proyectos \n"
        "2) Tablas \n"
        "3) Variables \n"
        "4) Mostrar \n"
        "5) Estadistica \n"
        "6) Salir \n",
        1,
        6
        )

    if menu == 1:
        print("Generación y gestión de proyectos\n")

        nombre = input("Ingrese el nombre del proyecto: ")

        proyecto = crear_proyecto(nombre)

        proyectos.append(proyecto)

        print("Proyecto creado correctamente")


    elif menu == 2:
        print("Creación y modificación de tablas\n")

        if len(proyectos) > 0:
        
            proyecto = seleccionar_proyecto(proyectos)

            crear_tabla_proyecto(proyecto)

            print(proyectos)

        else:
            print("No existen proyectos creados. Primero cree uno en el menu proyectos")
    

    elif menu == 3:
        print("Creación, carga y modificación de variables\n")
        
        if len(proyectos) > 0:

            proyecto = seleccionar_proyecto(proyectos)

            if len(proyecto["tablas"]) > 0:

                tabla = seleccionar_tabla(proyecto)

                gestionar_variables(tabla)

            else:

                print("El proyecto no posee tablas. Debe crear una desde el menú Tablas.")

        else:
            print("No existen proyectos creados. Primero cree uno en el menu proyectos")


    elif menu == 4:
        print("Mostrar por pantalla información disponible en una tabla\n")

        if len(proyectos) > 0:

            proyecto = seleccionar_proyecto(proyectos)

            if len(proyecto["tablas"]) > 0:

                tabla = seleccionar_tabla(proyecto)

                mostrar_informacion_tabla(tabla)

            else:

                print("El proyecto no posee tablas. Debe crear una desde el menú Tablas.")

        else:
            print("No existen proyectos creados. Primero cree uno en el menu proyectos")
            

    elif menu == 5:
        print("Conteos o frecuencias. Máximos y mínimos. Medidas de tendencia central: promedios aritméticos y geométricos. Medidas de dispersión. Medidas de posición.\n")
        
        if len(proyectos) > 0:

            proyecto = seleccionar_proyecto(proyectos)

            if len(proyecto["tablas"]) > 0:

                tabla = seleccionar_tabla(proyecto)

                gestionar_estadistica(tabla)

            else:

                print("El proyecto no posee tablas. Debe crear una desde el menú Tablas.")

        else:
            print("No existen proyectos creados. Primero cree uno en el menu proyectos")

   
    elif menu == 6:

        guardar_proyectos(
        proyectos,
        RUTA_PROYECTOS
    )
        
        print("Finalizo la ejecucion del programa\n")





