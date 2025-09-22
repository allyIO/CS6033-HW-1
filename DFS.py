class DFS:
    def __init__(self, map, start, end):
        self.numCityVisits = 0
        self.maxQueueSize = 0
        self.startCity = start
        self.endCity = end
        self.map = map
        self.pathCost = 0

        self.searchResult = None
        self.solve()

    def solve(self):
        visited = set()
        stack = [(self.startCity, [self.startCity])]
        
        while stack:
            # Pop last element
            curr, path = stack.pop()

            # Check if visited
            if curr not in visited:
                visited.add(curr)

                self.numCityVisits += 1
                self.maxQueueSize = max(self.maxQueueSize, len(stack))

                # Check if we reached the end                
                if curr == self.endCity:
                    self.searchResult = path, 
                    self.pathCost = self.calculatePathCost(path)
                    return self.searchResult
                
                # Each neighbor in the map is a tuple
                for n, cost in self.map.get(curr, []):
                    if n not in visited:
                        stack.append((n, path + [n]))
        self.pathCost = None
        return None

    def calculatePathCost(self, path):
        totalCost = 0
        for i in range(len(path) - 1):
            currentCity = path[i]
            nextCity = path[i+1]
            # Find the cost to go from the current city to the next one
            for neighbor, cost in self.map.get(currentCity, []):
                if neighbor == nextCity:
                    totalCost += cost
                    break
        return totalCost