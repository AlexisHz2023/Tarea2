def visualizar_fecha():
    dia = int(input("Ingresa el número de día: "))
    mes = int(input("Ingresa el número de mes: "))
    año = int(input("Ingresa el número de año: "))

    dia_str = str(dia).rjust(2, '0')
    mes_str = str(mes).rjust(2, '0')
    año_str = str(año % 100).rjust(2, '0')

    print(f"{dia_str}/{mes_str}/{año_str}")

visualizar_fecha()
