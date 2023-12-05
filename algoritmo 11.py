def division_entera_y_resto(dividendo, divisor):
    cociente = 0
    while dividendo >= divisor:
        dividendo -= divisor
        cociente += 1
    return cociente, dividendo

dividendo = int(input("Ingrese el dividendo: "))
divisor = int(input("Ingrese el divisor: "))

cociente, resto = division_entera_y_resto(dividendo, divisor)
print(f"División entera: {cociente}")
print(f"Resto: {resto}")
