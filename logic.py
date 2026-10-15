from datetime import datetime


def calcular_edad(fecha_nacimiento):
    hoy = datetime.now().date()
    cumplio_anios = (hoy.month, hoy.day) >= (fecha_nacimiento.month, fecha_nacimiento.day)
    edad == hoy.year - fecha_nacimiento.year
    
    if not cumplio_anios:
        edad -= 1
        
    return edad



