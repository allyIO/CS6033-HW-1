class BestFirstSearch:
    def __init__(self, map, start, end):
        self.numCityVisits = 0
        self.maxQueueSize = 0
        self.startCity = 0
        self.endCity = 0

        print("Searching best first...")
        self.searchResult = None