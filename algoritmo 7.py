import math

def coordenadas_polares_a_cartesianas(r, theta):
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    
    return x, y

# Ejemplo de uso
r = 5.0  # Radio
theta = 0.0  # Ángulo en radianes (en este caso, 0 radianes)

x, y = coordenadas_polares_a_cartesianas(r, theta)

print(f"Coordenadas cartesianas: ({x}, {y})")
