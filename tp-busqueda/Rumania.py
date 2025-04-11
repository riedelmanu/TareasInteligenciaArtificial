from simpleai.search import SearchProblem, greedy
from simpleai.search.viewers import WebViewer


GOAL = "Bucharest"


class RomaniaProblem(SearchProblem):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cities = ["Arad", "Bucharest", "Craiova", "Drobeta", "Eforie", "Fagaras", "Giurgiu",
                       "Hirsova", "Iasi", "Lugoj", "Mehadia", "Neamt", "Oradea", "Pitesti", "Rimnicu Vilcea",
                       "Sibiu", "Timisoara", "Urziceni", "Vaslui", "Zerind"]
        self.neighbours = {("Arad", "Sibiu"): 140, ("Arad", "Timisoara"): 118, ("Arad", "Zerind"): 75,
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
                           ("Zerind", "Arad"): 75, ("Zerind", "Oradea"): 71}
        self.distanceToBucharest = {"Arad": 366, "Bucharest": 0, "Craiova": 160, "Drobeta": 242, "Eforie": 161,
                                    "Fagaras": 176, "Giurgiu": 77, "Hirsova": 151, "Iasi": 226, "Lugoj": 244,
                                    "Mehadia": 241, "Neamt": 234, "Oradea": 380, "Pitesti": 100, "Rimnicu Vilcea": 193,
                                    "Sibiu": 253, "Timisoara": 329, "Urziceni": 80, "Vaslui": 199, "Zerind": 374}

    def actions(self, state):
        act = []
        for city in self.cities:
            if (state, city) in self.neighbours:
                act.append("Ir a " + city)
        return act

    def result(self, state, action):
        return action.replace("Ir a ", "")

    def is_goal(self, state):
        return state == GOAL

    def cost(self, state, action, state2):
        return self.neighbours[state, state2]

    def heuristic(self, state):
        # how far are we from the goal?
        return self.distanceToBucharest[state]


problem = RomaniaProblem(initial_state='Arad')
result = greedy(problem, graph_search=True, viewer=WebViewer())

print(result.state)
print(result.path())