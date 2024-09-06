# Inicialización de la matriz 3D con temperaturas para las ciudades Puyo y Tena
# La estructura es [ciudades][semanas][días]

ciudades = ["Puyo", "Tena"]
temperaturas = [
    [  # Ciudad: Puyo
        [30, 32, 29, 28, 31, 33, 30],  # Semana 1
        [31, 30, 30, 29, 32, 34, 29]  # Semana 2
    ],
    [  # Ciudad: Tena
        [25, 26, 27, 28, 29, 27, 26],  # Semana 1
        [24, 23, 25, 26, 28, 27, 25]  # Semana 2
    ]
]

# Obtener el número de ciudades, semanas y días
num_ciudades = len(temperaturas)
num_semanas = len(temperaturas[0])
num_dias = len(temperaturas[0][0])

# Recorrer la matriz y calcular los promedios
for ciudad in range(num_ciudades):
    print(f"Ciudad: {ciudades[ciudad]}")

    for semana in range(num_semanas):
        suma_temperaturas = 0

        for dia in range(num_dias):
            suma_temperaturas += temperaturas[ciudad][semana][dia]

        # Calcular el promedio para la semana
        promedio = suma_temperaturas / num_dias
        print(f"  Semana {semana + 1} - Promedio de temperatura: {promedio:.2f}°C")
