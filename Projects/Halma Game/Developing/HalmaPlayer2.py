# -*- coding: utf-8 -*-
"""
Created on Sun March 20 23:01:48 2020
Last Update : 27 March 2020

@author: Toro
"""

# Dependency
from AIclass import Piece, Board, AIvariables

# Library
from copy import deepcopy
import time

### ----- BUILD THE OBJECT----- ###
# Pondering Board for heuristic
ponderBoard = Board()

# AI variable
AIVar = AIvariables()

# Piece
p101 = Piece(101, (0, 0))
p102 = Piece(102, (1, 0))
p103 = Piece(103, (0, 1))
p104 = Piece(104, (2, 0))
p105 = Piece(105, (1, 1))
p106 = Piece(106, (0, 2))
p107 = Piece(107, (3, 0))
p108 = Piece(108, (2, 1))
p109 = Piece(109, (1, 2))
p110 = Piece(110, (0, 3))
p111 = Piece(111, (4, 0))
p112 = Piece(112, (3, 1))
p113 = Piece(113, (2, 2))
p114 = Piece(114, (1, 3))
p115 = Piece(115, (0, 4))

p201 = Piece(201, (9, 9))
p202 = Piece(202, (9, 8))
p203 = Piece(203, (8, 9))
p204 = Piece(204, (9, 7))
p205 = Piece(205, (8, 8))
p206 = Piece(206, (7, 9))
p207 = Piece(207, (9, 6))
p208 = Piece(208, (8, 7))
p209 = Piece(209, (7, 8))
p210 = Piece(210, (6, 9))
p211 = Piece(211, (9, 5))
p212 = Piece(212, (8, 6))
p213 = Piece(213, (7, 7))
p214 = Piece(214, (6, 8))
p215 = Piece(215, (5, 9))

# All Piece Objects in array
def buildPieces(nomor):
    if nomor == 0:
        Pieces = [p101, p102, p103, p104, p105, p106, p107,
                  p108, p109, p110, p111, p112, p113, p114, p115]
    else:
        Pieces = [p201, p202, p203, p204, p205, p206, p207,
                   p208, p209, p210, p211, p212, p213, p214, p215]
    return Pieces

