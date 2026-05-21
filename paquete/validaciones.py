def validar_rango(num:int , minimo:int , maximo:int) -> bool:
    """
    Determina si un numero se encuentra
    entre un valor minimo y un valor maximo.
    
    """
    if num >= minimo and num <= maximo:
        return True
    else:
        return False
    

