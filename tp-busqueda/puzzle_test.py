from simpleai.search import SearchProblem, astar

GOAL = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 0)
)

# Estado inicial fácil, a un solo movimiento del objetivo
INITIAL = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 0, 8)
)

class PuzzleProblem(SearchProblem):
    def __init__(self, initial_state, heuristic_type):
        self.heuristic_type = heuristic_type
        super().__init__(initial_state)

    def actions(self, state):
        row, col = next((r, c) for r in range(3) for c in range(3) if state[r][c] == 0)
        moves = []
        if row > 0: moves.append('arriba')
        if row < 2: moves.append('abajo')
        if col > 0: moves.append('izquierda')
        if col < 2: moves.append('derecha')
        return moves

    def result(self, state, action):
        row, col = next((r, c) for r in range(3) for c in range(3) if state[r][c] == 0)
        new_row, new_col = row, col
        if action == 'arriba': new_row -= 1
        if action == 'abajo': new_row += 1
        if action == 'izquierda': new_col -= 1
        if action == 'derecha': new_col += 1
        state = [list(r) for r in state]
        state[row][col], state[new_row][new_col] = state[new_row][new_col], state[row][col]
        return tuple(tuple(r) for r in state)

    def is_goal(self, state):
        return state == GOAL

    def cost(self, state1, action, state2):
        return 1

    def heuristic(self, state):
        print("Evaluando estado:")
        for row in state:
            print(row)
        print()

        if self.heuristic_type == 'misplaced':
            return sum(1 for r in range(3) for c in range(3)
                       if state[r][c] != 0 and state[r][c] != GOAL[r][c])
        elif self.heuristic_type == 'manhattan':
            total = 0
            for r in range(3):
                for c in range(3):
                    value = state[r][c]
                    if value != 0:
                        goal_r = (value - 1) // 3
                        goal_c = (value - 1) % 3
                        total += abs(goal_r - r) + abs(goal_c - c)
            return total


print("Con heurística: fichas mal colocadas")
problem1 = PuzzleProblem(INITIAL, heuristic_type='misplaced')
result1 = astar(problem1)
print("Solución encontrada en", len(result1.path()) - 1, "pasos\n")

print("Con heurística: distancia Manhattan")
problem2 = PuzzleProblem(INITIAL, heuristic_type='manhattan')
result2 = astar(problem2)
print("Solución encontrada en", len(result2.path()) - 1, "pasos")
