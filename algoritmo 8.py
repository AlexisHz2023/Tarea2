def calcular_salario():
    horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))
    tarifa_por_hora = float(input("Ingrese la tarifa por hora: "))
    semanas_trabajadas = int(input("Ingrese la cantidad de semanas trabajadas: "))
    
    # Definir las horas normales y las horas extras
    horas_normales = min(horas_trabajadas, 40)  # Hasta 40 horas se consideran normales
    horas_extra = max(horas_trabajadas - 40, 0)  # Horas que superan las 40 se consideran extras
    
    # Calcular el salario total incluyendo las semanas trabajadas
    salario_ordinario = horas_normales * tarifa_por_hora
    salario_extra = horas_extra * 1.5 * tarifa_por_hora
    salario_semanal = salario_ordinario + salario_extra
    salario_total = salario_semanal * semanas_trabajadas
    
    return salario_total

# Llamamos a la función para calcular el salario
salario = calcular_salario()
print(f"El salario total es: ${salario:.2f}")
