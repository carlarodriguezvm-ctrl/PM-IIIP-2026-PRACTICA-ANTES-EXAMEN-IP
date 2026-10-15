from datetime import datetime


def calcular_edad(fecha_nacimiento):
    # Obtenemos la fecha actual sin incluir la hora.
    hoy = datetime.now().date()

    # Calculamos la diferencia entre el año actual y el año de nacimiento.
    edad = hoy.year - fecha_nacimiento.year

    # Comprobamos si la persona todavía no ha cumplido años este año.
    if (hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        edad -= 1

    # Devolvemos la edad calculada.
    return edad