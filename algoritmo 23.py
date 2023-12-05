import csv

# Función para cargar la agenda desde un archivo CSV
def cargar_agenda(nombre_archivo):
    try:
        with open(nombre_archivo, mode='r') as archivo:
            lector = csv.reader(archivo)
            encabezados = next(lector)  # Leer la primera fila (encabezados)
            agenda = [fila for fila in lector]
            return agenda
    except FileNotFoundError:
        return []

# Nombre del archivo de la agenda
nombre_archivo = "agenda.csv"

# Cargar la agenda desde el archivo
agenda = cargar_agenda(nombre_archivo)

# Verificar si la agenda está vacía
if not agenda:
    print("La agenda está vacía.")
else:
    # Imprimir los encabezados
    print("Registros en la agenda:")
    print("Nombre | Dirección | Ciudad | Código Postal | Teléfono | Edad")
    
    # Iterar sobre los registros e imprimirlos
    for contacto in agenda:
        nombre, direccion, ciudad, codigo_postal, telefono, edad = contacto
        print(f"{nombre} | {direccion} | {ciudad} | {codigo_postal} | {telefono} | {edad}")
