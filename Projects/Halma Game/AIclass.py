# -*- coding: utf-8 -*-
"""
Create : 20 March 2020 11.23
Last Update :

@author: Toro
"""
from queue import PriorityQueue

# Starting position
startPositions = {
    101: (0, 0),
    102: (1, 0),
    103: (0, 1),
    104: (2, 0),
    105: (1, 1),

    106: (0, 2),
    107: (3, 0),
    108: (2, 1),
    109: (1, 2),
    110: (0, 3),

    111: (4, 0),
    112: (3, 1),
    113: (2, 2),
    114: (1, 3),
    115: (0, 4),

    201: (9, 9),
    202: (9, 8),
    203: (8, 9),
    204: (9, 7),
    205: (8, 8),

    206: (7, 9),
    207: (9, 6),
    208: (8, 7),
    209: (7, 8),
    210: (6, 9),

    211: (9, 5),
    212: (8, 6),
    213: (7, 7),
    214: (6, 8),
    215: (5, 9)
}

'''
Piece class use to save the piece state

Performa is in negative (-). the smaller / more negative is better performance, (-23 is better than -11)
'''


class Piece(object):
    def __init__(self, name, position):
        if round(name/100) == 1:
            xt, yt = (9, 9)
            self.player = 1
        else:
            xt, yt = (0, 0)
            self.player = 2
        self.name = name  # 101,....
        self.position = position  # (x,y)
        self.legalMove = []  # [[[5, 0], [7,0]], [3,0]]
        # The Biggest performa from this piece legal move
        self.greedyMove = PriorityQueue()
        x0, y0 = position
        xr, yr = (xt - x0, yt - y0)
        self.range = (xr, yr)  # (x, y)

    '''
    update New Position and New Range
    '''

    def update(self, newPosition):
        self.position = newPosition
        self.range = ()

    '''
    VOID
    Save all legal move
    '''

    def saveLegalMove(self, legalMove):
        self.legalMove = legalMove

    '''
    VOID
    Put all move to self.greedyMove one per one
    '''

    def saveGreedyMove(self, greedyMove):
        # print('save Greedy Move')
        for i in range(len(greedyMove)):
            self.greedyMove.put(greedyMove[i])

    '''
    VOID => Change the self.greedyMove state
    1. Get the Best Performa (Most Negative Performa Value) from self.greedyMove PriorityQueue
    2. Clear the self.greedyMove state
    '''

    def getBestPerforma(self):
        # print('getBestPerforma')
        theBestPerforma = ()
        if self.greedyMove.empty:
            theBestPerforma = (0, 0)
        if not self.greedyMove.empty():
            theBestPerforma = self.greedyMove.get()
        while not self.greedyMove.empty():
            self.greedyMove.get()
        # print (theBestPerforma)
        return theBestPerforma


'''
Board class is used to save state:
Overall progress of Pieces
'''


