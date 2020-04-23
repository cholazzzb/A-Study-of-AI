# -*- coding: utf-8 -*-
"""
Create : 16 April 2020 16.23
Last Update : 16 April 2020

@author: Toro
"""

from copy import deepcopy

# FORMAT (vertical or y, horizontal or x)
startPositions = {
    101: (0, 0),    102: (0, 1),    103: (1, 0),    104: (0, 2),    105: (1, 1),    106: (2, 0),    107: (0, 3),    108: (1, 2),    109: (2, 1),    110: (3, 0),    111: (1, 3),    112: (2, 2),    113: (3, 1),
    201: (0, 9),    202: (0, 8),    203: (1, 9),    204: (0, 7),    205: (1, 8),    206: (2, 9),    207: (0, 6),    208: (1, 7),    209: (2, 8),    210: (3, 9),    211: (1, 6),    212: (2, 7),    213: (3, 8),
    301: (9, 9),    302: (9, 8),    303: (8, 9),    304: (9, 7),    305: (8, 8),    306: (7, 9),    307: (9, 6),    308: (8, 7),    309: (7, 8),    310: (6, 9),    311: (8, 6),    312: (7, 7),    313: (6, 8),
    401: (9, 0),    402: (9, 1),    403: (8, 0),    404: (9, 2),    405: (8, 1),    406: (7, 0),    407: (9, 3),    408: (8, 2),    409: (7, 1),    410: (6, 0),    411: (8, 3),    412: (7, 2),    413: (6, 1)
}

class Piece(object):
    def __init__(self, name, position):
        if round(name/100) == 1:
            self.player = 1
        if round(name/100) == 2:
            self.player = 2
        if round(name/100) == 3:
            self.player = 3
        if round(name/100) == 4:
            self.player = 4

        self.name = name
        self.position = position

        # NOTES : The variables are pair ex: legalMoves[x] has rangeLegalMoves[x], lenLegalMoves[x], etc
        self.legalMoves = []
        # delta = (yAfterMove - ybeforeMove, xAfterMove - xbeforeMove)
        self.deltaLegalMoves = []
        self.lenLegalMoves = []

        self.pieceDirections = []
        self.isAtDestination = False

    def setPieceDirections(self, pieceDirections):
        self.pieceDirections = pieceDirections

    def clearLegalMoves(self):
        self.legalMoves = []
        self.deltaLegalMoves = []
        self.lenLegalMoves = []

    def updatePosition(self, decision):
        if decision[0] != None:
            self.position = decision[0][-1]
        print('UPDATE POSITION')
        print('PIECE ', self.name)
        print('NEW POSITION ', self.position)

    def checkIsAtDestination(self):
        y, x = self.rangeWithDestination
        if y+x < 4:
            self.isAtDestination = True
        
    def checkThreeDestinationPoints(self, AIvariables):    
        destinationThreePoints = AIvariables.threeDestinationPoints[self.player-1]
        for destinationThreePoint in destinationThreePoints:
            if destinationThreePoint[0] == self.position[0] and destinationThreePoint[1] == self.position[1]:
                self.isAtDestination = True

    def calculateLenLegalMoves(self):
        print(self.legalMoves)
        if self.legalMoves[0] != None:
            for legalMove in self.legalMoves:
                self.lenLegalMoves.append(len(legalMove[0]))
        print('LEN LEGAL MOVES', self.lenLegalMoves)
            
    def calculateDeltaLegalMoves(self, destinationPoints):
        if self.legalMoves[0] != None:
            yDest, xDest = destinationPoints[self.player-1]
            for legalMove in self.legalMoves:
                yNew, xNew = legalMove[0][-1]
                yOld, xOld = legalMove[1]
                rangeNew = (abs(yNew-yDest), abs(xNew-xDest))
                rangeOld = (abs(yOld-yDest), abs(xOld-xDest))
                yDelta, xDelta = (rangeOld[0]-rangeNew[0], rangeOld[1]-rangeNew[1])
                self.deltaLegalMoves.append((yDelta, xDelta))
        print('DELTA LEGAL MOVES', self.deltaLegalMoves)

    def calculateRangeWithDestination(self, destinationPoints):
        y, x = destinationPoints[self.player-1]
        ypos, xpos = self.position
        self.rangeWithDestination = (abs(y-ypos), abs(x-xpos))
        print("RANGE WITH DESTINATION", self.rangeWithDestination)



