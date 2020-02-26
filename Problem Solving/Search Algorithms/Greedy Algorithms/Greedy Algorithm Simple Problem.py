from copy import deepcopy

map1 = {'A': ['B', 'C', 'H'],
         'B': ['A', 'D', 'E', 'F'],
         'C': ['A', 'B'],
         'D': ['A'],
         'E': ['D', "G"],
         'F': ['H', 'B'],
         'G': ['D', 'A'],
         'H': ['E']}

straightDistance = {
    'A': 3,
    'B': 55,
    'C': 6,
    'D': 5,
    'E': 19,
    'G': 10,
    'H': 15
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

answer = greedyAlgorithm(map1, 'A', 'F', straightDistance)
print(answer)