# -*- coding: utf-8 -*-
"""
Create : 12 April 2020 16.23
Last Update :

@author: Toro
"""
#from queue import PriorityQueue
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
#        self.greedyMove = PriorityQueue()
        x0, y0 = position
        xr, yr = (xt - x0, yt - y0)
        self.range = (xr, yr)  # (x, y)
        self.legalMoves = []

        # New AI parameters
        self.destination = (xt, yt)
        self.newLegalMoves = []
        self.rangeAfterMoves = []
        self.highestRangeMove = ()

        ## Smaller is better
        self.rangeResult = (0, 0) # bestMove new position - destination coordinate (0,0) or (9,9)
        
        ## Bigger is better
        self.deltaAverage = 0 # old Average - new Average after bestMove new Position
        
        self.isAtDestination = False # Use Boundary to check 
        self.bestMove = 0 # The Best Move Combination

        ## Version 2
        self.relativePosition = []

    '''
    VOID
    update New Position and New Range
    '''
    def updateAfterDecide(self, newPosition):
        print('NEWPOSITION', newPosition)
        self.position = newPosition
        x, y = newPosition
        xt, yt = self.destination
        if self.player == 2:
            if abs(xt+yt-x-y) < 5:
                self.isAtDestination = True
        if self.player == 1:
            if abs(xt+yt-x-y) > 13:
                self.isAtDestination = True

    '''
    VOID
    analysis for LegalMoves and save it to New AI Parameters
    '''
    def analysisLegalMove(self):
        print(self.bestMove)
        if len(self.bestMove) != 0:
            # self.rangeResult
            yn, xn = self.bestMove[-1][0][0]
            xt, yt = self.destination
            self.rangeResult = (abs(xt-xn), abs(yt-yn))
            # self.deltaAverage
            self.deltaAverage = (xn/15, yn/15)
            # print('smaller')
            # print(self.rangeResult)
            # print('bigger')
            # print(self.deltaAverage)
            # print('')

    '''
    VOID
    save the BestMove into self.bestMove

    the BestMove can be vary, but this one will choose:
    '''
    def getBestMove(self):
        maxIndex = 0
        maxLen = 0
        for i in range(len(self.legalMoves)):
            if len(self.legalMoves[i]) > maxLen:
                maxIndex = i
                maxLen = len(self.legalMoves[i])
        if len(self.legalMoves) == 0:
            return []
        else:
            return self.legalMoves[maxIndex]


    '''
    VOID
    Save all legal move
    '''
    def saveLegalsMove(self, legalMove):
        for newMove in legalMove:
            self.legalMoves.append(newMove)

    '''
    VOID 
    Empty the array self.legalMove
    '''
    def clearLegalMove(self):
        self.legalMoves = []

    '''
    convert old Legal Moves to New Format
    '''
    def convertLegalMoves(self):
        oldMoves = deepcopy(self.legalMoves)
        newMove = []
        newMoves = []
        if len(oldMoves) == 0:
            newMoves = [None, None, 2]
        for oldMove in oldMoves:
            newMove = []
            if len(oldMove) > 1:
                moves = []
                for i in range (len(oldMove)):
                    moves.append(oldMove[i][0][0]) 
                newMove.append(moves)
                newMove.append(oldMove[0][1])
                newMove.append(1)    
            else:
                newMove = oldMove[0]
            newMoves.append(newMove)
        return newMoves

    def calculateRangeMoves(self):
        if self.newLegalMoves[0] == None:
            self.rangeAfterMoves.append((0,0))
        else:
            for legalMove in self.newLegalMoves:
                xt, yt = legalMove[0][-1]
                x0, y0 = legalMove[1]
                self.rangeAfterMoves.append((abs(xt-x0), abs(yt-y0)))

        print('RANGE AFTER MOVES', self.rangeAfterMoves)

    def resetPieceStates(self):
        # New AI parameters
        self.legalMoves = []
        self.destination = (0, 0)
        self.newLegalMoves = []
        self.rangeAfterMoves = []
        self.highestRangeMove = ()

    def switchLegalMoves(self):
        afterSwitch = []
        if len(self.newLegalMoves) != 3 and self.newLegalMoves[0] != None:
            for legalMove in self.newLegalMoves:
                if legalMove[0] != None:
                    oldStop = legalMove[0]
                    oldStart = legalMove[1]
                    newType = legalMove[2]

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
                afterSwitch.append(newReturn)
            self.newLegalMoves = afterSwitch


