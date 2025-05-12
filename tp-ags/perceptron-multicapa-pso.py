import numpy as np

# Función de activación sigmoide
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivada de la función sigmoide
def sigmoid_derivative(x):
    return x * (1 - x)

# Función de costo (error cuadrático medio)
def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

# Red Neuronal Perceptrón Multicapa
class MLP:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        # Inicialización aleatoria de los pesos
        self.weights_input_hidden = np.random.randn(input_size, hidden_size)
        self.weights_hidden_output = np.random.randn(hidden_size, output_size)
    
    def forward(self, X):
        # Propagación hacia adelante
        self.hidden_input = np.dot(X, self.weights_input_hidden)
        self.hidden_output = sigmoid(self.hidden_input)
        self.output_input = np.dot(self.hidden_output, self.weights_hidden_output)
        self.output = sigmoid(self.output_input)
        return self.output

# Algoritmo de Optimización por Enjambre de Partículas (PSO)
class ParticleSwarmOptimization:
    def __init__(self, num_particles, max_iter, w, c1, c2, mlp, X, y):
        self.num_particles = num_particles
        self.max_iter = max_iter
        self.w = w  # Factor de inercia
        self.c1 = c1  # Coeficiente cognitivo
        self.c2 = c2  # Coeficiente social
        self.mlp = mlp
        self.X = X
        self.y = y
    
    def initialize_particles(self):
        particles = []
        for _ in range(self.num_particles):
            # Inicialización aleatoria de los pesos
            particle = {
                'position': np.random.randn(self.mlp.input_size * self.mlp.hidden_size + self.mlp.hidden_size * self.mlp.output_size),
                'velocity': np.zeros(self.mlp.input_size * self.mlp.hidden_size + self.mlp.hidden_size * self.mlp.output_size),
                'best_position': None,
                'best_error': float('inf')
            }
            particles.append(particle)
        return particles
    
    def evaluate_particles(self, particles):
        for particle in particles:
            # Actualizamos los pesos de la red con la posición de la partícula
            position = particle['position']
            self.mlp.weights_input_hidden = position[:self.mlp.input_size * self.mlp.hidden_size].reshape(self.mlp.input_size, self.mlp.hidden_size)
            self.mlp.weights_hidden_output = position[self.mlp.input_size * self.mlp.hidden_size:].reshape(self.mlp.hidden_size, self.mlp.output_size)
            
            # Calculamos el error de la red
            predictions = self.mlp.forward(self.X)
            error = mean_squared_error(self.y, predictions)
            
            # Actualizamos la mejor posición personal si es necesario
            if error < particle['best_error']:
                particle['best_error'] = error
                particle['best_position'] = particle['position'].copy()
    
    def update_velocity_and_position(self, particles, gbest_position):
        for particle in particles:
            r1 = np.random.rand(len(particle['position']))
            r2 = np.random.rand(len(particle['position']))
            
            # Actualizamos la velocidad
            particle['velocity'] = (self.w * particle['velocity'] +
                                    self.c1 * r1 * (particle['best_position'] - particle['position']) +
                                    self.c2 * r2 * (gbest_position - particle['position']))
            
            # Actualizamos la posición
            particle['position'] += particle['velocity']
    
    def run(self):
        particles = self.initialize_particles()
        gbest_position = None
        gbest_error = float('inf')
        
        for iteration in range(self.max_iter):
            self.evaluate_particles(particles)
            
            # Encontramos la mejor partícula global
            for particle in particles:
                if particle['best_error'] < gbest_error:
                    gbest_error = particle['best_error']
                    gbest_position = particle['best_position']
            
            # Actualizamos las velocidades y posiciones
            self.update_velocity_and_position(particles, gbest_position)
            
            # Mostrar progreso
            if iteration % 100 == 0:
                print(f"Iteración {iteration}, Mejor error global: {gbest_error}")
        
        return gbest_position

# Entrenamiento
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # Puntos de entrada
y = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # Salidas deseadas (los cuadrantes)
mlp = MLP(input_size=2, hidden_size=2, output_size=2)

pso = ParticleSwarmOptimization(num_particles=30, max_iter=1000, w=0.729, c1=1.494, c2=1.494, mlp=mlp, X=X, y=y)
best_position = pso.run()

print("Mejor posición global encontrada por PSO:", best_position)
