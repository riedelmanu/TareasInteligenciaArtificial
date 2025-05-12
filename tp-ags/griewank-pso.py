import numpy as np
import pyswarms as ps

# Parámetros
DIM = 10
LOWER_BOUND = -600
UPPER_BOUND = 600

# Función Griewank para múltiples partículas
def griewank(x):
    sum_term = np.sum(x ** 2, axis=1) / 4000
    prod_term = np.prod(np.cos(x / np.sqrt(np.arange(1, DIM + 1))), axis=1)
    return 1 + sum_term - prod_term

# Límites
bounds = (np.ones(DIM) * LOWER_BOUND, np.ones(DIM) * UPPER_BOUND)

# Configuración del optimizador
options = {
    'c1': 1.494,  # coeficiente cognitivo
    'c2': 1.494,  # coeficiente social
    'w': 0.729    # inercia
}

# Inicializar PSO
optimizer = ps.single.GlobalBestPSO(
    n_particles=100,
    dimensions=DIM,
    options=options,
    bounds=bounds
)

# Ejecutar optimización
best_cost, best_pos = optimizer.optimize(griewank, iters=200)

# Mostrar resultados
print("\n🔍 Mejor solución encontrada con PSO:")
print(f"x = {best_pos}")
print(f"f(x) = {best_cost:.6f}")
