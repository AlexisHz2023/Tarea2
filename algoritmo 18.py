# Definir las palabras que deseas contar
palabras_a_contar = ['a', 'an', 'and']

# Crear un diccionario para almacenar el recuento de cada palabra
recuento_palabras = {palabra: 0 for palabra in palabras_a_contar}

# Solicitar al usuario que ingrese el texto línea por línea
texto = ""
while True:
    linea = input("Ingresa una línea de texto (o presiona Enter para finalizar): ")
    if not linea:
        break
    texto += linea + "\n"

# Dividir el texto en palabras
palabras = texto.split()

for palabra in palabras:
    palabra = palabra.strip('.,?!()[]{}":;')
    if palabra in recuento_palabras:
        recuento_palabras[palabra] += 1

for palabra, recuento in recuento_palabras.items():
    print(f"'{palabra}' aparece {recuento} veces.")
