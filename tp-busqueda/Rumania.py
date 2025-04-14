from simpleai.search import SearchProblem, greedy, astar
import time

DESTINO = "Bucharest"

class ProblemaRumania(SearchProblem):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.conexiones = {
            ("Arad", "Zerind"): 75, ("Zerind", "Arad"): 75,
            ("Arad", "Sibiu"): 140, ("Sibiu", "Arad"): 140,
            ("Arad", "Timisoara"): 118, ("Timisoara", "Arad"): 118,
            ("Zerind", "Oradea"): 71, ("Oradea", "Zerind"): 71,
            ("Oradea", "Sibiu"): 151, ("Sibiu", "Oradea"): 151,
            ("Sibiu", "Fagaras"): 99, ("Fagaras", "Sibiu"): 99,
            ("Sibiu", "Rimnicu Vilcea"): 80, ("Rimnicu Vilcea", "Sibiu"): 80,
            ("Fagaras", "Bucharest"): 211, ("Bucharest", "Fagaras"): 211,
            ("Rimnicu Vilcea", "Pitesti"): 97, ("Pitesti", "Rimnicu Vilcea"): 97,
            ("Rimnicu Vilcea", "Craiova"): 146, ("Craiova", "Rimnicu Vilcea"): 146,
            ("Pitesti", "Bucharest"): 101, ("Bucharest", "Pitesti"): 101,
            ("Craiova", "Pitesti"): 138, ("Pitesti", "Craiova"): 138,
            ("Craiova", "Drobeta"): 120, ("Drobeta", "Craiova"): 120,
            ("Drobeta", "Mehadia"): 75, ("Mehadia", "Drobeta"): 75,
            ("Mehadia", "Lugoj"): 70, ("Lugoj", "Mehadia"): 70,
            ("Lugoj", "Timisoara"): 111, ("Timisoara", "Lugoj"): 111,
            ("Bucharest", "Giurgiu"): 90, ("Giurgiu", "Bucharest"): 90,
            ("Bucharest", "Urziceni"): 85, ("Urziceni", "Bucharest"): 85,
            ("Urziceni", "Hirsova"): 98, ("Hirsova", "Urziceni"): 98,
            ("Hirsova", "Eforie"): 86, ("Eforie", "Hirsova"): 86,
            ("Urziceni", "Vaslui"): 142, ("Vaslui", "Urziceni"): 142,
            ("Vaslui", "Iasi"): 92, ("Iasi", "Vaslui"): 92,
            ("Iasi", "Neamt"): 87, ("Neamt", "Iasi"): 87
        }

        # Distancia en línea recta a Bucarest
        self.heuristicas = {
            "Arad": 366, "Bucharest": 0, "Craiova": 160, "Drobeta": 242,
            "Eforie": 161, "Fagaras": 176, "Giurgiu": 77, "Hirsova": 151,
            "Iasi": 226, "Lugoj": 244, "Mehadia": 241, "Neamt": 234,
            "Oradea": 380, "Pitesti": 100, "Rimnicu Vilcea": 193,
            "Sibiu": 253, "Timisoara": 329, "Urziceni": 80,
            "Vaslui": 199, "Zerind": 374
        }

    def actions(self, estado):
        return [ciudad2 for (ciudad1, ciudad2) in self.conexiones if ciudad1 == estado]

    def result(self, estado, accion):
        return accion

    def is_goal(self, estado):
        return estado == DESTINO

    def cost(self, estado1, accion, estado2):
        return self.conexiones.get((estado1, estado2), 9999)

    def heuristic(self, estado):
        return self.heuristicas.get(estado, 9999)

def ejecutar_busqueda(nombre, algoritmo, problema):
    print(f"\nEjecutando {nombre}")
    inicio = time.time()
    resultado = algoritmo(problema)
    fin = time.time()
    print(f"Camino encontrado: {[accion for accion, _ in resultado.path()[1:]]}")
    print(f"Cantidad de pasos: {len(resultado.path()) - 1}")
    print(f"Tiempo de ejecución: {fin - inicio:.8f} segundos")

problema = ProblemaRumania(initial_state='Arad')

ejecutar_busqueda("Búsqueda Voraz", greedy, problema)
ejecutar_busqueda("Búsqueda A*", astar, problema)
