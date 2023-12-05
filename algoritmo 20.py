def convert_to_uppercase(text):
    return text.upper()

def convert_to_lowercase(text):
    return text.lower()

while True:
    text = input("Ingresa una cadena de texto (o presiona Enter para salir): ")
    
    if not text:
        break
    
    choice = input("Selecciona una opción (1 para convertir a mayúsculas, 2 para convertir a minúsculas): ")
    
    if choice == "1":
        uppercase_text = convert_to_uppercase(text)
        print(f"En mayúsculas: {uppercase_text}")
    
    elif choice == "2":
        lowercase_text = convert_to_lowercase(text)
        print(f"En minúsculas: {lowercase_text}")
    
    else:
        print("Opción no válida. Por favor, selecciona 1 o 2 para convertir el texto, o presiona Enter para salir.")
