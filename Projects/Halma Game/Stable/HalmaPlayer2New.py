# -*- coding: utf-8 -*-
"""
Created on Sun March 20 23:01:48 2020
Last Update : 16 April 2020

@author: Toro
"""

from AIclass import Piece, Board, AIvariables

from copy import deepcopy
import time

ponderBoard = Board()
AIVar = AIvariables()


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

class HalmaPlayer03(object):
    '''
    New Features



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

    ## AI Version 1 Main Function
    def main1(self, Model):
        ##### This code is for update and Analysis
        # ponderBoard.updateBoard(Model.getPapan())
        ponderBoard.updateBoard(CustomBoard)
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

        ##### This code is the First AI Decision Code
        self.bestMoveSet = self.Pieces[bestIndex].bestMove
        # print('self.bestMoveSet', self.bestMoveSet)

        ##### Don't forget to update the Piece Object Position
        yN, xN = self.bestMoveSet[-1][0][0]
        self.Pieces[bestIndex].updateAfterDecide((xN, yN))

        # print('bestMoveSet no switch', self.bestMoveSet)
        if len(self.bestMoveSet) == 0:
            if self.henti == 0:

                ##### This code make all legalMoves save in Piece Object
                self.updateAndAnalysis(Model) 
                ## including loncat more than 1x 
                ## but the direction only to destination area

                ##### Edit and make the AI code below ####

                # If x and y in switching
                # self.Pieces[bestIndex].updateAfterDecide((yN, xN))
                print('bestMoveSet no switch after', self.bestMoveSet)                        
                
                ##### Don't forget to delete the Piece legalMoves after decide
                for Piece in self.Pieces: # Success
                    Piece.clearLegalMove()

        if len(self.bestMoveSet) == 0:
            self.henti = 0
            print('berhenti')
            return None, None, 2

        self.theReturn = self.bestMoveSet.pop(0)
        # Switching x and y
        y1, x1 = self.theReturn[0][0]
        y2, x2 = self.theReturn[1]
        self.theReturn[0] = [(x1, y1)]
        self.theReturn[1] = (x2, y2)
        
        print()
        print('HALMIEZZZ DECISION (HALMIEZZZ MAIN)')
        print("theReturn should len 1", self.theReturn)
        print()

        self.henti = 1
        time.sleep(0.5)
        return self.theReturn[0], self.theReturn[1], self.theReturn[2]

    def switchReturn(self, oldReturn):
        if oldReturn[0] != None:
            oldStop = oldReturn[0]
            oldStart = oldReturn[1]
            newType = oldReturn[2]

            newStop = []
            # Switch stop
            for before in oldStop:
                x, y = before
                new = (y, x)
                newStop.append(new)

            # Switch start
            x, y = oldStart
            newStart = (y, x)
            newReturn = newStop, newStart, newType
        else:
            newReturn = None, None, 2
        return newReturn

    def main(self, Model):
        # self.setNomor(1) # Delete this later
        # ponderBoard.updateBoard(CustomBoard)
        forReturn = None
        ponderBoard.updateBoard(Model.getPapan())
        ponderBoard.updateNearFarPlus(self.Pieces)

        if ponderBoard.finishMode != True:
            i = 1
            for Piece in self.Pieces:
                print("----- PIECE " + str(i) + "----- ")
                Piece.saveLegalsMove(ponderBoard.getLegalMove(Piece, AIVar))
                print(Piece.legalMoves)
                Piece.newLegalMoves = Piece.convertLegalMoves()
                #### HERE THE SWITCHER FOR LEGALMOVES
                # Piece.switchLegalMoves()
                print(Piece.newLegalMoves)
                Piece.calculateRangeMoves()
                i += 1

            # print('NEAREST PIECE', ponderBoard.nearestPiece)
            print('NEAREST POSITION', ponderBoard.nearestPosition)        
            # print('FURTHEST PIECE', ponderBoard.furthestPiece)
            print('FURTHEST POSITION', ponderBoard.furthestPosition)
            print('MAX RANGE', ponderBoard.maxRange)
            ponderBoard.getHighestRangeMove(self.Pieces)
            # Check distance between furthest and nearest Piece
            xF, yF = ponderBoard.furthestPosition
            xN, yN = ponderBoard.nearestPosition
            xH, yH = ponderBoard.HighestRangeOverall
            print('LPM', abs((xF-xN) + (yF-yF)))
            print('MR', xH+yH)

            forReturn = self.Pieces[ponderBoard.HighestRangeOverallPiece].newLegalMoves[ponderBoard.HighestRangeOverallIndex] 
            print('FOR RETURN', forReturn)
            
            # Update Piece Position
            if forReturn != None:
                if forReturn[0] != None:
                    print('####MovedPieceIndex', ponderBoard.HighestRangeOverallPiece)
                    self.Pieces[ponderBoard.HighestRangeOverallPiece].updateAfterDecide(forReturn[0][-1])
            
            # Restart State
            ponderBoard.restartState()
            for Piece in self.Pieces:
                Piece.resetPieceStates()    
                    
            # print('AFTER SWITCH', finalReturn)   
            # CHECK PIECE POSITION
            for Piece in self.Pieces:
                print("NAME", Piece.name , "POSITION", Piece.position)
            # SWITCH POSITION FOR RETURN
            if forReturn != None:
                if forReturn[0] != None:
                    finalReturn = self.switchReturn(forReturn)
                    print('BENER', finalReturn)


        # FINISH GAME ??
        if forReturn == None or ponderBoard.finishMode == True :
            finalReturn = ponderBoard.finishGame(self.Pieces, ponderBoard, AIVar)
            ponderBoard.finishMode = True

        return finalReturn
        # if abs((xF-xN) + (yF-yF)) < xH+yH:
        #     print('Do Greedy Move')
        #     print(self.Pieces[ponderBoard.HighestRangeOverallPiece].newLegalMoves[ponderBoard.HighestRangeOverallIndex])
        #     return self.Pieces[ponderBoard.HighestRangeOverallPiece].newLegalMoves[ponderBoard.HighestRangeOverallIndex]
        # else:
        #     self.planA()
        



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
