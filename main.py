# HW 1 Search Testing
from BFS import *
from DFS import *
from BestFirst import *
from AStar import *
from enum import Enum
import random
import time

# Romania cities
class Cities(Enum):
    ARAD = 1
    BUCHAREST = 2
    CRAIOVA = 3
    DROBETA = 4
    EFORIE = 5
    FAGARAS = 6
    GIURGIU = 7
    HIRSOVA = 8
    IASI = 9
    LUGOJ = 10
    MEHADIA = 11
    NEAMT = 12
    ORADEA = 13
    PITESTI = 14
    RIMNICU_VILCEA = 15
    SIBIU = 16
    TIMISOARA = 17
    URZICENI = 18
    VASLUI = 19
    ZERIND = 20

SLD_TO_BUCHAREST = {
    "ARAD": 366,
    "BUCHAREST": 0,
    "CRAIOVA": 160,
    "DROBETA": 242,
    "EFORIE": 161,
    "FAGARAS": 176,
    "GIURGIU": 77,
    "HIRSOVA": 151,
    "IASI": 226,
    "LUGOJ": 244,
    "MEHADIA": 241,
    "NEAMT": 234,
    "ORADEA": 380,
    "PITESTI": 100,
    "RIMNICU_VILCEA": 193,
    "SIBIU": 253,
    "TIMISOARA": 329,
    "URZICENI": 80,
    "VASLUI": 199,
    "ZERIND": 374
}


# Romania map adjacency list
ROAD_ADJ_LIST = {
    Cities.ARAD: [(Cities.SIBIU, 140), (Cities.TIMISOARA, 118), (Cities.ZERIND, 75)],
    Cities.BUCHAREST: [(Cities.FAGARAS, 211), (Cities.GIURGIU, 90), (Cities.PITESTI, 101),(Cities.URZICENI, 85)],
    Cities.CRAIOVA: [(Cities.DROBETA, 120), (Cities.PITESTI, 138), (Cities.RIMNICU_VILCEA, 146)],
    Cities.DROBETA: [(Cities.CRAIOVA, 120), (Cities.MEHADIA, 75)],
    Cities.EFORIE: [(Cities.HIRSOVA, 86)],
    Cities.FAGARAS: [(Cities.BUCHAREST, 211), (Cities.SIBIU, 99)],
    Cities.GIURGIU: [(Cities.BUCHAREST, 90)],
    Cities.HIRSOVA: [(Cities.EFORIE, 86), (Cities.URZICENI, 98)],
    Cities.IASI: [(Cities.NEAMT, 87), (Cities.VASLUI, 92)],
    Cities.LUGOJ: [(Cities.MEHADIA, 70), (Cities.TIMISOARA, 111)],
    Cities.MEHADIA: [(Cities.DROBETA, 75), (Cities.LUGOJ, 70)],
    Cities.NEAMT: [(Cities.IASI, 87)],
    Cities.ORADEA: [(Cities.SIBIU, 151), (Cities.ZERIND, 71)],
    Cities.PITESTI: [(Cities.BUCHAREST, 101), (Cities.CRAIOVA, 138), (Cities.RIMNICU_VILCEA, 97)],
    Cities.RIMNICU_VILCEA: [(Cities.CRAIOVA, 146), (Cities.PITESTI, 97), (Cities.SIBIU, 80)],
    Cities.SIBIU: [(Cities.ARAD, 140), (Cities.FAGARAS, 99), (Cities.ORADEA, 151)],
    Cities.TIMISOARA: [(Cities.ARAD, 118), (Cities.LUGOJ, 111)],
    Cities.URZICENI: [(Cities.BUCHAREST, 85), (Cities.HIRSOVA, 98), (Cities.VASLUI, 142)],
    Cities.VASLUI: [(Cities.IASI, 92), (Cities.URZICENI, 142)],
    Cities.ZERIND: [(Cities.ARAD, 75), (Cities.ORADEA, 71)]
}

