import random

# Fórmula b: cada cláusula como lista de literales (positivos o negativos)
clauses = [
    [4, 2, 3],
    [5, 1, 2],
    [4, 1, -3],
    [3, 1, 2],
    [4, 1, -2],
    [-5, -1, 4]
]

NUM_VARS = 6
POP_SIZE = 30
GENERATIONS = 100
MUTATION_RATE = 0.05
TOURNAMENT_SIZE = 3

# Crear un individuo aleatorio
def create_individual():
    return [random.randint(0, 1) for _ in range(NUM_VARS)]

# Evaluar cuántas cláusulas son verdaderas
def fitness(individual):
    satisfied = 0
    for clause in clauses:
        clause_satisfied = False
        for literal in clause:
            var_index = abs(literal)
            var_value = individual[var_index]
            if literal > 0 and var_value == 1:
                clause_satisfied = True
                break
            elif literal < 0 and var_value == 0:
                clause_satisfied = True
                break
        if clause_satisfied:
            satisfied += 1
    return satisfied

# Selección por torneo
def tournament_selection(population):
    competitors = random.sample(population, TOURNAMENT_SIZE)
    return max(competitors, key=fitness)

# Cruce de un punto
def crossover(parent1, parent2):
    point = random.randint(1, NUM_VARS - 1)
    return parent1[:point] + parent2[point:]

# Mutación
def mutate(individual):
    return [(bit if random.random() > MUTATION_RATE else 1 - bit) for bit in individual]

# Algoritmo Genético Simple
def genetic_algorithm():
    population = [create_individual() for _ in range(POP_SIZE)]
    best_individual = max(population, key=fitness)

    for generation in range(GENERATIONS):
        new_population = []
        for _ in range(POP_SIZE):
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)

            if fitness(child) > fitness(best_individual):
                best_individual = child

        population = new_population

    return best_individual, fitness(best_individual)

# Ejecutar
solution, satisfied_clauses = genetic_algorithm()
print(f"Mejor solución: {solution}")
print(f"Cláusulas satisfechas: {satisfied_clauses} de {len(clauses)}")
