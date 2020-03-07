'''
WARNING !!!
This code will error if you change the startBoard value
'''

from copy import deepcopy
from queue import PriorityQueue
from numpy.random import randint #randint(a,b,c), a is smallest value, b is biggest values, c is how much the random number is generated in list/array 

## -- Starting Board-- ##
# startBoard[0] = player 1
# startBoard[1] = player 2
# startBoard[n][6] = Points player n = Storehouse
startBoard = [
    [7,7,7,7,7,7,7,0],
    [7,7,7,7,7,7,7,0]
]

class Congklak(object):
    'Congklak game class'

    '''
    Variable list definition:
    1. self.board = The most updated board
    2. self.container = temporary container to save the marble from house when moving 
    3. player = the player house to move() (1/2)
    4. decision = the house to move() (1-7)
    '''

    __virtualBoard = [
    [7,7,7,7,7,7,7,0],
    [7,7,7,7,7,7,7,0]
] # For virtualizing new board 2x8 array
    __max1 = [] # Player 1 7x3 7 = every house, 3 = [house index(1-7), end Board, delta]
    __min1 = [] # Player 2
    __maxMinRAM = [] # Player 1 


    def __init__(self, board):
        self.board = board
        self.container = []
        self.turn = 1 # Player 1 or 2 giliran
        self.player = 1 # Player 1 or 2 daerah lubang
        self.lastDecision = 0 # between 1-8
        self.gameNotation = []

    def getVirtualBoard(self):
        return self.__virtualBoard
    
    def getMax1(self):
        return self.__max1

    def getMin1(self):
        return self.__min1
    
    def getBoard(self):
        return self.board

    def getTurn(self):
        return self.turn
    
    def getLastDecision(self):
        return self.lastDecision

    def setTurn(self, turn):
        self.turn = turn
    
    # player : 1-2, decision : 1-7
    def move(self, player, decision):
        newData = [decision]

        self.gameNotation.append(["Player " + str(player), decision])

        if player > 2 or decision > 7:
            print("the player or decision is not valid!")
            return 0
        
        # print('')
        # print('Initial Board', self.__virtualBoard)
        # print('Decision: Region =', player, 'House =', decision)

        # get the marbles
        self.container = self.__virtualBoard[player-1][decision-1]
        self.__virtualBoard[player-1][decision-1] = 0

        # move the marbles
        while self.container > 0:
            self.container -= 1
            
            # change to the next house
            decision += 1
            # print('House Index to put the marble', decision)

            # Skip the opponent house
            if decision == 8 and self.turn != player:
                decision += 1

            # Change the player house
            if decision > 8:
                player += 1
                if player > 2:
                    player -= 2
                decision -= 8

            # put marble in the next house
            self.__virtualBoard[player-1][decision-1] += 1          

        # Set the last player house
        self.player = player

        # Set the last decision 
        self.lastDecision = decision

        # print("New Board", self.__virtualBoard)
        # print("Last Index: Region =", self.player, "House = ", self.lastDecision)

        # print("total marble in the last house", self.__virtualBoard[self.player-1][self.lastDecision-1])

        # End condition
        # end in the warehouse
        if self.lastDecision == 8:
            # print("END IN WAREHOUSE") 
            newData.append(self.__virtualBoard)         
            return newData
            # if self.turn == 1:
            #     player1Move()
            # else:
            #     player2Move()

        # Move again at the last house
        if self.__virtualBoard[self.player-1][self.lastDecision-1]-1 != 0:
            # print("MOVE AGAIN")
            self.move(self.player, self.lastDecision)

        # empty in own house
        if self.turn == self.player:
            # print("END IN OWN HOUSE")         
            # print('End Board', self.__virtualBoard)
            # print("")
            newData.append(self.__virtualBoard)
            return newData

        # empty in enemy house
        else:
            # print('END IN ENEMY HOUSE')
            # print('End Board', self.__virtualBoard)
            # print("")
            newData.append(self.__virtualBoard)
            return newData

    def checkFinish(self):
        if self.__virtualBoard[0][7]+self.__virtualBoard[1][7] == 98:
            print("The game is finished")
            return 1
        else: 
            return 0

    def updateMax1(self):
        print('----- UPDATE Max1 -----')
        self.turn = 1
        for i in range (1,8):
            # Deep copy the real board to virtualBoard
            self.__virtualBoard = deepcopy(self.board)

            # get Virtual Board from moving a marble house
            newMax = self.move(1, i)
            newMax.append(self.__virtualBoard[1][7] - self.board[1][7])
            self.__max1.append(newMax)
            # print(newMax1)
        for i in range (0, 7):
            print(self.__max1[i])
            # print(self.__virtualBoard)

        '''
        Priority Queue
        '''
        # test = PriorityQueue()
        # test.put([110, "test"])
        # test.put([20, "test"])
        # print(test.get())
        # print(test)

    def updateMin1(self):
        print('----- UPDATE Min1 -----')
        self.turn = 2
        # print('TARGET', self.__max1[0][1])
        # for i in range (1,7):
        # self.__virtualBoard = self.__max1[i][1]
        for i in range (1,8):
            self.__virtualBoard = deepcopy(self.__max1[0][1])
            newMin = self.move(2,i)
            newMin.append(self.__virtualBoard[1][7] - self.board[1][7])
            self.__min1.append(newMin)

        # self.__virtualBoard = deepcopy(self.__max1[0][1])
        # newMin = self.move(2,1)
        # newMin.append(self.__virtualBoard[1][1] - self.board[1][i-1])
        # self.__min1.append(newMin)
        for i in range (0,7):
            print("MIN1", self.__min1[i])


    def updateMax2(self):
        print('----- UPDATE Max2 -----')           

    def start(self):
        print('----- SEARCH ALGORITHMS STARTED -----')
        self.updateMax1()
        self.updateMin1()
        # updateMax2()

    ### OLD FUNCTIONS

    # Check if there any marble in the house (1 = there is, 0 = every house is null)
    def checkHouse(player):
        # print(Game.board)
        sumNull = 0
        for i in range(0, 7):
            # print (Game.board[player-1][i])
            if self.board[player-1][i] == 0:
                sumNull += 1
        # print(sumNull)        
        if sumNull == 7:
            # print("TRUE")
            return 0
        else:
            return 1

    # Choose random index of array that have value not zero 
    def randomValidIndex(player):
        validIndex = []
        for i in range(0,7):
            if self.board[player-1][i] != 0:
                validIndex.append(i)

        index = randint(0,len(validIndex))
        return validIndex[index] + 1

    # AI 1 (random valid move)
    def player1Move():
        # print(checkHouse(1))
        if checkHouse(1) == 1:
            print("")
            print("[PLAYER 1 IS MOVE]")
            decision = randomValidIndex(1)
            print("Initial Board", self.board)
            print("decision", decision)
            self.setTurn(1)
            self.move(1, decision)

    # AI 2 (random valid move)
    def player2Move():
        if checkHouse(2) == 1:
            print("")
            print("[PLAYER 2 IS MOVE]")
            decision = randomValidIndex(2)
            print("Initial Board", self.board)
            print("decision", decision)
            # To move the marble
            self.setTurn(2)
            self.move(2, decision)

Game = Congklak(startBoard) 
Game.start()
# Game.setTurn(2)
# print(Game.move(2,2))
