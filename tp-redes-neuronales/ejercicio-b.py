# Supongamos que tenemos que separar los puntos P1=(1,1), P2=(1,0), P3=(0,1) a través de la función f(x,y) = 3x+2y > 2 (es decir, devuelve 1 si se cumple la desigualdad y 0 si no la cumple). Para ello construye un perceptrón simple y utiliza como función de activación la función sigmoide, una función de aprendizaje basada en la Regla Delta generalizada y un factor de aprendizaje e = 0.5 . Asigna valores aleatorios y pequeños, tanto positivos como negativos a los pesos sinápticos. Realiza sólo una iteración para cada uno de los patrones de entrada.

import numpy as np
import pandas as pd

# Semilla para resultados reproducibles
np.random.seed(42)

# Función sigmoide y su derivada
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(y):
    return y * (1 - y)

# Patrones de entrada y salidas deseadas según f(x, y) = 3x + 2y > 2
datos = [
    {"x": [1, 1, 1], "target": 1},  # P1 = (1,1)
    {"x": [1, 1, 0], "target": 1},  # P2 = (1,0)
    {"x": [1, 0, 1], "target": 1}   # P3 = (0,1)
]

# Factor de aprendizaje
eta = 0.5

# Pesos iniciales aleatorios pequeños (incluye sesgo w0)
W = np.random.uniform(-0.5, 0.5, 3)

# Lista para registrar resultados
resultados = []

# Iterar sobre cada patrón una vez
for i, dato in enumerate(datos):
    x = np.array(dato["x"])      # [x0, x1, x2]
    t = dato["target"]

    # Forward pass
    net = np.dot(W, x)
    y = sigmoid(net)

    # Backward pass (Regla Delta generalizada)
    error = t - y
    delta = error * sigmoid_derivative(y)

    # Actualización de pesos
    W = W + eta * delta * x

    # Guardar resultados
    resultados.append({
        "Patrón": f"P{i+1}",
        "Entrada": x.tolist(),
        "Salida esperada": t,
        "Salida obtenida": round(y, 4),
        "Error": round(error, 4),
        "Pesos nuevos": np.round(W, 4).tolist()
    })

# Mostrar resultados en consola
df = pd.DataFrame(resultados)
print("\nResultados del Perceptrón Simple:\n")
print(df.to_string(index=False))
