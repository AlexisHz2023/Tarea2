from datetime import datetime

def es_fecha_valida(fecha):
    try:
        datetime.strptime(fecha, '%Y-%m-%d')
        return True
    except ValueError:
        return False

fecha_ingresada = input("Ingresa una fecha en formato 'YYYY-MM-DD': ")

if es_fecha_valida(fecha_ingresada):
    print("La fecha ingresada es válida.")
else:
    print("La fecha ingresada no es válida.")