class PonderBoard(object):
    def __init__(self):

        self.piecesPosition = startPositions
        self.realBoard = []

        # FP -> Furthest Piece from corner destination (0,0) or (0,9) or (9,9) or (9,0)
        self.FPName = 101
        self.NPName = 113  # NP -> Nearest Piece from idem
        self.rangeBetweenFPNP = (2, 2)
        
        # Furthest / Nearest from Destination Point
        self.furthestPiece = 0
        self.nearestPiece = 0

    def updateRealBoard(self, newBoard):
        self.realBoard = newBoard

    def isSquareInBoard(self, position):
        y, x = position
        if y > -1 and x > -1 and y < 10 and x < 10:
            return True
        else:
            return False

    def isPieceInTheSquare(self, position):
        y, x = position
        if self.realBoard[y][x] == 0:
            return False
        else:
            return True

    def checkPieceGeserMoves(self, Piece):
        y0, x0 = Piece.position
        for pieceDirection in Piece.pieceDirections:
            y, x = pieceDirection
            if self.isSquareInBoard((y0+y, x0+x)):
                if self.isPieceInTheSquare((y0+y, x0+x)) == False:
                    Piece.legalMoves.append([[(y0+y, x0+x)], (y0, x0), 0])
        if len(Piece.legalMoves) == 0:
            Piece.legalMoves = [None, None, 2]

    def checkPieceJumpMoves(self, newPiecePosition, pieceDirections):
        y0, x0 = newPiecePosition
        jumpMoves = []
        for pieceDirection in pieceDirections:
            y, x = pieceDirection
            if self.isSquareInBoard((y0+y, x0+x)) and self.isSquareInBoard((y0+y+y, x0+x+x)):
                if self.isPieceInTheSquare((y0+y, x0+x)) and self.isPieceInTheSquare((y0+y+y, x0+x+x)) == False:
                    jumpMoves.append([(y0+y+y, x0+x+x)])
        return jumpMoves

    def checkPieceLegalMoves(self, Piece):
        print()
        print('-----', Piece.name, "-----")
        # Check Jumps Moves
        # First Loop
        jumpMoves = self.checkPieceJumpMoves(Piece.position, Piece.pieceDirections)
        print('JUMPMOVES', jumpMoves)
        # After First Loop
        if len(jumpMoves) != 0:
            isCheckAgain = True
        else:
            isCheckAgain = False
        # print('IS CHECK AGAIN', isCheckAgain)
        while isCheckAgain:
            for jumpMove in jumpMoves:
                oldMove = jumpMoves.pop(0)
                analyzeMove = deepcopy(oldMove[-1])
                # print('OLDMOVE', oldMove)
                # print('ANALYZEMOVE', analyzeMove)
                # print('JUMPMOVES', jumpMoves)
                analyzeResults = self.checkPieceJumpMoves(analyzeMove, Piece.pieceDirections)
                # print('ANALYZE RESULTS BEFORE', analyzeResults)
                isCheckAgain = False
                if len(analyzeResults) != 0:
                    for analyzeResult in analyzeResults:
                        if len(oldMove) > 1:
                            positionBeforeAnalyzeMove = oldMove[-2]
                            yBefore, xBefore = positionBeforeAnalyzeMove
                            # print('POSITION BEFORE ANALYZE MOVE', positionBeforeAnalyzeMove)
                            analyzeResult = analyzeResult[0]
                            # print('ANALYZE RESULTS AFTER', analyzeResult)
                            yAfter, xAfter = analyzeResult
                            if yAfter != yBefore or xAfter != xBefore:
                                newMove = deepcopy(oldMove)
                                newMove.append(analyzeResult)
                                # print('NEWMOVE', newMove)                        
                                jumpMoves.append(newMove)
                                isCheckAgain = True
                        else:
                            newMove = deepcopy(oldMove)
                            newMove.append(analyzeResult[0])
                            # print('NEWMOVE', newMove)                        
                            jumpMoves.append(newMove)
                            isCheckAgain = True
                else:
                    jumpMoves.append(oldMove)
            # print('IS CHECK AGAIN', isCheckAgain)
            # print('JUMP MOVES', jumpMoves)
        for jumpMove in jumpMoves:
            Piece.legalMoves.append([jumpMove, Piece.position, 1])

        # Check Geser Moves
        y0, x0 = Piece.position
        for pieceDirection in Piece.pieceDirections:
            y, x = pieceDirection
            if self.isSquareInBoard((y0+y, x0+x)):
                if self.isPieceInTheSquare((y0+y, x0+x)) == False:
                    Piece.legalMoves.append([[(y0+y, x0+x)], (y0, x0), 0])
        if len(Piece.legalMoves) == 0:
            Piece.legalMoves = [None, None, 2]

    def getLongestLenMove(self, Pieces):
        longestLen = 0
        thePieceIndex = 0
        lenIndex = 0
        for pieceIndex in range(len(Pieces)):
            for pieceLenIndex in range(len(Pieces[pieceIndex].lenLegalMoves)):
                if Pieces[pieceIndex].lenLegalMoves[pieceLenIndex] > longestLen:
                    longestLen = Pieces[pieceIndex].lenLegalMoves[pieceLenIndex]
                    thePieceIndex = pieceIndex
                    lenIndex = pieceLenIndex
                    print('PIECE - LEN INDEX', thePieceIndex, lenIndex)
                    self.longestLenMovePieceIndex = thePieceIndex
        self.longestLenMove = Pieces[thePieceIndex].legalMoves[lenIndex]
                    
    def getBiggestDeltaMove(self, Pieces):
        biggestDelta = 0
        thePieceIndex = 0
        deltaIndex = 0
        for pieceIndex in range(len(Pieces)):
            for pieceDeltaIndex in range(len(Pieces[pieceIndex].deltaLegalMoves)):
                y, x = Pieces[pieceIndex].deltaLegalMoves[pieceDeltaIndex]
                if y+x > biggestDelta:
                    biggestDelta = y+x
                    thePieceIndex = pieceIndex
                    deltaIndex = pieceDeltaIndex
                    self.biggestDeltaMovePieceIndex = thePieceIndex
        self.biggestDeltaMove = Pieces[thePieceIndex].legalMoves[deltaIndex]
        self.biggestDelta = biggestDelta

    # ANALYZE FUNCTION
    def getFurthestNearestPiece(self, Pieces):
        nearest = 18
        furthest = 0
        for pieceIndex in range(len(Pieces)):
            y, x = Pieces[pieceIndex].rangeWithDestination
            if abs(y+x) > furthest:
                furthest = abs(y+x)
                self.furthestPiece = Pieces[pieceIndex].name
            if abs(y+x) < nearest:
                nearest = abs(y+x)
                self.nearestPiece = Pieces[pieceIndex].name
        # print("NEAREST PIECE", self.nearestPiece)
        # print("FURTHEST PIECE", self.furthestPiece)
        
    def countPiecesAtDestination(self, Pieces):
        self.sumPiecesAtDestination = 0
        for Piece in Pieces:
            if Piece.isAtDestination:
                self.sumPiecesAtDestination += 1

        print('SUM PIECES AT DESTINATION = ', self.sumPiecesAtDestination)

    ## SPECIAL FUNCTION FOR ENDMODE
    def getNearestDestination(self, Piece, Model, destinations):
        nearest = 18
        nearestDestination = (10, 10)
        for destination in destinations:
            print('APA ISI INI ', destination, Model.getBidak(destination[0], destination[1]))
            if Model.getBidak(destination[0], destination[1]) == 0 or round(Model.getBidak(destination[0], destination[1])/100) != Piece.player :
                if abs(Piece.position[0]-destination[0])+abs(Piece.position[1]-destination[0]) < nearest:
                    nearest = abs(Piece.position[0]-destination[0])+abs(Piece.position[1]-destination[0])
                    nearestDestination = destination
        print("SELECTED NEAREST DESTINATION", nearestDestination)
        print("PIECE POSITION", Piece.position)
        return nearestDestination


    def getMoveFromDestination(self, Piece, destination, AIvariables):
        directions = AIvariables.playersDirections[Piece.player-1]
        yPos, xPos = Piece.position
        yDes, xDes = AIvariables.destinationPoints[Piece.player-1]
        print()
        for direction in directions:
            if self.isSquareInBoard((yPos+direction[0], xPos+direction[1])):
                if self.isPieceInTheSquare((yPos+direction[0], xPos+direction[1])):
                    if self.isSquareInBoard((yPos+direction[0]*2, xPos+direction[1]*2)):
                        if self.isPieceInTheSquare((yPos+direction[0]*2, xPos+direction[1]*2)) == False and abs(yDes-(yPos+direction[0]*2))+ abs(xDes-(xPos+direction[1]*2)) < 4:
                            return [(yPos+direction[0]*2, xPos+direction[1]*2)], Piece.position, 1
                else:    
                    return [(yPos+direction[0], xPos+direction[1])], Piece.position, 0     
        return None, None, 2

    def moveDestinationPiece(self, nomor, nearestDestination, AIvariables):
        directions = AIvariables.playersDirections[((nomor+2)%4)-1]
        # print("THIS IS SAI ", nearestDestination[0]+direction[0]+direction[0], nearestDestination[1]+direction[1])
        for direction in directions:
            if self.isSquareInBoard((nearestDestination[0]+direction[0]+direction[0], nearestDestination[1]+direction[1]+direction[1])):
                if self.realBoard[nearestDestination[0]+direction[0]+direction[0]][nearestDestination[1]+direction[1]+direction[1]]//100 == nomor and self.realBoard[nearestDestination[0]+direction[0]][nearestDestination[1]+direction[1]] != 0:
                    return [nearestDestination], (nearestDestination[0]+direction[0]+direction[0], nearestDestination[1]+direction[1]+direction[1]), 1
            if self.isSquareInBoard((nearestDestination[0]+direction[0], nearestDestination[1]+direction[1])):
                if self.realBoard[nearestDestination[0]+direction[0]][nearestDestination[1]+direction[1]]//100 == nomor:
                    return [nearestDestination], (nearestDestination[0]+direction[0], nearestDestination[1]+direction[1]), 0
        return None, None, 2

