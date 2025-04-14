from simpleai.search import SearchProblem, astar
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
    def __init__(self, estado_inicial, tipo_heuristica):
        self.tipo_heuristica = tipo_heuristica
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

    def heuristic(self, estado):
        if self.tipo_heuristica == 'fichas_fuera_de_lugar':
            return sum(
                1 for f in range(3) for c in range(3)
                if estado[f][c] != 0 and estado[f][c] != OBJETIVO[f][c]
            )

        elif self.tipo_heuristica == 'manhattan':
            total = 0
            for f in range(3):
                for c in range(3):
                    valor = estado[f][c]
                    if valor != 0:
                        fila_objetivo = (valor - 1) // 3
                        col_objetivo = (valor - 1) % 3
                        total += abs(fila_objetivo - f) + abs(col_objetivo - c)
            return total

for heuristica in ['fichas_fuera_de_lugar', 'manhattan']:
    print(f"\nUsando heurística: {heuristica}")
    problema = ProblemaPuzzle(estado_inicial, tipo_heuristica=heuristica)

    inicio = time.time()
    resultado = astar(problema)
    fin = time.time()

    print("Cantidad de pasos:", len(resultado.path()) - 1)
    print("Tiempo total: {:.4f} segundos".format(fin - inicio))
    print("Secuencia de movimientos:")
    for accion, estado in resultado.path():
        print("Movimiento:", accion)
        for fila in estado:
            print(fila)
        print()
