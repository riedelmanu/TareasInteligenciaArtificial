import numpy as np
import pyswarms as ps

# Dimensión y límites
DIM = 10
LOWER_BOUND = -500
UPPER_BOUND = 500

# Función Schwefel (misma que en el AG)
def schwefel(x):
    return 4189.82901 * DIM - np.sum(x * np.sin(np.sqrt(np.abs(x))), axis=1)

# Definir límites para pyswarms
bounds = (np.ones(DIM) * LOWER_BOUND, np.ones(DIM) * UPPER_BOUND)

# Configuración del optimizador
options = {
    'c1': 1.494,     # coeficiente cognitivo
    'c2': 1.494,     # coeficiente social
    'w': 0.729       # inercia
}

# Crear optimizador PSO
optimizer = ps.single.GlobalBestPSO(
    n_particles=100,      # número de partículas (equivale a tamaño de población)
    dimensions=DIM,
    options=options,
    bounds=bounds
)

# Ejecutar optimización
best_cost, best_pos = optimizer.optimize(schwefel, iters=200)

# Resultados
print("\n🔍 Mejor solución encontrada con PSO:")
print(f"x = {best_pos}")
print(f"f(x) = {best_cost:.4f}")
