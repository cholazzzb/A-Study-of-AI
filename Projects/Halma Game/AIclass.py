# -*- coding: utf-8 -*-
"""
Create : 20 March 2020 11.23
Last Update :

@author: Toro
"""
from queue import PriorityQueue
from copy import deepcopy

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

        # New AI
        self.legalMoves = []
        self.rangeResult = []
        self.deltaAverage = []
        self.bestMove = 0
        self.isAtDestination = False

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

        # New AI
        self.averageRange = () 

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

    def updateRange(self, performa):
        x0, y0 = self.ranges
        xp, yp = performa
        self.ranges = (x0+xp, y0+yp)

    # Make sure the move won't check the reverse move
    def getGeserMove(self, player, lastPosition, AIvariables):
        langkahs = []
        x, y = lastPosition
        # Check Geser with greedyDirections
        if player == 1:
            directions = AIvariables.greedyDirections1
        else:
            directions = AIvariables.greedyDirections2
        for direction in directions:
            xM, yM = direction
            # Make sure the move is in the board
            if y+yM < 10 and y+yM > -1 and x+xM < 10 and x+xM > -1:
                # Make sure the move is legal
                if self.board[y+yM][x+xM] == 0:
                    langkah = [[(y+yM, x+xM)], (y, x), 0]
                    langkahs.append(langkah)
        return langkahs

    def getLoncatMove(self, player, lastPosition, AIvariables):
        langkahs = []
        x, y = lastPosition
        # Check Loncat with greedyDirections
        if player == 1:
            directions = AIvariables.greedyDirections1
        else:
            directions = AIvariables.greedyDirections2
        for direction in directions:
            xM, yM = direction
            # Make sure the move is in the board
            if y+yM < 10 and y+yM > -1 and x+xM < 10 and x+xM > -1:
                # Make sure the move is legal
                if self.board[y+yM][x+xM] != 0 and self.board[y+yM+yM][x+xM+xM] == 0:
                    langkah = [[(y+yM+yM, x+xM+xM)], (y, x), 1]
                    langkahs.append(langkah)
        return langkahs

    def getLegalMove(self, Piece, AIvariables):
        # Check Loncat with greedyDirections
        lastLen = 0
        # First Loop
        langkahs = self.getLoncatMove(Piece.player, Piece.position, AIvariables)                   
        legalMovesLoncat = []
        for langkah in langkahs:
            copyOflegalMove = []
            copyOflegalMove.append(langkah)
            legalMovesLoncat.append(copyOflegalMove)
        newLen = len(legalMovesLoncat)

        # After First Loop
        while lastLen != newLen:
            lastLen = len(legalMovesLoncat)
            print("LEGAL MOVES", legalMovesLoncat)
            for i in range (lastLen):
                legalMove = legalMovesLoncat.pop(0)
                print(legalMove)
                y, x = legalMove[-1][0][0]
                langkahs = self.getLoncatMove(Piece.player, (x, y), AIvariables)
                for langkah in langkahs:
                    legalMove.append(langkah)
                    legalMovesLoncat.append(legalMove)
                    legalMove.pop(-1)
            newLen = len(legalMovesLoncat)
            print(lastLen, newLen)

        # ## For print First Loop
        # print(legalMovesLoncat)
        # # Print
        # print('LegalMovesLoncat')
        # for legalMove in legalMovesLoncat:
        #     print(legalMove)
        print(legalMovesLoncat)

        return legalMovesLoncat

    def main(self):
        print('main')

class AIvariables(object):
    def __init__(self):
        self.directions = [(1, 0), (1, -1), (0, -1),
                           (-1, -1), (-1, 0), (-1, 1),
                           (0, 1), (1, 1)]
        self.greedyDirections1 = [(1,0), (0,1), (1,1)]
        self.greedyDirections2 = [(-1,0), (0,-1), (-1,-1)]
