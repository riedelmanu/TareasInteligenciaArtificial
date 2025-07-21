#F. Separa los patrones P1= (1 0 1), P2=(1 1 0) y P3=(1 1 1) en 2 categorías usando para el algoritmo de aprendizaje no supervisado WTA. Los vectores de pesos iniciales deben ser aleatorios, así como el factor de aprendizaje usado. Razona por qué la red los ha agrupado de esa manera al finalizar el proceso de aprendizaje.

import numpy as np
import pandas as pd

# Semilla para reproducibilidad
np.random.seed(42)

# Patrones de entrada
patrones = {
    "P1": np.array([1, 0, 1]),
    "P2": np.array([1, 1, 0]),
    "P3": np.array([1, 1, 1])
}

# Convertir a matriz para procesar fácilmente
X = np.array(list(patrones.values()))

# Parámetros
n_clusters = 2  # 2 neuronas (categorías)
eta = np.random.uniform(0.1, 0.6)  # tasa de aprendizaje aleatoria
epochs = 10  # iteraciones de entrenamiento

# Pesos iniciales aleatorios
W = np.random.uniform(0, 1, (n_clusters, X.shape[1]))

# ENTRENAMIENTO WTA
for _ in range(epochs):
    for x in X:
        # Calcular distancia euclidiana a cada neurona
        distancias = np.linalg.norm(W - x, axis=1)
        winner = np.argmin(distancias)
        # Actualizar solo la neurona ganadora
        W[winner] += eta * (x - W[winner])

# ASIGNACIÓN FINAL de cada patrón a su categoría
asignaciones = {}
for nombre, x in patrones.items():
    distancias = np.linalg.norm(W - x, axis=1)
    winner = np.argmin(distancias)
    asignaciones[nombre] = f"Categoría {winner + 1}"

# Mostrar resultados
df_resultado = pd.DataFrame({
    "Patrón": list(asignaciones.keys()),
    "Vector": [x.tolist() for x in patrones.values()],
    "Categoría asignada": list(asignaciones.values())
})

pesos_finales = pd.DataFrame(W, columns=["w1", "w2", "w3"])
pesos_finales.index = ["Categoría 1", "Categoría 2"]

print("Factor de aprendizaje usado:", round(eta, 4))
print("\nAsignación de patrones:")
print(df_resultado.to_string(index=False))
print("\nPesos finales de cada categoría:")
print(pesos_finales)