class Board(object):

    def __init__(self):
        self.positions = startPositions
        # total ranges (x, y) # Classic game 10x10 2 player 15 pieces, start ranges = ()
        self.ranges1 = (115, 155)
        self.ranges2 = (155, 155)
        self.board = []

        # For Greedy Decision
        self.greedyCollector = PriorityQueue()

    '''
    INPUT
    position (x, y)

    OUTPUT
    0 = null, there is no piece in the position
    Other = there is a piece there
    '''

    def getPiece(self, position):
        x, y = position
        return self.board[y][x]

    # Just update the board

    def updateBoard(self, newBoard):
        self.board = newBoard

    '''
    performa = (deltax, deltay)
    '''

    def updateRange(self, performa):
        x0, y0 = self.ranges
        xp, yp = performa
        self.ranges = (x0+xp, y0+yp)

    '''
    PURE FUNCTION => Check all legal Move (- performa)
    
    INPUT : position
    Position to be checked

    OUTPUT : legalMoves
    Return every legalMove that piece can do 
    For Simplification, only some legalMove that have -performa will saved from this pure function

    The return format is :
    (totalPerforma, performa, move)
    (totalPerforma, (-x performa, -y performa), [ 1/2, (x,y)awal, (x,y)akhir])
    1 = geser
    2 = loncat
    '''

    def checkLegalMove(self, player, position):
        # print('checkLegalMove')
        x, y = position
        legalMoves = []
        # print(x, y)
        # For the player1
        if player == 1:
            # Check geser Move (if True) & Loncat Move (elif)
            if y+1 < 10:
                if self.board[y+1][x] == 0:
                    totalPerforma = -1
                    performa = (0, -1)
                    move = [1, position, (x, y+1)]
                    legalMoves.append((totalPerforma, performa, move))
                elif y+2 < 10:
                    if self.board[y+2][x] == 0:
                        totalPerforma = -2
                        performa = (0, -2)
                        move = [2, position, (x, y+2)]
                        legalMoves.append((totalPerforma, performa, move))

            if x+1 < 10:
                if self.board[y][x+1] == 0:
                    totalPerforma = -1
                    performa = (-1, 0)
                    move = [1, position, (x+1, y)]
                    legalMoves.append((totalPerforma, performa, move))
                elif x+2 < 10:
                    if self.board[y][x+2] == 0:
                        totalPerforma = -2
                        performa = (-2, 0)
                        move = [2, position, (x+2, y)]
                        legalMoves.append((totalPerforma, performa, move))

            if x+1 < 10 and y+1 < 10:
                if self.board[y+1][x+1] == 0:
                    totalPerforma = -2
                    performa = (-1, -1)
                    move = [1, position, (x+1, y+1)]
                    legalMoves.append((totalPerforma, performa, move))
                elif x+2 < 10 and y+2 < 10:
                    if self.board[y+2][x+2] == 0:
                        totalPerforma = -4
                        performa = (-2, -2)
                        move = [2, position, (x+2, y+2)]
                        legalMoves.append((totalPerforma, performa, move))

        # For the player2
        else:
            # Check geser Move (if True) & Loncat Move (elif)
            if y-1 > 0:
                if self.board[y-1][x] == 0:
                    totalPerforma = -1
                    performa = (0, -1)
                    move = [1, position, (x, y-1)]
                    legalMoves.append((totalPerforma, performa, move))
                elif y-2 > 0:
                    if self.board[y-2][x] == 0:
                        totalPerforma = -2
                        performa = (0, -2)
                        move = [2, position, (x, y-2)]
                        legalMoves.append((totalPerforma, performa, move))

            if x-1 > 0:
                if self.board[y][x-1] == 0:
                    totalPerforma = -1
                    performa = (-1, 0)
                    move = [1, position, (x-1, y)]
                    legalMoves.append((totalPerforma, performa, move))
                elif x-2 > 0:
                    if self.board[y][x-2] == 0:
                        totalPerforma = -2
                        performa = (-2, 0)
                        move = [2, position, (x-2, y)]
                        legalMoves.append((totalPerforma, performa, move))

            if x-1 > 0 and y-1 > 0:
                if self.board[y-1][x-1] == 0:
                    totalPerforma = -2
                    performa = (-1, -1)
                    move = [1, position, (x-1, y-1)]
                    legalMoves.append((totalPerforma, performa, move))
                elif x-2 > 0 and y-2 > 0:
                    if self.board[y-2][x-2] == 0:
                        totalPerforma = -4
                        performa = (-2, -2)
                        move = [2, position, (x-2, y-2)]
                        legalMoves.append((totalPerforma, performa, move))
        return legalMoves

    '''
    PURE FUNCTION =>
    1. Collect all best performance from all pieces
    2. Get the best from the best performance
    3. Clear the greedyDecision

    INPUT
    decisions : All best decision from the Pieces
    [(-4, (-2, -2), [2, (0, 2), (2, 4)]), (-2, (-1, -1), [1, (3, 1), (4, 2)]), ...]

    OUTPUT
    the greedyDecision : One of the biggest performa from all decisions (self.greedyCollector)
    '''
    def greedyDecision(self, decisions):
        # print('greedyDecision')
        for decision in decisions:
            # print(decision)
            self.greedyCollector.put(decision)
        theGreedyDecision = self.greedyCollector.get()    
        while not self.greedyCollector.empty():
            self.greedyCollector.get()
        # print (theGreedyDecision)
        return theGreedyDecision

    def main(self):
        print('main')
