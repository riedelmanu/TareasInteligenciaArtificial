#E. Se cree que los niños aprenden mediante un proceso llamado razonamiento por analogías, en el que intentan asociar objetos parecidos a otros que ya conocen, y los intentan agrupar por categorías. Supón que un niño ha visto alguna vez un león en el zoo y que sabe que es peligroso, y lo ha representado internamente por el patrón (1,1,0,1,0) Un día va por la calle y se encuentra a un gato, que representaremos por el patrón (1,1,1,0,1) ¿Debe salir corriendo el niño porque crea al verlo que se parece demasiado a un león? Modela ésta situación (el aprendizaje del león y después del gato) mediante un perceptrón multicapa y mediante un algoritmo de aprendizaje no supervisado.


import numpy as np
import pandas as pd

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(y):
    return y * (1 - y)

# Datos de entrenamiento: solo el león
x_leon = np.array([1, 1, 1, 0, 1, 0])  # x0 (sesgo) + patrón
t_leon = 1  # peligroso

# Patrón del gato para probar después
x_gato = np.array([1, 1, 1, 1, 0, 1])  # x0 + patrón

# Pesos iniciales
np.random.seed(0)
W_hidden = np.random.uniform(-0.5, 0.5, (3, 6))  # 3 neuronas ocultas, 6 entradas
W_output = np.random.uniform(-0.5, 0.5, 4)       # 3 salidas ocultas + sesgo

# Parámetros
eta = 0.5
epochs = 10  # pocas épocas para simular el aprendizaje del niño

# Entrenamiento
for _ in range(epochs):
    # FORWARD
    net_hidden = W_hidden @ x_leon
    y_hidden = sigmoid(net_hidden)
    y_hidden_biased = np.insert(y_hidden, 0, 1)  # agregar bias

    net_output = np.dot(W_output, y_hidden_biased)
    y_output = sigmoid(net_output)

    # BACKWARD
    error = t_leon - y_output
    delta_output = error * sigmoid_derivative(y_output)
    delta_hidden = delta_output * W_output[1:] * sigmoid_derivative(y_hidden)

    # Actualizar pesos
    W_output += eta * delta_output * y_hidden_biased
    W_hidden += eta * np.outer(delta_hidden, x_leon)

# TEST: ¿qué pasa con el gato?
net_hidden_gato = W_hidden @ x_gato
y_hidden_gato = sigmoid(net_hidden_gato)
y_hidden_gato_biased = np.insert(y_hidden_gato, 0, 1)

net_output_gato = np.dot(W_output, y_hidden_gato_biased)
y_output_gato = sigmoid(net_output_gato)

print(f"Salida obtenida para el gato (probabilidad de peligro): {y_output_gato:.4f}")
