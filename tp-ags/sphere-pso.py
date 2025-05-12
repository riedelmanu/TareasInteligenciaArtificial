import numpy as np

# Parámetros PSO
POP_SIZE = 50
GENS = 100
DIM = 2
LOWER_BOUND = -5
UPPER_BOUND = 5

w = 0.729      # Inercia
c1 = 1.494     # Cognitivo
c2 = 1.494     # Social

# Función Sphere
def sphere(x):
    return np.sum(x**2)

# Inicializar partículas
positions = np.random.uniform(LOWER_BOUND, UPPER_BOUND, (POP_SIZE, DIM))
velocities = np.random.uniform(-1, 1, (POP_SIZE, DIM))
personal_best_pos = np.copy(positions)
personal_best_val = np.array([sphere(p) for p in positions])
global_best_pos = personal_best_pos[np.argmin(personal_best_val)]
global_best_val = np.min(personal_best_val)

# Bucle principal de PSO
for gen in range(GENS):
    for i in range(POP_SIZE):
        fitness = sphere(positions[i])
        if fitness < personal_best_val[i]:
            personal_best_val[i] = fitness
            personal_best_pos[i] = positions[i]

    best_particle_idx = np.argmin(personal_best_val)
    if personal_best_val[best_particle_idx] < global_best_val:
        global_best_val = personal_best_val[best_particle_idx]
        global_best_pos = personal_best_pos[best_particle_idx]

    for i in range(POP_SIZE):
        r1 = np.random.rand(DIM)
        r2 = np.random.rand(DIM)
        velocities[i] = (
            w * velocities[i] +
            c1 * r1 * (personal_best_pos[i] - positions[i]) +
            c2 * r2 * (global_best_pos - positions[i])
        )
        positions[i] += velocities[i]
        positions[i] = np.clip(positions[i], LOWER_BOUND, UPPER_BOUND)

    print(f"Gen {gen}: Mejor fitness = {global_best_val:.6f}")

print("\n🔍 Mejor solución encontrada por PSO (Sphere):")
print(f"x = {global_best_pos}")
print(f"f(x) = {global_best_val:.6f}")
