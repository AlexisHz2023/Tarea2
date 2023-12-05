def contar_elementos_positivos():
    entrada = input("Ingresa una lista de números separados por espacios: ")

    numeros = [float(x) for x in entrada.split()]

    contador_positivos = 0

    for numero in numeros:
        if numero > 0:
            contador_positivos += 1

    return contador_positivos

positivos = contar_elementos_positivos()
print(f"El número de elementos positivos en la lista es: {positivos}")
