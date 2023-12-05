# Función para modificar un registro en el archivo secuencial
def modificar_registro_secuencial(archivo_secuencial, identificador, nuevos_datos):
    with open(archivo_secuencial, 'r') as file_original, open("temporal.txt", 'w') as file_temporal:
        encontrado = False
        for linea in file_original:
            campos = linea.strip().split(',')
            nombre = campos[0]  # Suponemos que el nombre es el identificador único
            if nombre == identificador:
                # Modificar el registro con los nuevos datos introducidos por el usuario
                file_temporal.write(','.join(nuevos_datos) + '\n')
                encontrado = True
            else:
                # Copiar el registro tal como está al archivo temporal
                file_temporal.write(linea)
        
        if not encontrado:
            print(f"No se encontró el registro con nombre '{identificador}'.")
    
    # Reemplazar el archivo original con el archivo temporal
    import os
    os.replace("temporal.txt", archivo_secuencial)

# Ejemplo de uso
archivo_secuencial = "agenda_secuencial.txt"
identificador_a_modificar = input("Introduce el nombre del registro a modificar: ")
nuevos_datos = input("Introduce los nuevos datos en el formato: Nombre,Dirección,Ciudad,Código Postal,Teléfono,Edad\n").split(',')

modificar_registro_secuencial(archivo_secuencial, identificador_a_modificar, nuevos_datos)
