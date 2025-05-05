import numpy as np

# Parámetros del AG
POP_SIZE = 100
GENS = 200
DIM = 10
LOWER_BOUND = -600
UPPER_BOUND = 600
MUTATION_RATE = 0.1
TOURNAMENT_SIZE = 3

# Función Griewank
def griewank(x):
    sum_term = np.sum(x ** 2) / 4000
    prod_term = np.prod(np.cos(x / np.sqrt(np.arange(1, DIM + 1))))
    return 1 + sum_term - prod_term

# Crear individuo
def create_individual():
    return np.random.uniform(LOWER_BOUND, UPPER_BOUND, DIM)

# Crear población
def create_population():
    return [create_individual() for _ in range(POP_SIZE)]

# Evaluar fitness
def evaluate_population(population):
    return [griewank(ind) for ind in population]

# Selección por torneo
def tournament_selection(population, fitness):
    best = None
    for _ in range(TOURNAMENT_SIZE):
        i = np.random.randint(len(population))
        if (best is None) or (fitness[i] < fitness[best]):
            best = i
    return population[best]

# Cruce aritmético
def crossover(parent1, parent2):
    alpha = np.random.rand()
    return alpha * parent1 + (1 - alpha) * parent2

# Mutación
def mutate(individual):
    if np.random.rand() < MUTATION_RATE:
        i = np.random.randint(DIM)
        individual[i] += np.random.normal(0, 20)
        individual[i] = np.clip(individual[i], LOWER_BOUND, UPPER_BOUND)
    return individual

# Algoritmo Genético principal
def genetic_algorithm():
    population = create_population()
    best_solution = None
    best_fitness = float("inf")

    for generation in range(GENS):
        fitness = evaluate_population(population)
        new_population = []

        for _ in range(POP_SIZE):
            parent1 = tournament_selection(population, fitness)
            parent2 = tournament_selection(population, fitness)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)

        population = new_population

        # Guardar el mejor
        for ind, fit in zip(population, evaluate_population(population)):
            if fit < best_fitness:
                best_fitness = fit
                best_solution = ind

        print(f"Gen {generation}: Mejor fitness = {best_fitness:.6f}")

    print("\n🔍 Mejor solución encontrada:")
    print(f"x = {best_solution}")
    print(f"f(x) = {best_fitness:.6f}")

genetic_algorithm()
