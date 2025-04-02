import time
import random

class AspiradoraReactiva:
    def __init__(self, tamano_mapa=(5, 5)):
        self.tamano_mapa = tamano_mapa
        self.mapa = [[random.choice(["limpio", "sucio", "sucio"]) for _ in range(tamano_mapa[1])] for _ in range(tamano_mapa[0])]
        self.posicion = (0, 0)
        self.estado = "buscando"
        self.direccion = "derecha"
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
        print(f"Estado: {self.estado}")
        print("-" * 20)

    def limpiar(self):
        x, y = self.posicion
        if self.mapa[x][y] == "sucio":
            self.mapa[x][y] = "limpio"
            self.estado = "limpiando"
            print(f"Limpieza en ({x}, {y})")
        else:
            self.estado = "buscando"
        self.visitados.add((x, y))

    def mover(self):
        x, y = self.posicion
        if len(self.visitados) == self.tamano_mapa[0] * self.tamano_mapa[1]:
            return  # Si todas las celdas fueron visitadas, no seguir moviéndose
        
        if self.direccion == "derecha":
            if y + 1 < self.tamano_mapa[1]:
                self.posicion = (x, y + 1)
            else:
                if x + 1 < self.tamano_mapa[0]:
                    self.posicion = (x + 1, y)
                    self.direccion = "izquierda"
        elif self.direccion == "izquierda":
            if y - 1 >= 0:
                self.posicion = (x, y - 1)
            else:
                if x + 1 < self.tamano_mapa[0]:
                    self.posicion = (x + 1, y)
                    self.direccion = "derecha"
        self.estado = "moviendo"

    def iniciar(self):
        while any("sucio" in fila for fila in self.mapa):
            self.mostrar_mapa()
            self.limpiar()
            self.mover()
            time.sleep(0.5)
        
        print("Limpieza terminada")

if __name__ == "__main__":
    robot = AspiradoraReactiva()
    robot.iniciar()
