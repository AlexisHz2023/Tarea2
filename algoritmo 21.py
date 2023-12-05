def es_palindromo(cadena):
    cadena = cadena.replace(" ", "").lower()
    
    return cadena == cadena[::-1]

cadena = "Anilina"
if es_palindromo(cadena):
    print(f"'{cadena}' es un palíndromo.")
else:
    print(f"'{cadena}' no es un palíndromo.")
