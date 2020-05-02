from copy import deepcopy

class StatisticsData(object):
    def __init__(self):
        self.totalGeser = [0, 0, 0, 0]
        self.totalJump = [0, 0, 0, 0]
        self.totalTime = [0, 0, 0, 0]
        self.averageTime = [0, 0, 0, 0]

    def countAndUpdateMove(self, giliran, move):
        # print(f"MOVE {move[2]}")
        if move[2] == 0:
            self.totalGeser[giliran] += 1
            # print(f"TOTAL GESER {self.totalGeser}")
        elif move[2] == 1:
            self.totalJump[giliran] += len(move[0])
            # print(f"TOTAL JUMP {self.totalJump}")

    def countAndUpdateTime(self, giliran, langkah, newDeltaTime):
        self.totalTime[giliran] += newDeltaTime
        self.averageTime[giliran] = ((self.averageTime[giliran] * (langkah-1)) + newDeltaTime) / langkah


class MoveContainer(object):
    def __init__(self):
        self.moves = []
        self.currentIndexMove = 1
        self.moveSet = []
        for component in range(12):
            self.moveSet.append(None)
        self.longestMove = [0, 0, 0, 0]

    def updateMoveData(self, move):
        self.moves.append(move)

    def isIndexInTheRange(self, index, array):
        if len(array) > index:
            return True
        else:
            return False

    def increaseCurrentMoveIndex(self):
        self.currentIndexMove += 1

    def decreaseCurrentMoveIndex(self):
        self.currentIndexMove -= 1

    # Update to return list of move
    def analyzeMoveSet(self, giliran):
        print(f'LEN MOVE {len(self.moves)}')
        print(f'GILIRAN {(giliran+3)%4}')
        if len(self.moves) != 0:
            if self.moves[-1][0] != None:
                self.moveSet[3*((giliran+3)%4)] = (str(self.moves[-1][1]) + '->' + str(self.moves[-1][0][-1]))
                self.moveSet[3*((giliran+3)%4)+1] = (len(self.moves[-1][0]))
                if self.longestMove[((giliran+3)%4)] < len(self.moves[-1][0]):
                    self.longestMove[((giliran+3)%4)] = len(self.moves[-1][0])
                    self.moveSet[3*((giliran+3)%4)+2] = len(self.moves[-1][0])
            else:
                self.moveSet[3*((giliran+3)%4)] = None
                self.moveSet[3*((giliran+3)%4)+1] = 0

    def getMove(self, index):
        # print('GET MOVE', self.moveSet[index])
        return self.moveSet[index]