# Solicitar al usuario que ingrese el número de elementos de la lista
N = int(input("Ingrese la cantidad de elementos en la lista: "))

# Inicializar una lista vacía para almacenar los elementos
L = []

# Solicitar al usuario que ingrese los elementos uno por uno
for i in range(N):
    elemento = float(input(f"Ingrese el elemento {i+1}: "))
    L.append(elemento)

# Inicializar una variable para almacenar el valor máximo
maximo = L[0]  # Suponemos que el primer elemento es el máximo

# Recorrer la lista para encontrar el valor máximo
for elemento in L:
    if elemento > maximo:
        maximo = elemento

# Imprimir el valor máximo
print(f"El valor máximo en la lista es: {maximo}")
