#Considera los siguientes 3 ejemplos. Construye un perceptrón multicapa con una unidad en la capa oculta. Realiza una sólo iteración para todos los patrones, suponiendo un valor umbral de 4, unos pesos iniciales wij=1 y un factor de aprendizaje = 0.6. Utiliza también una función de activación sigmoide y la regla delta generalizada como regla de aprendizaje. ¿Cuáles son los pesos finales? *ver tabla*

import numpy as np
import pandas as pd

# Función sigmoide y su derivada
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(y):
    return y * (1 - y)

# Datos de entrada (incluye sesgo x0=1)
datos = [
    {"x": [1, 1, 0, 1, 0], "target": 1},  # +
    {"x": [1, 0, 1, 0, 0], "target": 0},  # -
    {"x": [1, 0, 0, 1, 1], "target": 1}   # +
]

# Factor de aprendizaje y umbral (bias negativo)
eta = 0.6
umbral = 4

# Inicialización de pesos: todos en 1
# Capa entrada -> oculta (1 neurona oculta, 5 entradas incluyendo x0)
W_hidden = np.ones(5)

# Capa oculta -> salida (1 entrada desde la neurona oculta + sesgo)
W_output = np.ones(2)

# Lista para almacenar resultados
resultados = []

# Entrenamiento: una sola iteración por patrón
for i, patron in enumerate(datos):
    x = np.array(patron["x"])          # x0, x1, x2, x3, x4
    t = patron["target"]

    # FORWARD: capa oculta
    net_h = np.dot(W_hidden, x) - umbral
    y_h = sigmoid(net_h)

    # FORWARD: capa salida
    x_salida = np.array([1, y_h])       # sesgo + salida de oculta
    net_o = np.dot(W_output, x_salida)
    y_o = sigmoid(net_o)

    # BACKWARD
    error = t - y_o
    delta_o = error * sigmoid_derivative(y_o)
    delta_h = delta_o * W_output[1] * sigmoid_derivative(y_h)

    # ACTUALIZACIÓN DE PESOS
    W_output += eta * delta_o * x_salida
    W_hidden += eta * delta_h * x

    resultados.append({
        "Patrón": f"P{i+1}",
        "Entrada": x.tolist()[1:],  # Sin x0
        "Salida esperada": t,
        "Salida obtenida": round(y_o, 4),
        "Error": round(error, 4),
        "Pesos capa oculta": np.round(W_hidden, 4).tolist(),
        "Pesos capa salida": np.round(W_output, 4).tolist()
    })

df = pd.DataFrame(resultados)
print("\nResultados del ejercicio D (una iteración por patrón):\n")
print(df.to_string(index=False))