'''
Board class is used to save state:
Overall progress of Pieces
'''
class Board(object):

    def __init__(self):
        self.positions = startPositions
        # total ranges (x, y) # Classic game 10x10 2 player 15 pieces, start ranges = ()
        self.ranges1 = (155, 155)
        self.ranges2 = (155, 155)
        self.board = []

        # For Greedy Decision
#        self.greedyCollector = PriorityQueue()

        # New AI
        self.averageRange = () 

        # For Finishing Game
        targetContainer = []
        for i in range (15):
            targetContainer.append(False)
        self.targetContainer = targetContainer


        ### Version 2
        self.PiecesPositions = []
        self.PiecesRelativeDistance = []

        self.furthestPiece = None
        self.furthestPosition = None
        self.nearestPiece = None
        self.nearestPosition = None
        self.maxRange = None
        self.HighestRangeOverall = (0, 0)
        self.HighestRangeOverallPiece = 0
        self.HighestRangeOverallIndex = 0

        self.finishMode = False

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
                    langkah = [[(x+xM, y+yM)], (x, y), 0]
                    langkahs.append(langkah)
        return langkahs

    # Check move with one loncat
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
            if y+yM < 10 and y+yM > -1 and x+xM < 10 and x+xM > -1 and y+yM+yM < 10 and y+yM+yM > -1 and x+xM+xM < 10 and x+xM+xM > -1:
                # Make sure the move is legal
                if self.board[y+yM][x+xM] != 0 and self.board[y+yM+yM][x+xM+xM] == 0:
                    langkah = [[(x+xM+xM, y+yM+yM)], (x, y), 1]
                    langkahs.append(langkah)
        return langkahs

    def getLegalMove(self, Piece, AIvariables):
        # Check Check Multiple Loncat Move
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
            for i in range (lastLen):
                legalMove = legalMovesLoncat.pop(0)
                x, y = legalMove[-1][0][0]
                langkahs = self.getLoncatMove(Piece.player, (x, y), AIvariables)
                for langkah in langkahs:
                    legalMove.append(langkah)
                    forLegalMovesLoncat = deepcopy(legalMove)
                    legalMovesLoncat.append(forLegalMovesLoncat)
                    legalMove.pop(-1)
                if len(langkahs) == 0:
                    forLegalMovesLoncat = deepcopy(legalMove)
                    legalMovesLoncat.append(forLegalMovesLoncat)
            newLen = len(legalMovesLoncat)

        for newMoves in self.getGeserMove(Piece.player, Piece.position, AIvariables):
            legalMovesLoncat.append([newMoves])

        return legalMovesLoncat 

    ### Version 2
    def getPiecesPositions(self, Pieces):
        for Piece in Pieces:
            self.PiecesPositions.append(Piece.position)

    def calculateRelativeDistance(self):
        relativeDistance = []
        PieceRelativeDistance = []
        u = 1

        for i in range (len(self.PiecesPositions)):
            for residu in range (len(self.PiecesPositions) - u):
                x1, y1 = self.PiecesPositions[i]
                x2, y2 = self.PiecesPositions[residu + u]
                relativeDistance.append((x2-x1, y2-y1))
            self.PiecesRelativeDistance.append(relativeDistance)
            relativeDistance = []
            u += 1
        
    def giveRelativeDistance(self, Pieces):
        print()
        # In Development

    def updateNearFarPlus(self, Pieces):
        nearestRange = 20
        furthestRange = 0
        for Piece in Pieces:
            xt, yt = Piece.destination
            x0, y0 = Piece.position
            if abs(xt+yt-x0-y0) < nearestRange:
                nearestRange = abs(xt-x0) + abs(yt-y0)
                self.nearestPiece = Piece.name
                self.nearestPosition = Piece.position
            if abs(xt+yt-x0-y0) > furthestRange:
                furthestRange = abs(xt-x0) + abs(yt-y0)
                self.furthestPiece = Piece.name
                self.furthestPosition = Piece.position
        x2, y2 = self.nearestPosition
        x1, y1 = self.furthestPosition
        self.maxRange = (abs(x2-x1), abs(y2-y1))
    
    def getHighestRangeMove(self, Pieces):
        xMax = 0
        yMax = 0
        thePiece = 0
        theIndex = 0
        for Piece in range(len(Pieces)):
            for index in range(len(Pieces[Piece].rangeAfterMoves)):    
                xR, yR = Pieces[Piece].rangeAfterMoves[index]
                if xR+yR > xMax+yMax:
                    xMax = xR
                    yMax = yR
                    thePiece = Piece
                    theIndex = index
        self.HighestRangeOverall = Pieces[thePiece].rangeAfterMoves[theIndex]
        self.HighestRangeOverallPiece = thePiece
        self.HighestRangeOverallIndex = theIndex  
        print('HIGHEST RANGE', self.HighestRangeOverall)        
        print('PIECE', self.HighestRangeOverallPiece)
        print('INDEX', self.HighestRangeOverallIndex)                    
        # print("getHighestRangeMove")

    def getHighestRangeMoveR(self, Pieces):
        xMax = 0
        yMax = 0
        thePiece = 0
        theIndex = 0
        maxStrait = 0
        maxHorz = 0
        maxVert = 0
        '''finaldest = []
        finaldest1 = [[0, 0], [1, 0], [0, 1], [2, 0], [1, 1],
                      [0, 2], [3, 0], [2, 1], [1, 2], [0, 3], 
                      [4, 0], [3, 1], [2, 2], [1, 3], [0, 4]]
        finaldest2 = [[9, 9], [8, 9], [9, 8], [7, 9], [8, 8], 
                      [9, 8], [6, 9], [7, 8], [8, 7], [9, 6], 
                      [5, 9], [8, 8], [7, 7], [8, 6], [9, 5]]
        if Piece.player == 1:
            finaldest = finaldest1
        else:
            finaldest = finaldest2
        '''    
        for Piece in range(len(Pieces)):
            for i in range(len(Pieces[Piece].newLegalMoves)):
                if Pieces[Piece].newLegalMoves != [None,None,2]:
                    z = len(Pieces[Piece].newLegalMoves[i][0])-1
                    
                    if abs(Pieces[Piece].newLegalMoves[i][0][z][0]-Pieces[Piece].newLegalMoves[i][1][0]) == abs(Pieces[Piece].newLegalMoves[i][0][z][1]-Pieces[Piece].newLegalMoves[i][1][1]) and abs(Pieces[Piece].newLegalMoves[i][0][0][1]-Pieces[Piece].newLegalMoves[i][1][1]) > maxStrait:
                        
                        thePiece = Piece
                        theIndex = i
                        maxStrait = abs(Pieces[Piece].newLegalMoves[i][0][z][0]-Pieces[Piece].newLegalMoves[i][1][0])
                
                    elif abs(Pieces[Piece].newLegalMoves[i][0][z][0]-Pieces[Piece].newLegalMoves[i][1][0]) > maxHorz or abs(Pieces[Piece].newLegalMoves[i][0][z][1]-Pieces[Piece].newLegalMoves[i][1][1]) > maxVert:
                        
                        thePiece = Piece
                        theIndex = i
                        if abs(Pieces[Piece].newLegalMoves[i][0][z][0]-Pieces[Piece].newLegalMoves[i][1][0]) > abs(Pieces[Piece].newLegalMoves[i][0][z][1]-Pieces[Piece].newLegalMoves[i][1][1]):
                            maxHorz = abs(Pieces[Piece].newLegalMoves[i][0][0][0]-Pieces[Piece].newLegalMoves[i][1][0])
                        elif abs(Pieces[Piece].newLegalMoves[i][0][z][0]-Pieces[Piece].newLegalMoves[i][1][0]) < abs(Pieces[Piece].newLegalMoves[i][0][z][1]-Pieces[Piece].newLegalMoves[i][1][1]):
                            maxVert = abs(Pieces[Piece].newLegalMoves[i][0][z][1]-Pieces[Piece].newLegalMoves[i][1][1])
                
                    else:
                            thePiece = Piece
                            theIndex = i
                    
        self.HighestRangeOverall = Pieces[thePiece].rangeAfterMoves[theIndex]
        self.HighestRangeOverallPiece = thePiece
        self.HighestRangeOverallIndex = theIndex  
        print('HIGHEST RANGE', self.HighestRangeOverall)        
        print('PIECE', self.HighestRangeOverallPiece)
        print('INDEX', self.HighestRangeOverallIndex)                    
        # print("getHighestRangeMove")

    def restartState(self):
        self.PiecesPositions = []
        self.PiecesRelativeDistance = []

        self.furthestPiece = None
        self.furthestPosition = None
        self.nearestPiece = None
        self.nearestPosition = None
        self.maxRange = None
        self.HighestRangeOverall = (0, 0)
        self.HighestRangeOverallPiece = 0
        self.HighestRangeOverallIndex = 0

    def finishGame(self, Pieces, Board, AIVar):
        diagonalDest = []    
        diagonalDestIndex = []
        mustMovePiecesIndex = []    
        destination = []
        finishReturn = [(0,0)], (0,0), 1
        if Pieces[0].player == 1:
            diagonalDest = AIVar.diagonalDest1
            finalDirection = AIVar.finalDirections1
        else:
            diagonalDest = AIVar.diagonalDest2
            finalDirection = AIVar.finalDirections2
        # print('diagonalDest', diagonalDest)

        # Save the piece index must move to destination
        for index in range(len(Pieces)):
            if Pieces[index].isAtDestination == False:
                mustMovePiecesIndex.append(index)
            print(Pieces[index].name, Pieces[index].isAtDestination)
        print("MUSTMOVE", mustMovePiecesIndex)

        # Check the destination location for Must Move Piece
        for desti in finalDirection:
            x, y = desti
            if Board.board[y][x] == 0:
                destination.append(desti)
        print(destination)

        # Get Direction to Move
        destinationX, destinationY = destination[0]
        x, y = Pieces[mustMovePiecesIndex[0]].position
        directionX, directionY = (destinationX - x,destinationY - y)
        if directionX > 0:
            dirX = 1
        elif directionX < 0:
            dirX = -1
        else:
            dirX = 0
        if directionY > 0:
            dirY = 1
        elif directionY < 0:
            dirY = -1
        else:
            dirY = 0
        print('Direction X', 'Direction Y', dirX, dirY)
        print('Position', x, y)
        print('Destination', destinationX, destinationY)

        # Ubah jadi rekursif ya
        if Board.board[y+dirY][x+dirX] != 0:
            if Board.board[y+dirY+dirY][x+dirX+dirX] == 0:
                finishReturn = [(y+dirY+dirY,x+dirX+dirX)], (y,x), 1
            else:
                if Board.board[y+dirY][x] != 0:
                    if Board.board[y+dirY+dirY][x] == 0:
                        finishReturn = [(y+dirY+dirY,x)], (y,x), 1

                elif Board.board[y][x+dirX] != 0:
                    if Board.board[y][x+dirX+dirX] == 0:
                        finishReturn = [(y,x+dirX+dirX)], (y,x), 1

                elif Board.board[y+dirY][x] == 0:
                    finishReturn = [(y+dirY,x)], (y,x), 0

                else:
                    finishReturn = [(y,x+dirX)], (y,x), 0
        else:
            finishReturn = [(y+dirY,x+dirX)], (y,x), 0

        print("CHECK THIS", finishReturn)

        ## Update Piece Position
        yyy, xxx = finishReturn[0][-1]
        Pieces[mustMovePiecesIndex[0]].updateAfterDecide((xxx, yyy))
        return finishReturn



    def planA(self):
        print('plan A')

