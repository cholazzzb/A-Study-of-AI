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

def buildPieces(nomor):
    playerPieces = []
    startPiecesPosition = [halma_model.ASAL_10_13_0, halma_model.ASAL_10_13_1, halma_model.ASAL_10_13_2, halma_model.ASAL_10_13_3]

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

    def setTeman(self, teman):
        self.teman = teman       

    def easyMode(self, Model):
        print("EASY MODE")
        self.PonderBoard.updateRealBoard(Model.getPapan())
        # self.PonderBoard.updateRealBoard(CustomBoard)
        for Piece in self.Pieces:
            Piece.clearLegalMoves()
            self.PonderBoard.checkPieceLegalMoves(Piece)
            Piece.calculateLenLegalMoves()
        self.PonderBoard.getLongestLenMove(self.Pieces)
        print('DECISION', self.PonderBoard.longestLenMove)
        self.Pieces[self.PonderBoard.longestLenMovePieceIndex].updatePosition(self.PonderBoard.longestLenMove)
        return self.PonderBoard.longestLenMove


    def normalMode(self, Model):
        print("NORMAL MODE")

    def main(self, Model):
        ### IN DEVELOPMENT
        # self.setPonderBoard(AIPonderBoard)
        # # self.PonderBoard.updateRealBoard(Model.getPapan())
        # self.PonderBoard.updateRealBoard(CustomBoard)
        # for Piece in self.Pieces:
        #     self.PonderBoard.checkPieceLegalMoves(Piece)
        #     print(Piece.legalMoves)
        #     Piece.calculateLenLegalMoves()
        # self.PonderBoard.getLongestLenMove(self.Pieces)
        # print('DECISION')
        # print(self.PonderBoard.longestLenMove)
        # # return finalReturn
        
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
