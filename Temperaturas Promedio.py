def calcular_promedio_temperaturas(ciudades, temperaturas):
    """
    Función que calcula y muestra el promedio de temperatura semanal de múltiples ciudades.

    Parámetros:
    - ciudades: Lista con los nombres de las ciudades.
    - temperaturas: Lista tridimensional con las temperaturas por día, semana y ciudad.

    La función imprime el promedio de temperatura por semana para cada ciudad y el promedio total de cada ciudad.
    """
    # Obtener el número de ciudades, semanas y días
    num_ciudades = len(temperaturas)
    num_semanas = len(temperaturas[0])
    num_dias = len(temperaturas[0][0])

    # Recorrer la matriz de temperaturas y calcular los promedios
    for ciudad in range(num_ciudades):
        print(f"Ciudad: {ciudades[ciudad]}")
        suma_total_temperaturas_ciudad = 0

        for semana in range(num_semanas):
            suma_temperaturas_semana = 0

            for dia in range(num_dias):
                suma_temperaturas_semana += temperaturas[ciudad][semana][dia]

            # Calcular el promedio para la semana
            promedio_semana = suma_temperaturas_semana / num_dias
            print(f"  Semana {semana + 1} - Promedio de temperatura: {promedio_semana:.2f}°C")

            # Sumar las temperaturas de la semana a la suma total de la ciudad
            suma_total_temperaturas_ciudad += suma_temperaturas_semana

        # Calcular el promedio total para la ciudad
        promedio_ciudad = suma_total_temperaturas_ciudad / (num_semanas * num_dias)
        print(f"Promedio total para {ciudades[ciudad]}: {promedio_ciudad:.2f}°C\n")


# Datos de ejemplo con 3 ciudades y 4 semanas
ciudades = ["Puyo", "Tena", "Quito"]
temperaturas = [
    [  # Ciudad: Puyo
        [30, 32, 29, 28, 31, 33, 30],  # Semana 1
        [31, 30, 30, 29, 32, 34, 29],  # Semana 2
        [29, 30, 31, 32, 30, 29, 31],  # Semana 3
        [28, 29, 30, 31, 32, 33, 30]   # Semana 4
    ],
    [  # Ciudad: Tena
        [25, 26, 27, 28, 29, 27, 26],  # Semana 1
        [24, 23, 25, 26, 28, 27, 25],  # Semana 2
        [26, 28, 29, 30, 27, 26, 28],  # Semana 3
        [25, 26, 27, 28, 29, 30, 31]   # Semana 4
    ],
    [  # Ciudad: Quito
        [20, 21, 22, 21, 23, 22, 24],  # Semana 1
        [21, 22, 23, 24, 22, 21, 20],  # Semana 2
        [23, 24, 25, 26, 24, 23, 22],  # Semana 3
        [22, 23, 21, 24, 22, 23, 25]   # Semana 4
    ]
]

# Llamar a la función para calcular y mostrar el promedio de temperaturas
calcular_promedio_temperaturas(ciudades, temperaturas)
