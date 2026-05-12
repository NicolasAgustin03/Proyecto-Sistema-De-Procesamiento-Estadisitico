def validar_rango(num:int , minimo:int , maximo:int) -> bool:
    if num >= minimo and num <= maximo:
        return True
    else:
        return False
    
num = validar_rango(4 , 2 , 7)
