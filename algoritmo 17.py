nombres = input("Ingrese los nombres de los estudiantes (separados por comas): ").split(',')
nombres = [nombre.strip() for nombre in nombres]

calificaciones = input("Ingrese las calificaciones de los estudiantes (separadas por comas): ").split(',')
calificaciones = [float(calificacion) for calificacion in calificaciones]

media = sum(calificaciones) / len(calificaciones)

print(f"La calificación media es: {media:.2f}")

print("Diferencia con la media para cada estudiante:")
for i in range(len(nombres)):
    diferencia = calificaciones[i] - media
    print(f"{nombres[i]}: {calificaciones[i]:.2f}, Diferencia: {diferencia:.2f}")
