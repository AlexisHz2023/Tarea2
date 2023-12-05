def matriz_identidad(n):
    matriz = [[0 for j in range(n)] for i in range(n)]
    
    for i in range(n):
        matriz[i][i] = 1
    
    return matriz

matriz = matriz_identidad(4)

for fila in matriz:
    print(fila)
