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

    def setTurn(self, turn):
        self.turn = turn
    
    # player : 1-2, decision : 1-7
    def move(self, player, decision):
        if player > 2 or decision > 7:
            print("the player or decision is not valid!")
            return 0
        # get the marbles
        self.container = self.board[player-1][decision-1]
        self.board[player-1][decision-1] = 0

        # print("self.container", self.container)
        print("Initial Board", self.board)

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
        print("LAST INDEX - player", self.player, "last house", decision)
        print("")

        # print("Total new marbles = ", self.board[player-1][decision-1])
        self.endMove()

    def endMove(self):

        # end in the warehouse
        if self.lastDecision == 8:
            print("END IN WAREHOUSE")

        # Move again at the last house
        elif self.board[self.player-1][self.lastDecision-1] != 0:
            # print("LAST INDEX", self.player, self.lastDecision)
            self.move(self.player, self.lastDecision)

        # empty in own house
        elif self.turn == self.player:
            print("END IN OWN HOUSE")
            print('End Board', self.board)
            return 0

        # empty in enemy house
        else:
            print('END IN ENEMY HOUSE')
            self.board[self.player-1][self.lastDecision-1] += self.board[(self.player%2)+1][self.lastDecision-1] 
            print('End Board', self.board)        
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

def randomValidIndex(player):
    index = randint(1,7)
    # print(randint(1,7))
    if Game.board[player-1][index] == 0:
        # print("the house is empty!")
        index = randint(1,7)
        # print(randint(1,7))
        randomValidIndex(player)
    return index

def player1Move():
    print("PLAYER 1 IS MOVE")
    decision = randomValidIndex(1)
    print(decision)
    Game.setTurn(1)
    Game.move(1, decision)

def player2Move():
    print("PLAYER 2 IS MOVE")
    decision = randomValidIndex(2)
    print(decision)
    Game.setTurn(2)
    Game.move(2, decision)

def playRandomGame():
    finish = 0
    while finish == 0:
        player1Move()
        finish = Game.checkFinish()
        print('finish', finish)
        if finish == 1 :
            break
        player2Move()
        finish = Game.checkFinish()
        print('finish', finish)
        if finish == 1:
            break
    if Game.board[0][7] > 49:
        return 1
    elif Game.board[0][7] == 49:
        return 0.5
    return 2

Winner = playRandomGame()
print('The Winner is player : ', Winner)
