# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 08:04:48 2020

@author: Toro
"""

from numpy.random import randint #randint(a,b,c), a is smallest value, b is biggest values, c is how much the random number is generated in list/array 
from congklak_model import CongklakModel
from congklak_player import CongklakPlayer
from MaxMin import AI

from copy import deepcopy
import sys

class CongklakPlayer3(CongklakPlayer, AI):

    ## ----- AI CODE -----
    __virtualBoard = [] # For virtualizing new board 2x8 array
    __max1 = [] # Player 1 7x3 7 = every house, 3 = [house index(1-7), end Board, delta]
    __min1 = [] # Player 2
    __maxMinRAM = [] # Player 1 

    __warehouseMax = []
    __warehouseMin = []
    __delta = []
    
    def __init__(self):
        super().__init__('Toro AI')
        
        self.board = []
        self.container = []
        self.turn = 1 # Player 1 or 2 giliran
        self.player = 1 # Player 1 or 2 daerah lubang
        self.lastDecision = 0 # between 1-8
        self.gameNotation = []


    '''
    random Pick AI
    '''

    def randomPick(self, papan):
        # Choose random index of array that have value not zero 
        validIndex = []
        for i in range(0,7):
            if self.predictionBoard[self.nomor][i] != 0:
                validIndex.append(i)

        index = randint(0,len(validIndex))
        return validIndex[index]

    '''
    First AI

    Function list :
    1. calculate():
        DFS Search Algorithms

    '''
    def getVirtualBoard(self):
        return self.__virtualBoard
    
    def getMax1(self):
        return self.__max1

    def getMin1(self):
        return self.__min1
    
    def getBoard(self):
        return self.board

    def getTurn(self):
        return self.turn
    
    def getLastDecision(self):
        return self.lastDecision

    def setTurn(self, turn):
        self.turn = turn

    def setNewDataIndex(self, decision):
        newDataIndex = [decision]
        return newDataIndex

    # player : 1-2, decision : 1-7
    def move(self, player, decision):

        # self.gameNotation.append(["Player " + str(player), decision])

        if player > 2 or decision > 7:
            print("the player or decision is not valid!")
            sys.exit()

        # print(self.__virtualBoard)
        # print('THISSSSS', self.__virtualBoard[player-1][decision-1])
        
        # print('')
        # print('Initial Board', self.__virtualBoard)
        # print('Decision: Region =', player, 'House =', decision)

        # get the marbles
        self.container = self.__virtualBoard[player-1][decision-1]
        self.__virtualBoard[player-1][decision-1] = 0

        # move the marbles
        while self.container > 0:
            self.container -= 1
            
            # change to the next house
            decision += 1
            # print('House Index to put the marble', decision)

            # Skip the opponent house
            if decision == 8 and self.turn != player:
                decision += 1

            # Change the player house
            if decision > 8:
                player += 1
                if player > 2:
                    player -= 2
                decision -= 8

            # put marble in the next house
            self.__virtualBoard[player-1][decision-1] += 1          

        # Set the last player house
        self.player = player

        # Set the last decision 
        self.lastDecision = decision

        # print("New Board", self.__virtualBoard)
        # print("Last Index: Region =", self.player, "House = ", self.lastDecision)

        # print("total marble in the last house", self.__virtualBoard[self.player-1][self.lastDecision-1])
        # ----- END CONDITION -----
        # end in the warehouse
        if self.lastDecision == 8:
            # print("END IN WAREHOUSE") 
            return self.__virtualBoard         
            
            # if self.turn == 1:
            #     player1Move()
            # else:
            #     player2Move()

        # Move again at the last house
        if self.__virtualBoard[self.player-1][self.lastDecision-1]-1 != 0:
            # print("MOVE AGAIN")
            return self.move(self.player, self.lastDecision)

        # empty in own house
        elif self.turn == self.player:
            # print("END IN OWN HOUSE")         
            self.__virtualBoard[0][self.lastDecision-1] += self.__virtualBoard[1][self.lastDecision-1]
            self.__virtualBoard[1][self.lastDecision-1] = 0
            # print('End Board', self.__virtualBoard)
            # print("")
            return self.__virtualBoard
            
        # empty in enemy house
        else:
            # print('END IN ENEMY HOUSE')
            # print('End Board', self.__virtualBoard)
            # print("")
            return self.__virtualBoard

    def checkFinish(self):
        if self.__virtualBoard[0][7]+self.__virtualBoard[1][7] == 98:
            print("The game is finished")
            return 1
        else: 
            return 0

    def updateMax1(self):
        print('----- UPDATE Max1 -----')

        self.turn = 1
        self.__max1 = []

        for i in range (1,8):
            # print('-----DECISION-----', i)
            # Deep copy the real board to virtualBoard
            self.__virtualBoard = deepcopy(self.board)

            notNullHouseMax = self.notNull(1, i-1) 

            # get Virtual Board from moving a marble house
            newMax = self.setNewDataIndex(notNullHouseMax)
            newMax.append(self.move(1, notNullHouseMax))
            newMax.append(self.__virtualBoard[1][7] - self.board[1][7])
            self.__max1.append(newMax)
        
        for i in range (0, 7):
            print(self.__max1[i])

        '''
        Priority Queue
        '''
        # test = PriorityQueue()
        # test.put([110, "test"])
        # test.put([20, "test"])
        # print(test.get())
        # print(test)

    def updateMin1(self):
        print('----- UPDATE Min1 -----')
        self.turn = 2

        # Loop for all Max 
        for max1Index in range (0,len(self.__max1)):
            
            # tiap"nya
            # Dicari hasil papan dari move tiap lubang
            self.__min1 = []

            # Mencoba tiap langkah kalau lubang tidak kosong
            for langkahCoba in range (1, 8):
                self.__virtualBoard = deepcopy(self.__max1[max1Index][1])
                # Memastika isi lubang tidak kosong
                langkahCoba = self.notNull(2, langkahCoba)
                # print("HRSNYA G NOL", self.__virtualBoard, langkahCoba)
                # print("pilihan", langkahCoba)
                # print("isi" ,self.__virtualBoard[1][langkahCoba-1])
                self.__min1.append(self.move(2, langkahCoba))         
            
            # Dicari nilai delta terbesar dari self.__min1
            biggestIndex = 0
            biggestValue = -100
            for mencariTerbesar in range (0, len(self.__min1)):
                if self.__virtualBoard[0][7] - self.__virtualBoard[1][7] > biggestValue:
                    biggestIndex = mencariTerbesar
            
            # Print isi __min1
            # for indexMin1 in range (0, len(self.__min1)):
            #     print('ISI MIN1', self.__min1[indexMin1])


            self.__warehouseMax.append(self.__min1[biggestIndex][0][7])
            self.__warehouseMin.append(self.__min1[biggestIndex][1][7])
        
        # print(len(self.__warehouseMax))

        for indexWarehouseMaxMin in range (0, len(self.__warehouseMax)):
            self.__delta.append(self.__warehouseMax[indexWarehouseMaxMin] - self.__warehouseMin[indexWarehouseMaxMin])

            print('WAREHOUSEMAX', self.__warehouseMax[indexWarehouseMaxMin])
            print('WAREHOUSEMIN', self.__warehouseMin[indexWarehouseMaxMin])
            print('DELTA', self.__delta[indexWarehouseMaxMin])
            print('')

            # for i in range(0, 7):
            #     theNewBoard = move(2, minR)
            #     self.__warehouseMax = 
            '''
            # Isi minRAM [index max, deltaTabungan, Tabungan1, Tabungan2]
            # loop to test all possibilities from minRAMIndex
            for i in range (1,8): 
                # Copy last board from __max1 array to virtualBoard
                self.__virtualBoard = deepcopy(self.__max1[minRAMIndex][1])

                # If the house is empty skip to check
                # print('INI I NYA', i)
                notNullHouseMin = self.notNull(2, i-1)
                # print('APAKAH 0', notNullHouseMin)
                # save the last board after checking to @newMin
                newMin = [minRAMIndex+1]
                newMin.append(self.move(2, notNullHouseMin))
                # put in the delta
                newMin.append(self.__virtualBoard[1][7] - self.board[1][7])
                # put the newdata to @self.__min1 array
                self.__min1.append(newMin)
                # print("LEN MIN", len(self.__min1))

            # Get the biggest delta from self.__min1
            for i in range(0, len(self.__min1)):

                biggest = self.__min1[i][2] # variable to save biggest delta value
                biggestIndex = 0 # variable to save the biggest index
                    
                for u in range (0, len(self.__min1)):
                    if self.__min1[u][2] > biggest:
                        biggest = self.__min1[u][2]
                        biggestIndex = u
                    # print("BIGGEST", biggest)
                    # print("BIGGEST INDEX", biggestIndex)

            newMaxMinRAM = []
            newMaxMinRAM.append(biggestIndex+1) # Tell the best house index that have the best result
            newMaxMinRAM.append(self.__min1[biggestIndex])
            self.__maxMinRAM.append(newMaxMinRAM)
            
        for i in range (0, len(self.__maxMinRAM)):
            print("MinRAM", self.__maxMinRAM[i])
            '''


    def updateMax2(self):
        print('----- UPDATE Max2 -----')           

    # Just for change the 
    def start(self):
        print('----- SEARCH ALGORITHMS STARTED -----')
        self.updateMax1()
        self.updateMin1()
        # theBest = -100
        # theBestIndex = 0
        # print('LEN MAXMIN RAM', len(self.__maxMinRAM))
        # for i in range(0, len(self.__maxMinRAM)):
        #     if self.__maxMinRAM[i][1][1][0][7] - self.__maxMinRAM[i][1][1][1][7] > theBest:
        #         theBest = self.__maxMinRAM[i][1][1][0][7] - self.__maxMinRAM[i][1][1][1][7]
        #         theBestIndex = self.__maxMinRAM[i][1][0]
        # return theBestIndex 
        # self.updateMax2()

    # To skip null house
    def notNull(self, player, house):
        if self.checkHouse(player, house):
            house += 1
            if house > 7:
                house -= 7
            return self.notNull(player, house)
        else:
            return house

    # Return 0 if null
    def checkHouse(self, player, house):
        if self.__virtualBoard[player-1][house-1] == 0:
            return 1
        else:
            return 0
        
    # Pemain beraksi
    # Gunakan informasi dari papan untuk memilih nomor 
    # lubang mulai
    def main(self, papan):
        turn = 0
        self.board = papan
        lubang = papan.getLubang(self.nomor)
        
        # Update Prediction Board
        self.predictionBoard = []
        newBoard = papan.getLubang(0)
        newBoard.append(papan.getTabungan(0))
        self.predictionBoard.append(newBoard)
        newBoard = papan.getLubang(1)
        newBoard.append(papan.getTabungan(1))
        self.predictionBoard.append(newBoard)
        self.board = deepcopy(self.predictionBoard) ## Copy board dari pa eko ke virtual board
        # self.__virtualBoard = deepcopy(self.board)
        
        # Execute AI Decision
        bestDecision = self.start()
        turn += 1
        print("TOTAL TURN", turn)
        print("INI BEST DECISION", bestDecision)

        return bestDecision

