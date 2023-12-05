def mcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mcd_cuatro_numeros(a, b, c, d):
    resultado1 = mcd(a, b)
    
    resultado2 = mcd(c, d)
    
    resultado_final = mcd(resultado1, resultado2)
    
    return resultado_final

# Ejemplo de uso
num1 = 24
num2 = 36
num3 = 48
num4 = 60

resultado = mcd_cuatro_numeros(num1, num2, num3, num4)
print(f"El MCD de {num1}, {num2}, {num3} y {num4} es: {resultado}")