class HalmaPlayer3(object):

    '''
    Decision Making
    Based on Greedy :

    1. Check all pieces move and choose the longest possible move
    2.

    Architecture :
    1. Ponder Board (to calculate and pondering from the real board have attributes about pieces)
    2. Piece = contain every Piece attributes
    3. AIvariables = contain variables for AI
    
    ##### PIECE #####
    Piece attributes
    1. self.player = 1 / 2 # Player 1 or 2
    2. self.name = Piece name (101,.....)
    3. self.position #== (x, y)
    4. self.range = (xr, yr) range self.position to the destination (0,0) or (9,9)
    
    # The x and y should be reverse here
    5. self.legalMoves = [ [[[(x2, y2)], (x1, y1), type], [[(x2, y2)], (x1, y1), type], [[(x2, y2)], (x1, y1), type] ]
                          [[[(x2, y2)], (x1, y1), type]],
                          [[[(x2, y2)], (x1, y1), type], [[(x2, y2)], (x1, y1), type]]  ]
    6. self.rangeResult = [(xr, yr),
                        (xr, yr),
                        (xr, yr)] # The range after the best move
    7. self.deltaAverage = [(-xda, -yda),   
                            (-xda, -yda),
                            (-xda, -yda)] # (self.rangeResult - self.range) / 15
    8. self.bestMove = 0-..... # the index of self.legalMove
    9. self.isAtDestination = False # True if the piece location is in the destinantion region

    Piece methods
    1. updatePosition() DONE
    2. analysisLegalMove()
    3. getBestMove()
    4. saveLegalMove() DONE
    5. clearLegalMove() DONE


    ##### PONDER BOARD #####
    Ponder Board attribute
    1. self.positions = {
        101: (0,0)
    }
    1.1 self.board [] # the board from the model
    content all piece position
    2. self.ranges1 = (xrange, yrange) # Contain the range of total all piece player 1
    3. self.ranges2 = (xrange, yrange) # idem for player 2
    4. self.averageRange = (xaverage, yaverage) # contain the average range from all piece of player 1 or 2 in x and y to the destination (0,0) or (9,9)
    
    Ponder Board Methods
    old Methods
    getPiece DONE
    updateBoard DONE
    updateRange DONE

    1. self.updatePositions(self, pieceName, newPosition):
    

    # Get possible Geser move 1x
    2. self.getGeserMoves(self, Piece, AIvariables):
    return langkahs
    DONE

    # Get possible Loncat move 1x
    3. self.getLoncatMoves(self, Piece, AIvariables):
    return langkahs
    format:
    [ [[(x1+2, y1)], (x1, y1), type], 
      [[(x1, y1+2)], (x1, y1), type], 
      [[(x1+2, y1+2)], (x1, y1), type] ]
    DONE

    # return geser move and loncat move more than 1x
    4. self.getLegalMoves(self, Piece, AIvariables):
    return legalMoves
    format:
    [ [[[(x2, y2)], (x1, y1), type], [[(x3, y3)], (x2, y2), type], [[(x4, y4)], (x3, y3), type] ]
      [[[(x2, y2)], (x1, y1), type]],
      [[[(x2, y2)], (x1, y1), type], [[(x3, y3)], (x2, y2), type]]  ]
    DONE

    ##### AI VARIABLES #####
    AIvariables attributes
    1. self.directions = [(1,0), (1,-1), (0,-1),
                        (-1,-1), (-1,0), (-1,1),
                        (0,1), (1,1)]

    AIvariables methods
    1.


    ##### THIS AI #####
    attributes
    self.moves = [ [[(x2, y2)], (x1, y1), type],
                [[(x2, y2)], (x1, y1), type],
                [[(x2, y2)], (x1, y1), type] ]


    methods
    1.  self.getMove(self):
    theMove = self.moves.pop(
    return theMove[0], theMove[1], theMove[2]
    )
    return [(x2, y2)], (x1, y1), type
    x2, y2 = posisi akhir
    x1, y1 = posisi awal
    type = 0=>geser, 1=>loncat, 2=> berhenti


    ##### THIS PLAYER3 #####
    main(Model):
    return best Move
    format:
    [(y2, x2)], (y1, x1), 0/1/2
    '''

    nama = "Halmiezzz"
    deskripsi = "Basic AI"
    nomor = 1
    index = 0
    papan = []

    def __init__(self, nama):
        self.nama = nama
        self.positions = {}
        self.ranges = ()  # total ranges (x, y)
        self.bestMoveSet = []
        self.theReturn = [] # the Return Value Container
        self.henti = 0 # 1 == berhenti, 0 == loncat > 1x
        
    def setNomor(self, nomor):
        self.nomor = nomor  # player nomor 1 / 2
        self.index = nomor-1
        self.Pieces = buildPieces(self.index)

    def main(self, Model):
        # print('bestMoveSet no switch', self.bestMoveSet)
        if len(self.bestMoveSet) == 0:
            if self.henti == 0:
                ponderBoard.updateBoard(Model.getPapan()) # Update ponderBoards            
                # ponderBoard.updateBoard(CustomBoard) # Update ponderBoards            
                # print(ponderBoard.getGeserMove(1, (1,3), AIVar)) # Success
                # print(ponderBoard.getLoncatMove(1, (3,0), AIVar)) # Success
                # print(ponderBoard.getLegalMove(p107, AIVar)) # Success
                bestIndex = 0
                # bestRangeResult = 18
                bestLengthMove = 0
                for Piece in self.Pieces: # Success
                    Piece.saveLegalsMove(ponderBoard.getLegalMove(Piece, AIVar))
                    Piece.bestMove =  Piece.getBestMove()
                    Piece.analysisLegalMove()

                    # Best on new range to destination
                    # x, y = Piece.rangeResult
                    # if x+y < bestRangeResult and x != 0 and y != 0 and len(Piece.bestMove) != 0:
                    #     bestRangeResult = x+y
                    #     bestIndex = (Piece.name%100)-1
                    if len(Piece.bestMove) > bestLengthMove:
                        bestIndex = (Piece.name%100)-1
                        bestLengthMove = len(Piece.bestMove)

                self.bestMoveSet = self.Pieces[bestIndex].bestMove
                print('self.bestMoveSet', self.bestMoveSet)
                yN, xN = self.bestMoveSet[-1][0][0]
                self.Pieces[bestIndex].updateAfterDecide((xN, yN))
                # If x and y in switching
                # self.Pieces[bestIndex].updateAfterDecide((yN, xN))
                print('bestMoveSet no switch after', self.bestMoveSet)                        
                for Piece in self.Pieces: # Success
                    Piece.clearLegalMove()
        if len(self.bestMoveSet) == 0:
            self.henti = 0
            print('berhenti')
            return None, None, 2

        self.theReturn = self.bestMoveSet.pop(0)
        # Switching x and y
        # y1, x1 = self.theReturn[0][0]
        # y2, x2 = self.theReturn[1]
        # self.theReturn[0] = [(x1, y1)]
        # self.theReturn[1] = (x2, y2)
        
        print()
        print('HALMIEZZZ DECISION (HALMIEZZZ MAIN)')
        print("theReturn should len 1", self.theReturn)
        print()


        self.henti = 1
        time.sleep(0.5)
        return self.theReturn[0], self.theReturn[1], self.theReturn[2]

'''
PRIORITY QUEUE TESTER
'''
# test = PriorityQueue()
# test.put((-1000, [110, "test"]))
# test.put((10, [10, "tessdfsdt"]))
# test.put((30, [10, "tessdfsdt"]))
# test.put((110, [10, "tessdfsdt"]))
# print(test.get())
# print(test.get())
# print(test.get())
# print(test.get())

CustomBoard = [[101,102,104,107,111,  0,  110,  0,  0,  0],
               [103,105,108,112, 0,  110,  0,  0,  0,  0],
               [106,109,113,  0,  0,  0,  0,  0,  0,  0],
               [110,114,  0,  110,  0,  0,  103,  0,  0,  0],
               [115,  0,  0,  0,  0,  0,  0,  0,  0,  0],
               [  0,  0,  0,  0,  0,  0,  0,  0,  0,215],
               [  0,  0,  0,  0,  0,  0,  0,  0,214,210],
               [  0,  0,  0,  0,  0,  0,  0,213,209,206],
               [  0,  0,  0,  0,  0,  0,212,208,205,203],
               [  0,  0,  0,  0,  0,211,207,204,202,201]]
