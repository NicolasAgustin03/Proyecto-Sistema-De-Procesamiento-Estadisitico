from paquete import *

usuario1 = ""
contraseña1 = ""
usuario_creado = False
login = False

while login == False:

    cuenta = input("Ingrese 'registrarse' o 'iniciar sesion': ")

    while cuenta != "registrarse" and cuenta != "iniciar sesion":
        cuenta = input("Por favor, ingrese 'registrarse' o 'iniciar sesion': ")

    if cuenta == "registrarse":

        datos_usuario = registrar_usuario()

        usuario1 = datos_usuario[0]
        contraseña1 = datos_usuario[1]

        print("Inicie sesion\n")

        iniciar_sesion (usuario1, contraseña1)

        usuario_creado = True

        login = True

    elif cuenta == "iniciar sesion":

        if usuario_creado == False:
            print("No existen usuarios creados, debe registrarse primero")

        else:

            iniciar_sesion(usuario1, contraseña1)

            login = True

tabla = []
nombre_columnas = []
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

    elif menu == 2:
        print("Creación y modificación de tablas\n")

        filas = get_int("Ingrese la cantidad de filas: ")

        while filas <= 0:
            print("Debe ingresar una cantidad mayor a 0")
            filas = get_int("Ingrese la cantidad de filas: ")
        
        
        columnas = get_int("Ingrese la cantidad de columnas: ")

        while columnas <= 0:
            print("Debe ingresar una cantidad mayor a 0")
            columnas = get_int("Ingrese la cantidad de columnas: ")
        

        nombre_columnas = crear_columnas(columnas)
        tabla = generar_matriz(filas , columnas , "")
        cargar_matriz(tabla)
    

    elif menu == 3:
        print("Creación, carga y modificación de variables\n")

        
        if len(tabla) == 0:
            print("No hay tablas creadas")

        else:

            menu_2 = 1

            while menu_2 != 4:
                menu_2 = get_indice("Menu: \n"
                                "1) Modificar fila\n" 
                                "2) Modificar columna\n"
                                "3) Carga distribuida\n"
                                "4) Salir\n",
                                1,
                                4)
                    
                match menu_2:

                    case 1:
                        mostrar_matriz(nombre_columnas,tabla)

                        fila = get_indice("Ingrese la fila: ",
                           0,
                           len(tabla)-1
                           )

                        modificar_fila(tabla , fila)

                    case 2:
                        mostrar_matriz(nombre_columnas,tabla)

                        columna = get_indice("Ingrese la columna: ",
                           0,
                           len(tabla[0])-1
                           )
                        
                        modificar_columna(tabla , columna)

                    case 3:
                        mostrar_matriz(nombre_columnas,tabla)

                        fila = get_indice("Ingrese la fila: ",
                           0,
                           len(tabla)-1
                           )
                        
                        columna = get_indice("Ingrese la columna: ",
                           0,
                           len(tabla[0])-1
                           )
                        
                        carga_distribuida (tabla , fila , columna)



    elif menu == 4:
        print("Mostrar por pantalla información disponible en una tabla\n")

        if len(tabla) == 0:
            print("No hay tablas creadas")

        else:
            mostrar_matriz(nombre_columnas,tabla)

            fila = get_indice("Ingrese la fila que desea visualizar: ",
                              0,
                              len(tabla)-1
                              )
            mostrar_fila(tabla , fila)

            columna = get_indice("Ingrese la columna que desea visualizar: ",
                                 0,
                                 len(tabla[0])-1
                                 )
            
            mostrar_columna(tabla , columna)

            fila = get_indice("Ingrese la fila que desea filtrar : ",
                              0,
                              len(tabla)-1
                              )
            
            columna = get_indice("Ingrese la columna que desea filtrar : ",
                                 0,
                                 len(tabla[0])-1
                                 )
            
            filtrar_contenido(tabla , fila , columna)



    elif menu == 5:
        print("Conteos o frecuencias. Máximos y mínimos. Medidas de tendencia central: promedios aritméticos y geométricos. Medidas de dispersión. Medidas de posición.\n")
        
        if len(tabla) == 0:
            print("No hay tablas creadas")
        else:
            menu_3 = 1

            while menu_3 != 6:

                menu_3 = get_indice("Menu: \n"
                                "1) Frecuencias\n" 
                                "2) Maximos y minimos\n"
                                "3) Promedio aritmetico\n"
                                "4) Promedio Geometrico\n" \
                                "5) Medidas de dispersion\n" \
                                "6) Salir\n",
                                1,
                                6)
                
                match menu_3:
                    case 1:
                        print("")

                    case 2:
                        for i in range(len(nombre_columnas)):
                            print(f"{i}) {nombre_columnas[i]}")
                        
                        columna = get_indice("Seleccione la columna:",
                                             0,
                                             len(nombre_columnas)-1
                                             )
                        
                        if es_columna_numerica(tabla , columna) == True:

                            lista_columna = obtener_columna(tabla , columna)

                            may = calcular_maximo(lista_columna)
                            men = calcular_minimo(lista_columna)

                            print(f"Maximo: {may}")
                            print(f"Men: {men}")

                        else:
                            print("La columna ingresada no es numerica")

                    case 3:
                        for i in range(len(nombre_columnas)):
                            print(f"{i}) {nombre_columnas[i]}")
                        
                        columna = get_indice("Seleccione la columna:",
                                             0,
                                             len(nombre_columnas)-1
                                             )
                        
                        if es_columna_numerica(tabla , columna) == True:

                            lista_columna = obtener_columna(tabla , columna)

                            promedio = calcular_promedio(lista_columna)

                            print(f"Promedio: {promedio}")

                        else:
                            print("La columna ingresada no es numerica")




                        


                
            
        
    elif menu == 6:
        print("Finalizar la ejecución del programa\n")





