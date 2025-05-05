import numpy as np

# Parámetros del AG
POP_SIZE = 50
GENS = 100
DIM = 2
LOWER_BOUND = -5
UPPER_BOUND = 5
MUTATION_RATE = 0.1
TOURNAMENT_SIZE = 3

# Función objetivo: Sphere
def sphere(x):
    return np.sum(x ** 2)

# Crear individuo
def create_individual():
    return np.random.uniform(LOWER_BOUND, UPPER_BOUND, DIM)

# Crear población
def create_population():
    return [create_individual() for _ in range(POP_SIZE)]

# Evaluar fitness
def evaluate_population(population):
    return [sphere(ind) for ind in population]

# Torneo
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
    child = alpha * parent1 + (1 - alpha) * parent2
    return child

# Mutación
def mutate(individual):
    if np.random.rand() < MUTATION_RATE:
        i = np.random.randint(DIM)
        individual[i] += np.random.normal(0, 0.5)
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
