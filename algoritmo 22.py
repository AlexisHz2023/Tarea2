import csv

# Función para agregar un nuevo contacto a la agenda
def agregar_contacto(agenda, nombre, direccion, ciudad, codigo_postal, telefono, edad):
    nuevo_contacto = [nombre, direccion, ciudad, codigo_postal, telefono, edad]
    agenda.append(nuevo_contacto)

# Función para guardar la agenda en un archivo CSV
def guardar_agenda(agenda, nombre_archivo):
    with open(nombre_archivo, mode='w', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["Nombre", "Dirección", "Ciudad", "Código Postal", "Teléfono", "Edad"])
        escritor.writerows(agenda)

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

# Ejemplo de uso
nombre_archivo = "agenda.csv"
agenda = cargar_agenda(nombre_archivo)

# Agregar un nuevo contacto
nombre = "Ejemplo Persona"
direccion = "123 Calle Ejemplo"
ciudad = "Ejemplolandia"
codigo_postal = "12345"
telefono = "555-123-4567"
edad = 30
agregar_contacto(agenda, nombre, direccion, ciudad, codigo_postal, telefono, edad)

# Guardar la agenda en el archivo
guardar_agenda(agenda, nombre_archivo)
