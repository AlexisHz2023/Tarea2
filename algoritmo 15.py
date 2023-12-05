def suma_diagonal_principal(matriz):
    if len(matriz) != 4 or len(matriz[0]) != 4:
        return "La matriz no es de 4x4"
    
    suma = 0
    for i in range(4):
        suma += matriz[i][i]
    
    return suma

matriz = []

print("Ingresa los elementos de la matriz 4x4:")

for i in range(4):
    fila = []
    for j in range(4):
        elemento = float(input(f"Elemento [{i}][{j}]: "))
        fila.append(elemento)
    matriz.append(fila)

resultado = suma_diagonal_principal(matriz)

if type(resultado) == str:
    print(resultado)
else:
    print(f"La suma de los elementos de la diagonal principal es: {resultado}")
