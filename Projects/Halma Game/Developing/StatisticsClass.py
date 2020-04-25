class StatisticsData(object):
    def __init__(self):
        self.totalGeser = [0, 0, 0, 0]
        self.totalJump = [0, 0, 0, 0]
        self.totalTime = [0, 0, 0, 0]
        self.averageTime = [0, 0, 0, 0]

    def countAndUpdateMove(self, giliran, move):
        print(f"MOVE {move[2]}")
        if move[2] == 0:
            self.totalGeser[giliran] += 1
            print(f"TOTAL GESER {self.totalGeser}")
        elif move[2] == 1:
            self.totalJump[giliran] += len(move[0])
            print(f"TOTAL JUMP {self.totalJump}")

    def countAndUpdateTime(self, giliran, langkah, newDeltaTime):
        self.totalTime[giliran] += newDeltaTime
        self.averageTime[giliran] = ((self.averageTime[giliran] * (langkah-1)) + newDeltaTime) / langkah
            