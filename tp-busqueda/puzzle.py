from simpleai.search import SearchProblem, breadth_first
import time

OBJETIVO = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 0)  # El 0 representa el espacio vacío
)

estado_inicial = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 0, 8)
)

class ProblemaPuzzle(SearchProblem):
    def __init__(self, estado_inicial):
        super().__init__(estado_inicial)

    def actions(self, estado):
        fila, col = next((f, c) for f in range(3) for c in range(3) if estado[f][c] == 0)
        movimientos = []
        if fila > 0:
            movimientos.append('arriba')
        if fila < 2:
            movimientos.append('abajo')
        if col > 0:
            movimientos.append('izquierda')
        if col < 2:
            movimientos.append('derecha')
        return movimientos

    def result(self, estado, accion):
        fila, col = next((f, c) for f in range(3) for c in range(3) if estado[f][c] == 0)
        nueva_fila, nueva_col = fila, col

        if accion == 'arriba':
            nueva_fila -= 1
        elif accion == 'abajo':
            nueva_fila += 1
        elif accion == 'izquierda':
            nueva_col -= 1
        elif accion == 'derecha':
            nueva_col += 1

        estado = [list(fila) for fila in estado]
        estado[fila][col], estado[nueva_fila][nueva_col] = estado[nueva_fila][nueva_col], estado[fila][col]
        return tuple(tuple(fila) for fila in estado)

    def is_goal(self, estado):
        return estado == OBJETIVO

    def cost(self, estado1, accion, estado2):
        return 1  

def ejecutar_busqueda(algoritmo, problema):
    print(f"\nEjecutando {algoritmo.__name__}")
    inicio = time.time()
    resultado = algoritmo(problema)
    fin = time.time()
    print(f"Camino encontrado: {[accion for accion, _ in resultado.path()[1:]]}")
    print(f"Cantidad de pasos: {len(resultado.path()) - 1}")
    print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")

# diferentes estados iniciales
estados_iniciales = [
    (
        (1, 2, 3),
        (4, 5, 6),
        (7, 0, 8)
    ),
    (
        (1, 2, 3),
        (4, 0, 5),
        (7, 8, 6)
    ),
    (
        (2, 0, 3),
        (1, 4, 6),
        (7, 5, 8)
    )
]

for estado in estados_iniciales:
    print(f"\nEstado inicial:")
    for fila in estado:
        print(fila)

    problema = ProblemaPuzzle(estado)
    ejecutar_busqueda(breadth_first, problema)
