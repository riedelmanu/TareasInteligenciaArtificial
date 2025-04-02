import time
import random

class AspiradoraRobot:
    def __init__(self, tamano_mapa=(5, 5)):
        self.tamano_mapa = tamano_mapa
        self.mapa = [[random.choice(["limpio", "sucio", "sucio"]) for _ in range(tamano_mapa[1])] for _ in range(tamano_mapa[0])]
        self.posicion = (0, 0)
        self.visitados = set()

    def mostrar_mapa(self):
        for i in range(self.tamano_mapa[0]):
            for j in range(self.tamano_mapa[1]):
                if (i, j) == self.posicion:
                    print("A", end=" ")
                elif self.mapa[i][j] == "sucio":
                    print("X", end=" ")
                else:
                    print("O", end=" ")
            print()
        print("-" * 20)

    def limpiar(self):
        x, y = self.posicion
        self.visitados.add((x, y))
        if self.mapa[x][y] == "sucio":
            self.mapa[x][y] = "limpio"
            print(f"Limpieza en ({x}, {y})")
        else:
            print(f"({x}, {y}) ya está limpio")

    def mover(self):
        x, y = self.posicion
        movimientos_posibles = []
        prioridades = [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]  # Abajo, Adelante, Arriba, Atrás
        
        for movimiento in prioridades:
            if 0 <= movimiento[0] < self.tamano_mapa[0] and 0 <= movimiento[1] < self.tamano_mapa[1] and movimiento not in self.visitados:
                movimientos_posibles.append(movimiento)
        
        if movimientos_posibles:
            self.posicion = movimientos_posibles[0]  # Prioriza la primera opción disponible
        else:
            self.posicion = random.choice(prioridades)  # Si ya visitó todo, moverse aleatoriamente

    def iniciar(self):
        while any("sucio" in fila for fila in self.mapa):
            self.mostrar_mapa()
            self.limpiar()
            self.mover()
            time.sleep(0.5)
        
        print("Limpieza terminada")

if __name__ == "__main__":
    robot = AspiradoraRobot()
    robot.iniciar()
