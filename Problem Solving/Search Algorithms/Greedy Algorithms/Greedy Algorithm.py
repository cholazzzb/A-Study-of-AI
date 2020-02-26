from copy import deepcopy

map1 = {'Arad': ['Sibiu', 'Timisoara', 'Zerind'],
        'Bucharest': ['Fagaras', 'Urziceni', 'Giurgiu'],
        'Craiova': ['Pitesti', 'Rimnicu Vilcea', 'Drobeta'],
        'Drobeta': ['Craiova', 'Mehadia'],
        'Eforie': ['Hirsova'],
        'Fagaras': ['Sibiu', 'Bucharest'],
        'Giurgiu':  ['Bucharest'],
        'Hirsova': ['Eforie', 'Urziceni'],
        'Iasi': ['Neamt', 'Vaslui'],
        'Lugoj': ['Timisoara', 'Mehadia'],
        'Mehadia': ['Drobeta',  'Lugoj'],
        'Neamt': ['Iasi'],
        'Oradea': ['Zerind', 'Sibiu'],
        'Pitesti': ['Rimnicu Vilcea', 'Bucharest', 'Craiova'],
        'Rimnicu Vilcea': ['Sibiu', 'Pitesti', 'Craiova'],
        'Sibiu': ['Fagaras', 'Rimnicu Vilcea', 'Oradea', 'Arad'],
        'Timisoara': ['Arad', 'Lugoj'],
        'Urziceni': ['Hirsova', 'Vaslui', 'Bucharest'],
        'Vaslui': ['Iasi', 'Urziceni'],
        'Zerind': ['Arad', 'Oradea']
        }

straightDistance = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Drobeta': 242,
    'Eforie': 161,
    'Fagaras': 176,
    'Giurgiu':  77,
    'Hirsova': 151,
    'Iasi': 226,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 100,
    'Rimnicu Vilcea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374
}


class Paths(object):
    'this is used for remembering the paths'

    def __init__(self, start, heuristic):
        self.straightDistance = heuristic
        self.paths = [[start]]

    def getBestPath(self):
        shortest = self.straightDistance[self.paths[0][-1]]
        bestPathIndex = 0
        for i in range(len(self.paths)):
            if self.straightDistance[self.paths[i][-1]] <= shortest:
                shortest = self.straightDistance[self.paths[i][-1]]
                bestPathIndex = i
        print('GetBestPath - the best path: ', self.paths[bestPathIndex])
        return self.paths.pop(bestPathIndex)

    def updatePaths(self, newPath):
        self.paths.append(newPath)
        print('UpdatePath - self.paths: ', self.paths)


def greedyAlgorithm(map, startPoint, destination, heuristicDistance):
    if straightDistance == destination:
        returnVal = 'Your startpoint is the same with the destinantion!'
        return returnVal

    explored = []
    smartPath = Paths(startPoint, heuristicDistance)
    print('Paths', smartPath.paths)

    while len(explored) != len(heuristicDistance)+1:
        path = smartPath.getBestPath()
        explored.append(path[-1])
        neighbours = map[path[-1]]
        for neighbour in neighbours:
            if neighbour not in explored:
                newPath = deepcopy(path)
                newPath.append(neighbour)
                if neighbour == destination:
                    print('The path is : ')
                    return newPath
                smartPath.updatePaths(newPath)

    returnVal = 'No possible path founded'
    return returnVal

answer = greedyAlgorithm(map1, 'Arad', 'Bucharest', straightDistance)
print(answer)