def checkCorrect(search, startCity, endCity):
    # Later add some test cases that the AI can check itself against... not gonna do every combo because I don't hate myself
    return True

def main():
    correctnessResults = {"BFS": [], "DFS": [], "Best First": [], "A* 1": [], "A* 2": []}
    cityVisitResults = {"BFS": [], "DFS": [], "Best First": [], "A* 1": [], "A* 2": []}
    timeResults = {"BFS": [], "DFS": [], "Best First": [], "A* 1": [], "A* 2": []}
    spaceResults = {"BFS": [], "DFS": [], "Best First": [], "A* 1": [], "A* 2": []}

    for x in range(5):
        # from Cities enum, randomly pick 2 and use as indices in roadMapAdjList for start and end cities
        startCity = random.choice(list(Cities))
        endCity = random.choice(list(Cities))
        
        # BFS
        start = time.perf_counter()
        bfs = BFS(ROAD_ADJ_LIST, startCity, endCity)
        end = time.perf_counter()
        correctnessResults["BFS"].append(checkCorrect(bfs, startCity, endCity))
        cityVisitResults["BFS"].append(bfs.numCityVisits)
        timeResults["BFS"].append(end - start)
        timeResults["BFS"].append(end - start)
        spaceResults["BFS"].append(bfs.maxQueueSize)

        # DFS
        start = time.perf_counter()
        dfs = DFS(ROAD_ADJ_LIST, startCity, endCity)
        end = time.perf_counter()
        correctnessResults["DFS"].append(checkCorrect(dfs, startCity, endCity))
        cityVisitResults["DFS"].append(dfs.numCityVisits)
        timeResults["DFS"].append(end - start)
        timeResults["DFS"].append(end - start)
        spaceResults["DFS"].append(dfs.maxQueueSize)

        # Best First
        start = time.perf_counter()
        bestFirst = BFS(ROAD_ADJ_LIST, startCity, endCity)
        end = time.perf_counter()
        correctnessResults["Best First"].append(checkCorrect(bestFirst, startCity, endCity))
        cityVisitResults["Best First"].append(bestFirst.numCityVisits)
        timeResults["Best First"].append(end - start)
        timeResults["Best First"].append(end - start)
        spaceResults["Best First"].append(bestFirst.maxQueueSize)

        # A*, heuristic 1
        start = time.perf_counter()
        aStar1 = AStarSearch(ROAD_ADJ_LIST, startCity, endCity, SLD_TO_BUCHAREST, heuristic_type=1)
        end = time.perf_counter()
        correctnessResults["A*"].append(checkCorrect(aStar, startCity, endCity))
        cityVisitResults["A*"].append(aStar.numCityVisits)
        timeResults["A*"].append(end - start)
        spaceResults["A*"].append(aStar.maxQueueSize)

        # A*, heuristic 2
        start = time.perf_counter()
        aStar2 = AStarSearch(ROAD_ADJ_LIST, startCity, endCity, SLD_TO_BUCHAREST, heuristic_type=2)
        end = time.perf_counter()
        correctnessResults["A* 2"].append(checkCorrect(aStar2, startCity, endCity))
        cityVisitResults["A* 2"].append(aStar2.numCityVisits)
        timeResults["A* 2"].append(end - start)
        spaceResults["A* 2"].append(aStar2.maxQueueSize)

    # Output
    # In the future, have also print out to csv or excel spreadsheet for easy tabling/graphing... maybe look into pandas
        correctnessResults["A*"].append(checkCorrect(aStar, startCity, endCity))
        cityVisitResults["A*"].append(aStar.numCityVisits)
        timeResults["A*"].append(end - start)
        spaceResults["A*"].append(aStar.maxQueueSize)

    print("Correctness results:")
    print(correctnessResults)

    print("Cities visited:")
    print(cityVisitResults)

    print("Time results:")
    print(timeResults)

    print("Space results:")
    print(spaceResults)

if __name__ == "__main__":
    main()