class AIvariables(object):

    def __init__(self):

        ##### DONE #####
        self.piecesNames = []
        name = []
        for player in range(4):
            for piece in range(13):
                name.append((player+1)*100+piece+1)
            self.piecesNames.append(name)
            name = []

        # piecePosition ada di halma_model

        # FORMAT (vertical or y, horizontal or x) 1 = down or right, -1 = up or left
        self.playersDirections = [
            [(1, 1), (1, 0), (0, 1), (1, -1), (-1, 1)],
            [(1, -1), (1, 0), (0, -1), (1, 1), (-1, -1)],
            [(-1, -1), (-1, 0), (0, -1), (-1, 1), (1, -1)],
            [(-1, 1), (-1, 0), (0, 1), (-1, -1), (1, 1)]
        ]

        # TESTING
        # self.playersDirections = [
        #     [(-1,-1), (0,-1), (1,-1), (-1,0), (1,0),(-1,1), (0,1), (1,1)],
        #     [(-1,-1), (0,-1), (1,-1), (-1,0), (1,0),(-1,1), (0,1), (1,1)],
        #     [(-1,-1), (0,-1), (1,-1), (-1,0), (1,0),(-1,1), (0,1), (1,1)],
        #     [(-1,-1), (0,-1), (1,-1), (-1,0), (1,0),(-1,1), (0,1), (1,1)]
        # ]

        self.finalDestinations1 = [[9, 9], [8, 9], [9, 8], [7, 9], [8, 8],
                                   [9, 8], [6, 9], [7, 8], [8, 7], [9, 6],
                                   [5, 9], [8, 8], [7, 7], [8, 6], [9, 5]]
        self.finalDestinations2 = [[0, 0], [1, 0], [0, 1], [2, 0], [1, 1],
                                   [0, 2], [3, 0], [2, 1], [1, 2], [0, 3],
                                   [4, 0], [3, 1], [2, 2], [1, 3], [0, 4]]

        # diagonal = y + x
        self.diagonalDest1 = [18, 17, 16, 15, 14]
        self.diagonalDest2 = [0, 1, 2, 3, 4]

        self.destinationPoints = [(9,9), (9,0), (0,0), (0,9)]

        self.threeDestinationPoints = [
            [(8, 6), (7, 7), (6, 8)],
            [(8, 3), (7, 2), (6, 1)],
            [(1, 3), (2, 2), (3, 1)],
            [(1, 6), (2, 7), (3, 8)]
        ]