# AStar.py
import heapq
import itertools
from typing import Any, Dict, List, Tuple

class AStarSearch:
    """
    A* search implementation for the Romanian road map.

    Parameters:
        graph: adjacency list mapping Enum -> list of (neighbor_enum, cost)
        start: Enum member (start city)
        goal: Enum member (goal city)
        sld_bucharest: dict mapping city name string -> straight-line distance to Bucharest
        heuristic_type: 1 or 2, selects triangle inequality heuristic
    Attributes:
        searchResult: list of cities in path (empty if not found)
        numCityVisits: number of nodes expanded
        maxQueueSize: max frontier size
    """
    
    def __init__(self, graph: Dict[Any, List[Tuple[Any, int]]], start: Any, goal: Any, sld_bucharest: Dict[str,int], heuristic_type: int = 1):
        self.graph = graph
        self.start = start
        self.goal = goal
        self.sld_bucharest = sld_bucharest
        self.heuristic_type = heuristic_type

        self.numCityVisits = 0
        self.maxQueueSize = 0
        self.searchResult: List[Any] = []

        self.searchResult = self.a_star_search()

    # Heuristic 
    def heuristic(self, city: Any) -> float:
        city_name = city.name
        goal_name = self.goal.name

        if self.heuristic_type == 1:
            if goal_name == "BUCHAREST":
                return self.sld_bucharest[city_name]
            else:
                return abs(self.sld_bucharest[city_name] - self.sld_bucharest[goal_name])
        else:  # heuristic 2
            if goal_name == "BUCHAREST":
                return self.sld_bucharest[city_name]
            else:
                return self.sld_bucharest[city_name] + self.sld_bucharest[goal_name]

    #  A* search 
    def a_star_search(self) -> List[Any]:
        frontier = []
        counter = itertools.count()  
        start_g = 0
        start_h = self.heuristic(self.start)
        start_f = start_g + start_h

        heapq.heappush(frontier, (start_f, next(counter), start_g, self.start, [self.start]))
        visited = set()

        while frontier:
            self.maxQueueSize = max(self.maxQueueSize, len(frontier))
            f, _, g, current, path = heapq.heappop(frontier)

            if current in visited:
                continue

            visited.add(current)
            self.numCityVisits += 1

            if current == self.goal:
                return path

            for neighbor, cost in self.graph.get(current, []):
                if neighbor in visited:
                    continue
                g_new = g + cost
                f_new = g_new + self.heuristic(neighbor)
                heapq.heappush(frontier, (f_new, next(counter), g_new, neighbor, path + [neighbor]))

        return []  # no path found