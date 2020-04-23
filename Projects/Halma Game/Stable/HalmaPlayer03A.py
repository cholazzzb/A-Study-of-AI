# -*- coding: utf-8 -*-
"""
Created on Sun April 16 23:01:48 2020
Last Update : 16 April 2020

@author: Toro
"""

import halma_model
from AIClassTeam import Piece, PonderBoard, AIvariables

from copy import deepcopy
import time

AIPonderBoard = PonderBoard()
AIVar = AIvariables()

startPiecesPosition = [halma_model.ASAL_10_13_0, halma_model.ASAL_10_13_1, halma_model.ASAL_10_13_2, halma_model.ASAL_10_13_3]

def buildPieces(nomor):
    playerPieces = []

    piecesName = AIVar.piecesNames[nomor-1]
    for pieceNumber in range (13):
        playerPiece = Piece(piecesName[pieceNumber], startPiecesPosition[nomor-1][pieceNumber])
        playerPiece.setPieceDirections(AIVar.playersDirections[playerPiece.player-1])
        playerPieces.append(playerPiece)
    return playerPieces

class HalmaPlayer03A(object):

    def __init__(self, nama):
        self.nama = nama
        self.PonderBoard = AIPonderBoard
        
    def setNomor(self, nomor):
        self.nomor = nomor  # player nomor = 1 / 2 / 3 / 4
        self.Pieces = buildPieces(self.nomor)
        self.destinations = startPiecesPosition[((self.nomor+2)%4)-1]

    def setTeman(self, teman):
        self.teman = teman       

    def analyze(self, Model):
        self.PonderBoard.updateRealBoard(Model.getPapan())
        # self.PonderBoard.updateRealBoard(CustomBoard)
        for Piece in self.Pieces:
            Piece.clearLegalMoves()
            self.PonderBoard.checkPieceLegalMoves(Piece)
            Piece.calculateLenLegalMoves()
            Piece.calculateRangeWithDestination(AIVar.destinationPoints)
            Piece.calculateDeltaLegalMoves(AIVar.destinationPoints)
            Piece.checkIsAtDestination()
        self.PonderBoard.getFurthestNearestPiece(self.Pieces)
        self.PonderBoard.countPiecesAtDestination(self.Pieces)


    def getGreedyMove(self):
        self.PonderBoard.getLongestLenMove(self.Pieces)
        self.PonderBoard.getBiggestDeltaMove(self.Pieces)
        self.greedyMove = self.PonderBoard.biggestDeltaMove
        if self.greedyMove == None:
            self.greedyMove = [None, None, 2]
        self.Pieces[self.PonderBoard.biggestDeltaMovePieceIndex].updatePosition(self.greedyMove)

    def getPlanMove(self):
        print('FURTHEST PIECE INDEX', (self.PonderBoard.furthestPiece %100)-1)
        # self.planMove = 
        print()

    def getEndMove(self, Model):
        self.destination = startPiecesPosition[((self.nomor+2)%4)-1]
        print('DESTINATION', self.destination)
        for Piece in self.Pieces:
            if Piece.isAtDestination == False:
                Piece.checkThreeDestinationPoints(AIVar)
                print('SELECTED PIECE', Piece.name)
                nearestDestination = self.PonderBoard.getNearestDestination(Piece, Model, self.destination)
                self.endMove = self.PonderBoard.getMoveFromDestination(Piece, nearestDestination, AIVar)
                print("GET MOVE FROM DESTINATION ENDMOVE", self.endMove)
                if self.endMove[0] != None:
                    Piece.updatePosition(self.endMove)
                    return 0
            else:
                self.endMove = None, None, 2
        print('CHECK THIS', self.endMove[0] == None)
        if self.endMove[0] == None and self.PonderBoard.sumPiecesAtDestination < 13:
            print('NONEEEEEEEEE')
            self.endMove = self.PonderBoard.moveDestinationPiece(self.nomor, nearestDestination, AIVar)

    def easyMode(self, Model):
        print("EASY MODE")

        # EASIER MODE
        self.analyze(Model)
        self.getGreedyMove()
        print("RANGE FPNP", self.PonderBoard.rangeBetweenFPNP)
        print("BIGGEST DELTA", self.PonderBoard.biggestDelta)
        print("GREEDY MOVE", self.greedyMove)
        
        if self.greedyMove[0] != None:
            return self.greedyMove
        else:
            self.getEndMove(Model)
            print('END MOVE', self.endMove)
            return self.endMove

        # IN DEVELOPMENT
        # self.analyze(Model)
        # if self.PonderBoard.sumPiecesAtDestination < 8:
        #     self.getGreedyMove()
        #     if self.getGreedyMove != None:
        #         return self.greedyMove
        #     else:
        #         self.getEndMove(Model)
        #         print('END MOVE', self.endMove)
        #         return self.endMove
        # else:
        #     self.getEndMove(Model)
        #     print('END MOVE', self.endMove)
        #     return self.endMove

        # # STABLE
        # self.analyze(Model)
        # self.getGreedyMove()
        # print('DECISION', self.greedyMove)
        # return self.greedyMove

    def normalMode(self, Model):
        print("NORMAL MODE")

    def main(self, Model):        
        return self.easyMode(Model)

CustomBoard = [
[101, 102, 104, 107, 0, 0, 207, 204, 202, 201], 
[103, 105, 108, 111, 0, 0, 211, 208, 205, 203], 
[106, 109, 112, 0,   0, 0,   0, 212, 209, 206], 
[110, 113, 0,   0,   0, 0,   0,   0, 213, 210], 
[0,     0, 0,   0,   1, 0,   0,   0,   0,   0], 
[0,     0, 0,   0,   0, 0,   0,   0,   0,   0], 
[410, 413, 0,   0,   1, 0,   1,   0, 313, 310], 
[406, 409, 412, 0,   0, 0,   0, 312, 309, 306], 
[403, 405, 408, 411, 0, 0, 311, 308, 305, 303], 
[401, 402, 404, 407, 0, 0, 307, 304, 302, 301]]

EndBoard = [
[301, 302, 304, 307, 303, 0, 309,   0,   0,   0], 
[  0, 305, 308, 0  , 0,   0,   0,   0,   0,   0], 
[306, 309, 312, 0,   0,   0,   0,   0,   0,   0], 
[310, 313, 0,   0,   0,   0,   0,   0,   0,   0], 
[  0,   0, 0,   0,   0,   0,   0,   0,   0,   0], 
[  0,   0, 0,   0,   0,   0,   0,   0,   0,   0], 
[  0,   0, 0,   0,   0,   0,   0,   0,   0,   0], 
[  0,   0,   0, 0,   0,   0,   0,   0,   0,   0], 
[  0,   0,   0,   0, 0,   0,   0,   0,   0,   0], 
[  0,   0,   0,   0, 0,   0,   0,   0,   0,   0]]
