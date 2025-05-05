import random

# funcion a maximizar
def fitness(x):
    return x**5 - x**3 - 2*x**2

# individuo binario de 6 bits
def create_individual():
    return ''.join(random.choice('01') for _ in range(6))

# decodificar de binario a entero
def decode(individual):
    return int(individual, 2)

# crear poblacion inicial
def create_population(size):
    return [create_individual() for _ in range(size)]

# seleccion por torneo
def tournament_selection(population, k=3):
    selected = random.sample(population, k)
    selected.sort(key=lambda ind: fitness(decode(ind)), reverse=True)
    return selected[0]

# cruce de un punto
def crossover(parent1, parent2):
    point = random.randint(1, 5)
    return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]

# mutacion con probabilidad
def mutate(individual, mutation_rate=0.01):
    return ''.join(
        bit if random.random() > mutation_rate else str(1 - int(bit))
        for bit in individual
    )

# AGS principal
def genetic_algorithm(generations=50, population_size=20):
    population = create_population(population_size)
    for gen in range(generations):
        new_population = []
        for _ in range(population_size // 2):
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1)
            child2 = mutate(child2)
            new_population += [child1, child2]
        population = new_population

    # mejor individuo
    best = max(population, key=lambda ind: fitness(decode(ind)))
    best_x = decode(best)
    return best_x, fitness(best_x)

# ejecutar
if __name__ == "__main__":
    mejor_x, mejor_fitness = genetic_algorithm()
    print(f"Máximo encontrado: x = {mejor_x}, f(x) = {mejor_fitness}")