class AIvariables(object):
    def __init__(self):
        self.directions = [(1, 0), (1, -1), (0, -1),
                           (-1, -1), (-1, 0), (-1, 1),
                           (0, 1), (1, 1)]
        self.greedyDirections1 = [(1,0), (0,1), (1,1)]
        self.greedyDirections2 = [(-1,0), (0,-1), (-1,-1)]
        
        self.finalDirections1 = [[9, 9], [8, 9], [9, 8], [7, 9], [8, 8], 
                            [9, 8], [6, 9], [7, 8], [8, 7], [9, 6], 
                            [5, 9], [8, 8], [7, 7], [8, 6], [9, 5]]
        self.finalDirections2= [[0, 0], [1, 0], [0, 1], [2, 0], [1, 1],
                            [0, 2], [3, 0], [2, 1], [1, 2], [0, 3], 
                            [4, 0], [3, 1], [2, 2], [1, 3], [0, 4]]

        self.Pieces1Name = ['p101', 'p102', 'p103', 'p104', 'p105', 'p106', 'p107', 'p108', 'p109', 'p110', 'p111', 'p112', 'p113', 'p114', 'p115',]
        self.Pieces2Name = ['p201', 'p202', 'p203', 'p204', 'p205', 'p206', 'p207', 'p208', 'p209', 'p210', 'p211', 'p212', 'p213', 'p214', 'p215',]

        self.diagonalDest1 = [18, 17, 16, 15, 14]
        self.diagonalDest2 = [0, 1, 2, 3, 4]