import sympy

def calcular_factorial(numero):
    if numero < 0:
        return "El factorial no está definido para números negativos"
    elif numero == 0:
        return 1
    else:
        factorial = sympy.factorial(numero)
        return factorial

numero = int(input("Ingresa un número para calcular su factorial (entre 100 y 1,000,000): "))

if 1 <= numero <= 1000000:
    resultado = calcular_factorial(numero)
    print(f"El factorial de {numero} es: {resultado}")
else:
    print("El número está fuera del rango permitido (100 a 1,000,000).")
