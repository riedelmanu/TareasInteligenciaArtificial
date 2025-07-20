import numpy as np
import pandas as pd

# Función sigmoide y su derivada
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(y):
    return y * (1 - y)

# Factor de aprendizaje
eta = 0.1

# Pesos iniciales fijos (como punto A)
# W3: desde x0, x1, x2 hacia neurona oculta x3
W3 = np.array([1.5, 1.0, 1.0])

# W4: desde x0 (sesgo) y salida de x3 hacia neurona de salida x4
W4 = np.array([1.0, -2.0])

# Patrones (P1 y P2)
patrones = [
    {"nombre": "P1", "x": [1, 0, 1], "target": 1},  # XOR(0,1) = 1
    {"nombre": "P2", "x": [1, 1, 0], "target": 1}   # XOR(1,0) = 1
]

# Lista para guardar resultados
resultados = []

for patron in patrones:
    nombre = patron["nombre"]
    x = np.array([1] + patron["x"])  # Agregamos x0 = 1 (sesgo)
    t = patron["target"]

    # FORWARD PASS
    net3 = np.dot(W3, x[:3])  # x0, x1, x2 -> neurona oculta
    y3 = sigmoid(net3)

    net4 = W4[0] * 1 + W4[1] * y3  # x0 (sesgo) y salida y3
    y4 = sigmoid(net4)

    # BACKWARD PASS
    delta4 = (t - y4) * sigmoid_derivative(y4)
    delta3 = delta4 * W4[1] * sigmoid_derivative(y3)

    # Actualizar pesos
    W4 += eta * delta4 * np.array([1, y3])
    W3 += eta * delta3 * x[:3]

    resultados.append({
        "Patrón": nombre,
        "Entrada": x[1:].tolist(),
        "Salida esperada": t,
        "Salida obtenida": round(y4, 4),
        "Error": round(t - y4, 4),
        "Pesos W3 nuevos": np.round(W3, 4).tolist(),
        "Pesos W4 nuevos": np.round(W4, 4).tolist()
    })

# Mostrar resultados en tabla
df = pd.DataFrame(resultados)
print("\nResultados del ejercicio C (una iteración por patrón):\n")
print(df.to_string(index=False))