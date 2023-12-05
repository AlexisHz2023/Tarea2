# Definir una estructura para representar un registro de la Agenda
class RegistroAgenda:
    def __init__(self, nombre, direccion, ciudad, codigo_postal, telefono, edad):
        self.nombre = nombre
        self.direccion = direccion
        self.ciudad = ciudad
        self.codigo_postal = codigo_postal
        self.telefono = telefono
        self.edad = edad

# Función para crear un archivo de Agenda de direcciones
def crear_agenda(agenda_file, registros):
    with open(agenda_file, 'w') as file:
        for registro in registros:
            file.write(f"{registro.nombre},{registro.direccion},{registro.ciudad},{registro.codigo_postal},{registro.telefono},{registro.edad}\n")

# Función para leer y mostrar los registros de la Agenda
def leer_agenda(agenda_file):
    with open(agenda_file, 'r') as file:
        for line in file:
            campos = line.strip().split(',')
            nombre, direccion, ciudad, codigo_postal, telefono, edad = campos
            print(f"Nombre: {nombre}")
            print(f"Dirección: {direccion}")
            print(f"Ciudad: {ciudad}")
            print(f"Código Postal: {codigo_postal}")
            print(f"Teléfono: {telefono}")
            print(f"Edad: {edad}")
            print("-----------")

# Función para copiar un archivo secuencial a un archivo directo
def copiar_archivo_secuencial_a_directo(secuencial_file, directo_file):
    with open(secuencial_file, 'r') as sec_file:
        with open(directo_file, 'w') as dir_file:
            for line in sec_file:
                dir_file.write(line)

# Ejemplo de uso
registros = [
    RegistroAgenda("Juan Pérez", "Calle A, 123", "Ciudad A", "12345", "555-123-456", 30),
    RegistroAgenda("María López", "Avenida B, 456", "Ciudad B", "67890", "555-789-123", 25),
    # Agrega más registros según sea necesario
]

agenda_file = "agenda.txt"
crear_agenda(agenda_file, registros)

print("Registros de la Agenda:")
leer_agenda(agenda_file)

secuencial_file = "archivo_secuencial.txt"
directo_file = "directo_agenda.txt"
copiar_archivo_secuencial_a_directo(secuencial_file, directo_file)
