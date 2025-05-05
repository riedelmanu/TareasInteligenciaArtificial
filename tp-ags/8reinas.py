import random
import numpy as np
from typing import List, Tuple, Callable

def generar_individuo() -> List[int]:
    """Genera un individuo aleatorio (permutación de 0-7)"""
    return random.sample(range(8), 8)

def calcular_fitness(individuo: List[int]) -> int:
    """Calcula el fitness como el número de pares de reinas no atacantes"""
    ataques = 0
    for i in range(7):
        for j in range(i+1, 8):
            # Misma fila (imposible por nuestra representación)
            # Misma diagonal
            if abs(i - j) == abs(individuo[i] - individuo[j]):
                ataques += 1
    return 28 - ataques  # Máximo 28 pares no atacantes

def seleccionar_padres(poblacion: List[List[int]], fitness: List[int], num_padres: int) -> List[List[int]]:
    """Selecciona padres usando ruleta"""
    total_fitness = sum(fitness)
    probabilidades = [f/total_fitness for f in fitness]
    return random.choices(poblacion, weights=probabilidades, k=num_padres)

def crossover(padre1: List[int], padre2: List[int]) -> Tuple[List[int], List[int]]:
    """Crossover en un punto"""
    punto_corte = random.randint(1, 6)
    hijo1 = padre1[:punto_corte] + [g for g in padre2 if g not in padre1[:punto_corte]]
    hijo2 = padre2[:punto_corte] + [g for g in padre1 if g not in padre2[:punto_corte]]
    return hijo1, hijo2

def mutar(individuo: List[int], prob_mutacion: float) -> List[int]:
    """Mutación intercambiando dos genes"""
    if random.random() < prob_mutacion:
        i, j = random.sample(range(8), 2)
        individuo[i], individuo[j] = individuo[j], individuo[i]
    return individuo

def algoritmo_genetico(tam_poblacion: int = 100, prob_mutacion: float = 0.2, 
                      max_generaciones: int = 1000) -> List[int]:
    """Implementación del algoritmo genético para las 8 reinas"""
    
    # Inicializar población
    poblacion = [generar_individuo() for _ in range(tam_poblacion)]
    mejor_fitness = 0
    generacion = 0
    
    while generacion < max_generaciones and mejor_fitness < 28:
        # Evaluar fitness
        fitness = [calcular_fitness(ind) for ind in poblacion]
        mejor_fitness = max(fitness)
        
        # Seleccionar padres
        padres = seleccionar_padres(poblacion, fitness, tam_poblacion)
        
        # Crear nueva generación
        nueva_generacion = []
        for i in range(0, tam_poblacion, 2):
            hijo1, hijo2 = crossover(padres[i], padres[i+1])
            nueva_generacion.extend([mutar(hijo1, prob_mutacion), mutar(hijo2, prob_mutacion)])
        
        # Reemplazar población
        poblacion = nueva_generacion
        generacion += 1
        
        # Mostrar progreso
        if generacion % 50 == 0:
            print(f"Generación {generacion}, Mejor fitness: {mejor_fitness}")
    
    # Encontrar la mejor solución
    fitness = [calcular_fitness(ind) for ind in poblacion]
    mejor_idx = np.argmax(fitness)
    mejor_solucion = poblacion[mejor_idx]
    
    print(f"\nSolución encontrada en la generación {generacion}:")
    print(mejor_solucion)
    print(f"Fitness: {fitness[mejor_idx]}/28")
    
    return mejor_solucion

def imprimir_tablero(solucion: List[int]):
    """Imprime el tablero con las reinas"""
    for fila in range(8):
        linea = ""
        for col in range(8):
            if solucion[col] == fila:
                linea += "Q "
            else:
                linea += ". "
        print(linea)

# Ejecutar el algoritmo genético
solucion = algoritmo_genetico(tam_poblacion=100, prob_mutacion=0.3, max_generaciones=1000)
print("\nTablero solución:")
imprimir_tablero(solucion)
