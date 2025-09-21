import heapq
import Heuristics as heuristics

class BestFirstSearch:
    def __init__(self, map, start, end):
        self.entryCount = 0
        self.map = map
        self.startCity = start 
        self.endCity = end
        self.pathCost = 0
        
        self.numCityVisits = 0
        self.maxQueueSize = 0
        
        self.fringe = []
        
        # Calculate the priority (heuristic cost) for the start city.
        hCost = heuristics.getHeuristic(self.startCity, self.endCity)
        
        # Push the startNode onto the fringe.
        startNode = (hCost, self.entryCount, self.startCity, [self.startCity])
        heapq.heappush(self.fringe, startNode)
        
        self.maxQueueSize = 1
        
        print(f"BestFirstSearch initialized. Fringe starts with: {self.fringe}")

        self.solve()
    
    def solve(self):
        # Using a set here to detect cycles
        visited = set()
        while self.fringe: # while there are still unexpanded nodes to explore
            priority, count, currentCity, path = heapq.heappop(self.fringe)

            if currentCity in visited:
                continue

            visited.add(currentCity)
            self.numCityVisits += 1

            if currentCity == self.endCity:
                # We found the solution!
                finalCost = self.calculatePathCost(path)
                print(f"Path found: {path} with cost: {finalCost}")
                self.searchResult = path
                self.pathCost = finalCost
                return path, finalCost

            for neighborEnum, costToNeighbor in self.map.get(currentCity, []):
                # for each neighbor of the current city, add to fringe.
                if neighborEnum not in visited:
                    self.entryCount += 1
                    newPath = path + [neighborEnum]
                
                    # Get the heuristic for this neighbor
                    hCost = heuristics.getHeuristic(neighborEnum, self.endCity)
                
                    # Create a node and push it onto the fringe
                    node = (hCost, self.entryCount, neighborEnum, newPath)
                    heapq.heappush(self.fringe, node)
                    if (len(self.fringe) > self.maxQueueSize):
                        self.maxQueueSize = len(self.fringe)

        print("No path found.")
        self.searchResult = None
        self.pathCost = None
        return None, None
    
    def calculatePathCost(self, path):
        totalCost = 0
        for i in range(len(path) - 1):
            currentCity = path[i]
            nextCity = path[i+1]
        
            # Find the cost to go from the current city to the next one
            for neighbor, cost in self.map[currentCity]:
                if neighbor == nextCity:
                    totalCost += cost
                    break 
        return totalCost