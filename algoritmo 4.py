def encontrar_mayor(numero1, numero2):
    if numero1 > numero2:
        return numero1
    else:
        return numero2

# Ejemplo de uso
num1 = 25
num2 = 42
mayor = encontrar_mayor(num1, num2)
print(f"El número mayor entre {num1} y {num2} es {mayor}")
