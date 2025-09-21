# Straight-Line Distance from various cities to Bucharest (from textbook)
sldToBucharest = {
    'ARAD': 366, 'BUCHAREST': 0, 'CRAIOVA': 160, 'DROBETA': 242,
    'EFORIE': 161, 'FAGARAS': 176, 'GIURGIU': 77, 'HIRSOVA': 151,
    'IASI': 226, 'LUGOJ': 244, 'MEHADIA': 241, 'NEAMT': 234,
    'ORADEA': 380, 'PITESTI': 100, 'RIMNICU_VILCEA': 193, 'SIBIU': 253,
    'TIMISOARA': 329, 'URZICENI': 80, 'VASLUI': 199, 'ZERIND': 374
}

def getHeuristic(currentCityEnum, goalCityEnum, method='difference'):
    
    # Get the string names from the enum objects
    currentCityName = currentCityEnum.name
    goalCityName = goalCityEnum.name

    # Case 1: The goal is Bucharest, so we have exact SLD values.
    if goalCityName == 'BUCHAREST':
        return sldToBucharest.get(currentCityName, float('inf'))

    # Case 2: The goal is not Bucharest, so estimate with triangle inequality.
    else:
        # Get the known SLDs from our two cities to the reference point (Bucharest)
        sldCurrentToBucharest = sldToBucharest.get(currentCityName, float('inf'))
        sldGoalToBucharest = sldToBucharest.get(goalCityName, float('inf'))

        if method == 'difference':
            return abs(sldCurrentToBucharest - sldGoalToBucharest)
        
        elif method == 'sum':
            return sldCurrentToBucharest + sldGoalToBucharest
        
        else:
            return 0