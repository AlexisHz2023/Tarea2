def potencia(x, n):
    if n == 0:
        return 1
    elif n < 0:
        x = 1 / x
        n = -n
    
    result = 1
    for _ in range(n):
        result *= x
    return result

# Ejemplo de uso:
x = 2
n = 3
resultado = potencia(x, n)
print(f"{x}^{n} = {resultado}")
