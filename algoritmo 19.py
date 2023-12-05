def arabic_to_roman(arabic):
    if not (0 < arabic < 4000):
        return "El número debe estar entre 1 y 3999"
    roman_numerals = {
        1: "I", 4: "IV", 5: "V", 9: "IX",
        10: "X", 40: "XL", 50: "L", 90: "XC",
        100: "C", 400: "CD", 500: "D", 900: "CM",
        1000: "M"
    }
    result = ""
    for value, numeral in sorted(roman_numerals.items(), reverse=True):
        while arabic >= value:
            result += numeral
            arabic -= value
    return result

def roman_to_arabic(roman):
    roman_numerals = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000
    }
    arabic = 0
    prev_value = 0
    for numeral in reversed(roman):
        value = roman_numerals.get(numeral, 0)
        if value < prev_value:
            arabic -= value
        else:
            arabic += value
        prev_value = value
    return arabic

while True:
    choice = input("Selecciona una opción (1 para convertir de árabe a romano, 2 para convertir de romano a árabe, 0 para salir): ")
    
    if choice == "0":
        break
    
    if choice == "1":
        arabic = int(input("Ingresa un número arábigo: "))
        roman = arabic_to_roman(arabic)
        print(f"Número romano: {roman}")
    
    elif choice == "2":
        roman = input("Ingresa un número romano (mayúsculas): ")
        arabic = roman_to_arabic(roman)
        print(f"Número arábigo: {arabic}")
    
    else:
        print("Opción no válida. Por favor, selecciona 1, 2 o 0 para salir.")
