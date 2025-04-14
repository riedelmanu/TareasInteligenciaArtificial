from simpleai.search import SearchProblem, astar, breadth_first, depth_first, uniform_cost
from simpleai.search.viewers import WebViewer
import time

OBJETIVO = "Bucharest"

class ProblemaRumania(SearchProblem):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ciudades = [
            "Arad", "Bucharest", "Craiova", "Drobeta", "Eforie", "Fagaras", "Giurgiu",
            "Hirsova", "Iasi", "Lugoj", "Mehadia", "Neamt", "Oradea", "Pitesti",
            "Rimnicu Vilcea", "Sibiu", "Timisoara", "Urziceni", "Vaslui", "Zerind"
        ]

        self.vecinos = {
            ("Arad", "Sibiu"): 140, ("Arad", "Timisoara"): 118, ("Arad", "Zerind"): 75,
            ("Bucharest", "Fagaras"): 211, ("Bucharest", "Giurgiu"): 90, ("Bucharest", "Pitesti"): 101, ("Bucharest", "Urziceni"): 85,
            ("Craiova", "Drobeta"): 120, ("Craiova", "Pitesti"): 138, ("Craiova", "Rimnicu Vilcea"): 146,
            ("Drobeta", "Craiova"): 120, ("Drobeta", "Mehadia"): 75,
            ("Eforie", "Hirsova"): 86,
            ("Fagaras", "Bucharest"): 211, ("Fagaras", "Sibiu"): 99,
            ("Giurgiu", "Bucharest"): 90,
            ("Hirsova", "Eforie"): 86, ("Hirsova", "Urziceni"): 98,
            ("Iasi", "Neamt"): 87, ("Iasi", "Vaslui"): 92,
            ("Lugoj", "Mehadia"): 70, ("Lugoj", "Timisoara"): 111,
            ("Mehadia", "Lugoj"): 70, ("Mehadia", "Drobeta"): 75,
            ("Neamt", "Iasi"): 87,
            ("Oradea", "Sibiu"): 151, ("Oradea", "Zerind"): 71,
            ("Pitesti", "Craiova"): 138, ("Pitesti", "Rimnicu Vilcea"): 97, ("Pitesti", "Bucharest"): 101,
            ("Rimnicu Vilcea", "Craiova"): 146, ("Rimnicu Vilcea", "Sibiu"): 80, ("Rimnicu Vilcea", "Pitesti"): 97,
            ("Sibiu", "Arad"): 140, ("Sibiu", "Fagaras"): 99, ("Sibiu", "Oradea"): 151, ("Sibiu", "Rimnicu Vilcea"): 80,
            ("Timisoara", "Arad"): 118, ("Timisoara", "Lugoj"): 70,
            ("Urziceni", "Bucharest"): 85, ("Urziceni", "Hirsova"): 98, ("Urziceni", "Vaslui"): 142,
            ("Vaslui", "Iasi"): 92, ("Vaslui", "Urziceni"): 142,
            ("Zerind", "Arad"): 75, ("Zerind", "Oradea"): 71
        }

        self.distancia_bucarest = {
            "Arad": 366, "Bucharest": 0, "Craiova": 160, "Drobeta": 242, "Eforie": 161,
            "Fagaras": 176, "Giurgiu": 77, "Hirsova": 151, "Iasi": 226, "Lugoj": 244,
            "Mehadia": 241, "Neamt": 234, "Oradea": 380, "Pitesti": 100, "Rimnicu Vilcea": 193,
            "Sibiu": 253, "Timisoara": 329, "Urziceni": 80, "Vaslui": 199, "Zerind": 374
        }

    def actions(self, estado):
        return [destino for (origen, destino) in self.vecinos if origen == estado]

    def result(self, estado, accion):
        return accion

    def is_goal(self, estado):
        return estado == OBJETIVO

    def cost(self, estado1, accion, estado2):
        return self.vecinos.get((estado1, estado2), self.vecinos.get((estado2, estado1)))

    def heuristic(self, estado):
        return self.distancia_bucarest[estado]

def probar(algoritmo, nombre):
    print(f"\nUsando algoritmo: {nombre}")
    problema = ProblemaRumania(initial_state="Arad")
    inicio = time.time()
    resultado = algoritmo(problema, graph_search=True)
    fin = time.time()
    print(f"Estado final: {resultado.state}")
    print(f"Ruta: {[x for x in resultado.path()]}")
    print(f"Tiempo: {fin - inicio:.6f} segundos")

probar(breadth_first, "Búsqueda por Anchura")
probar(depth_first, "Búsqueda por Profundidad")
probar(uniform_cost, "Costo Uniforme")
probar(astar, "A* con heurística (distancia a Bucarest)")
