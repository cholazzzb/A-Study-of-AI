'''
WARNING !!!
This code will error if you change the startBoard value
'''

from copy import deepcopy
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

    def __init__(self, board):
        self.board = board
        self.container = []
        self.turn = 1 # Player 1 or 2
        self.player = 1 # Player 1 or 2
        self.lastDecision = 0 # between 1-8
        self.gameNotation = []

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
        self.gameNotation.append(["Player " + str(player), decision])

        if player > 2 or decision > 7:
            print("the player or decision is not valid!")
            return 0
        # get the marbles
        self.container = self.board[player-1][decision-1]
        self.board[player-1][decision-1] = 0

        # print("self.container", self.container)

        # move the marbles
        while self.container > 0:
            self.container -= 1
            
            # change to the next house
            decision += 1
            # print('House Index to put the marble', decision)

            # Skip the opponent house
            # print("Check - turn: ", self.turn, " player: ", player)
            if decision == 8 and self.turn != player:
                decision += 1

            # Change the player house
            if decision > 8:
                player += 1
                if player > 2:
                    player -= 2
                decision -= 8

            # put marble in the next house
            self.board[player-1][decision-1] += 1          

        # Set the last player house
        self.player = player

        # Set the last decision 
        self.lastDecision = decision

        print("New Board", self.board)
        print("Last Index - player", self.player, "last house", self.lastDecision)

        # print("Total new marbles = ", self.board[player-1][decision-1])
        self.endMove()

    def endMove(self):

        print("total marble in the last house", self.board[self.player-1][self.lastDecision-1])

        # end in the warehouse
        if self.lastDecision == 8:
            print("END IN WAREHOUSE")
            if self.turn == 1:
                player1Move()
            else:
                player2Move()

        # Move again at the last house
        elif self.board[self.player-1][self.lastDecision-1]-1 != 0:
            print("MOVE AGAIN")
            self.move(self.player, self.lastDecision)

        # empty in own house
        elif self.turn == self.player:
            print("END IN OWN HOUSE")
            self.board[self.player-1][self.lastDecision-1] += self.board[(self.player%2)][self.lastDecision-1] 
            self.board[(self.player%2)][self.lastDecision-1] = 0           
            print('End Board', self.board)
            print("")
            return 0

        # empty in enemy house
        else:
            print('END IN ENEMY HOUSE')
            print('End Board', self.board)
            print("")
            return 0

    def checkFinish(self):
        if self.board[0][7]+self.board[1][7] == 98:
            print("The game is finished")
            return 1
        else: 
            return 0

    def play(self):
        print('play the game')

Game = Congklak(startBoard) 

# Check if there any marble in the house (1 = there is, 0 = every house is null)
def checkHouse(player):
    # print(Game.board)
    sumNull = 0
    for i in range(0, 7):
        # print (Game.board[player-1][i])
        if Game.board[player-1][i] == 0:
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
        if Game.board[player-1][i] != 0:
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
        print("Initial Board", Game.board)
        print("decision", decision)
        Game.setTurn(1)
        Game.move(1, decision)

# AI 2 (random valid move)
def player2Move():
    if checkHouse(2) == 1:
        print("")
        print("[PLAYER 2 IS MOVE]")
        decision = randomValidIndex(2)
        print("Initial Board", Game.board)
        print("decision", decision)
        # To move the marble
        Game.setTurn(2)
        Game.move(2, decision)

def playRandomGame():
    finish = 0
    while finish == 0:
        player1Move()
        finish = Game.checkFinish()
        # print('finish', finish)
        if finish == 1 :
            break
        player2Move()
        finish = Game.checkFinish()
        # print('finish', finish)
        if finish == 1:
            break
    if Game.board[0][7] > 49:
        return 1
    elif Game.board[0][7] == 49:
        return 0.5
    return 2

Winner = playRandomGame()
print('The Winner is player : ', Winner)

print(Game.gameNotation)
# for i in range (0, len(Game.gameNotation)):
#     print(Game.gameNotation[i])