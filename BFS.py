from collections import deque

class BFS:
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
        queue = deque([(self.startCity, [self.startCity])])

        while queue:
            # Dequeue first element
            curr, path = queue.popleft()

            # Check if visited
            if curr not in visited:
                visited.add(curr)

                self.numCityVisits += 1
                self.maxQueueSize = max(self.maxQueueSize, len(queue))

                # Check if we reached the end
                if curr == self.endCity:
                    self.searchResult = path
                    self.pathCost = self.calculatePathCost(path)
                    return self.searchResult
                
                # Each neighbor in the map is a tuple
                for n, cost in self.map.get(curr, []):
                    if n not in visited:
                        queue.append((n, path + [n]))
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