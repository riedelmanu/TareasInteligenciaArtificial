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

# Algoritmo Genético para ajustar los pesos de la red
class GeneticAlgorithm:
    def __init__(self, population_size, generations, mutation_rate, crossover_rate, mlp, X, y):
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.mlp = mlp
        self.X = X
        self.y = y
    
    def initialize_population(self):
        population = []
        for _ in range(self.population_size):
            # Inicializamos individuos con pesos aleatorios
            individual = {
                'weights_input_hidden': np.random.randn(self.mlp.input_size, self.mlp.hidden_size),
                'weights_hidden_output': np.random.randn(self.mlp.hidden_size, self.mlp.output_size)
            }
            population.append(individual)
        return population
    
    def evaluate_population(self, population):
        fitness_scores = []
        for individual in population:
            # Asignamos los pesos de cada individuo a la red
            self.mlp.weights_input_hidden = individual['weights_input_hidden']
            self.mlp.weights_hidden_output = individual['weights_hidden_output']
            predictions = self.mlp.forward(self.X)
            error = mean_squared_error(self.y, predictions)
            fitness_scores.append(1 / (error + 1e-6))  # Queremos minimizar el error, maximizar la aptitud
        return fitness_scores
    
    def select_parents(self, population, fitness_scores):
        parents = np.random.choice(population, size=2, p=np.array(fitness_scores)/sum(fitness_scores), replace=False)
        return parents
    
    def crossover(self, parents):
        if np.random.rand() < self.crossover_rate:
            crossover_point = np.random.randint(1, self.mlp.input_size * self.mlp.hidden_size)
            child1 = parents[0].copy()
            child2 = parents[1].copy()
            
            # Crossover de pesos (corte en el punto determinado)
            child1['weights_input_hidden'].flat[crossover_point:] = parents[1]['weights_input_hidden'].flat[crossover_point:]
            child2['weights_input_hidden'].flat[crossover_point:] = parents[0]['weights_input_hidden'].flat[crossover_point:]
            
            return child1, child2
        return parents
    
    def mutate(self, individual):
        if np.random.rand() < self.mutation_rate:
            mutation_point = np.random.randint(0, self.mlp.input_size * self.mlp.hidden_size)
            individual['weights_input_hidden'].flat[mutation_point] += np.random.randn() * 0.1
        return individual
    
    def run(self):
        population = self.initialize_population()
        best_fitness = 0
        best_individual = None
        
        for generation in range(self.generations):
            fitness_scores = self.evaluate_population(population)
            
            # Obtener el mejor individuo
            best_fitness_idx = np.argmax(fitness_scores)
            if fitness_scores[best_fitness_idx] > best_fitness:
                best_fitness = fitness_scores[best_fitness_idx]
                best_individual = population[best_fitness_idx]
            
            # Selección, cruce y mutación
            new_population = []
            for _ in range(self.population_size // 2):
                parents = self.select_parents(population, fitness_scores)
                children = self.crossover(parents)
                new_population.extend(children)
            
            # Aplicar mutación
            new_population = [self.mutate(ind) for ind in new_population]
            
            # Reemplazar la población anterior
            population = new_population
            
            # Mostrar progreso
            if generation % 100 == 0:
                print(f"Generación {generation}, Mejor aptitud: {best_fitness}")
        
        return best_individual

# Entrenamiento
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # Puntos de entrada
y = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # Salidas deseadas (los cuadrantes)
mlp = MLP(input_size=2, hidden_size=2, output_size=2)

ga = GeneticAlgorithm(population_size=50, generations=1000, mutation_rate=0.01, crossover_rate=0.7, mlp=mlp, X=X, y=y)
best_individual = ga.run()

print("Mejor individuo encontrado por AGS:", best_individual)
