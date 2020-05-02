# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 07:23:50 2020
Updated on Sat April 25

@author: Mursito
@author: Toro

"""

import pygame
import time
from copy import deepcopy

from halma_model import HalmaModel
from halma_player import HalmaPlayer
from halma_view import HalmaView
from halma_view_gui_component import textBox

### ----- VARIABLE DECLARATION ----- ###
# Set the color variable
black = (0, 0, 0)
white = (255, 255, 255)
grey = (192, 192, 192)
dark_grey = (48, 48, 48)
red = (235, 0, 0)
blue = (0, 128, 235)
green = (0, 235, 0)
yellow = (235, 235, 0)
redIn = (255, 50, 50)
blueIn = (50, 128, 255)
greenIn = (50, 255, 50)
yellowIn = (255, 255, 50)

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 680
BOARD_SIZE = 616
SQUARE_SIZE = 58

FONT_BIG = 24
FONT_SMALL = 12

MARGIN_BOARD = 30
MARGIN_TEXT = 10

STATISTICS_BOARD_HEIGHT = 275
BUTTON_HEIGHT = 100
MOVE_WIDTH = 150
MOVE_HEIGHT = 30

pcolors=[red, blue, green, yellow]
pcolorsIn=[redIn, blueIn, greenIn, yellowIn]

class HalmaViewGui(HalmaView):

    # Constructor
    def __init__(self, title):
        super().__init__(title)

        self.playersNames = []

        ### ----- STATISTICS CALCULATION ----- ###
        self.totalGeser = []
        self.totalJumps = []
                
        ### ----- INITILIAZE pygame ----- ###
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(title)
    
        ## Create font objects
        self.font = pygame.font.Font('segoe-ui.ttf', FONT_BIG) # (font file, size)
        self.fontBold = pygame.font.Font('segoe-ui-bold.ttf', FONT_BIG)
        self.fontSmall = pygame.font.Font('segoe-ui.ttf', FONT_SMALL)
        self.fontSmallBold = pygame.font.Font('segoe-ui-bold.ttf', FONT_SMALL)

        # UI Variables
        ### ----- CREATE GAME OBJECTS ----- ###
        # Create game board with gridlines
        self.board = pygame.Surface((BOARD_SIZE, BOARD_SIZE))
        self.board.fill(dark_grey)
        for i in range(1, 10):
            pygame.draw.rect(self.board, grey, (0, i*SQUARE_SIZE + (i-1)*4, BOARD_SIZE, 4)) # (surface, color, (posisi x, posisi y, lebar, tinggi))
            pygame.draw.rect(self.board, grey, (i*SQUARE_SIZE + (i-1)*4, 0, 4, BOARD_SIZE))

        # Create Pieces
        self.pieces=[]
        for i in range(4):
            s = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
            s.fill(dark_grey)
            pygame.draw.circle(s, pcolors[i], (29, 29), 25)
            pygame.draw.circle(s, pcolorsIn[i], (29, 29), 20)
            self.pieces.append(s)

        # Create Player Board
        self.playersBoard = pygame.Surface((BOARD_SIZE-SQUARE_SIZE, BOARD_SIZE - STATISTICS_BOARD_HEIGHT))
        self.playersBoard.fill(white)

        # Moves Board
        self.movesBoard = pygame.Surface((BOARD_SIZE-SQUARE_SIZE, BOARD_SIZE - STATISTICS_BOARD_HEIGHT - 10 * FONT_SMALL ))
        self.movesBoard.fill(yellow)

        # Statistics Board
        self.statisticsBoard = pygame.Surface((BOARD_SIZE-SQUARE_SIZE, STATISTICS_BOARD_HEIGHT))
        self.statisticsBoard.fill(grey)

        self.movesBoardComponents = []

        statisticsBoardHComponentsLabel = ["PLAYER 1", "PLAYER 2", "PLAYER 3", "PLAYER 4"]
        statisticsBoardVComponentsLabel = ['JUMLAH GESER', 'JUMLAH LONCAT', "WAKTU RATA2(S)", "JUMLAH WAKTU(S)"]
        self.statisticsBoardHComponents = []
        self.statisticsBoardVComponents = []
        self.totalGeserComponents = []
        self.totalJumpComponents = []
        self.totalTimeComponents = []
        self.averageTimeComponents = []
        for i in range(4):
            component = textBox((BOARD_SIZE-MARGIN_BOARD)/5*(i+1)+(BOARD_SIZE-MARGIN_BOARD)/10, FONT_SMALL, 100, FONT_SMALL+MARGIN_TEXT, pcolors[i], grey, grey, self.fontSmallBold)
            component.updateText(statisticsBoardHComponentsLabel[i])
            self.statisticsBoardHComponents.append(component)
        
            component = textBox((BOARD_SIZE-MARGIN_BOARD)/5-(BOARD_SIZE-MARGIN_BOARD)/10, (i+2)*FONT_SMALL+(i+1)*MARGIN_TEXT, 100, FONT_SMALL+MARGIN_TEXT, black, grey, grey, self.fontSmallBold)
            component.updateText(statisticsBoardVComponentsLabel[i])
            self.statisticsBoardVComponents.append(component)
            
            component = textBox((BOARD_SIZE-MARGIN_BOARD)/5*(i+1)+(BOARD_SIZE-MARGIN_BOARD)/10, 2*FONT_SMALL+MARGIN_TEXT, 100, FONT_SMALL+MARGIN_TEXT, pcolors[i], grey, grey, self.fontSmallBold)
            self.totalGeserComponents.append(component)

            component = textBox((BOARD_SIZE-MARGIN_BOARD)/5*(i+1)+(BOARD_SIZE-MARGIN_BOARD)/10, 3*FONT_SMALL+2*MARGIN_TEXT, 100, FONT_SMALL+MARGIN_TEXT, pcolors[i], grey, grey, self.fontSmallBold)
            self.totalJumpComponents.append(component)

            component = textBox((BOARD_SIZE-MARGIN_BOARD)/5*(i+1)+(BOARD_SIZE-MARGIN_BOARD)/10, 5*FONT_SMALL+4*MARGIN_TEXT, 100, FONT_SMALL+MARGIN_TEXT, pcolors[i], grey, grey, self.fontSmallBold)
            self.totalTimeComponents.append(component)

            component = textBox((BOARD_SIZE-MARGIN_BOARD)/5*(i+1)+(BOARD_SIZE-MARGIN_BOARD)/10, 4*FONT_SMALL+3*MARGIN_TEXT, 100, FONT_SMALL+MARGIN_TEXT, pcolors[i], grey, grey, self.fontSmallBold)
            self.averageTimeComponents.append(component) 

            # Last Move
            component = textBox(30+MOVE_WIDTH+MARGIN_TEXT, 30+(MOVE_HEIGHT+MARGIN_TEXT)*(i+1), MOVE_WIDTH, MOVE_HEIGHT, black, yellow, black, self.fontSmallBold)
            self.movesBoardComponents.append(component)
            # Move length
            component = textBox(30+2*MOVE_WIDTH+MARGIN_TEXT, 30+(MOVE_HEIGHT+MARGIN_TEXT)*(i+1), MOVE_WIDTH/2, MOVE_HEIGHT, black, yellow, black, self.fontSmallBold)
            self.movesBoardComponents.append(component)
            # Longest length
            component = textBox(30+3*MOVE_WIDTH+MARGIN_TEXT, 30+(MOVE_HEIGHT+MARGIN_TEXT)*(i+1), MOVE_WIDTH/2, MOVE_HEIGHT, black, yellow, black, self.fontSmallBold)
            self.movesBoardComponents.append(component)

    def gambarPapan(self):
        self.screen.blit(self.board, (MARGIN_BOARD, 2*MARGIN_BOARD))       

    def gambarBidak(self, model):
        nkotak = model.getUkuran()
        for x in range(nkotak):
            for y in range(nkotak):
                bxy = model.getBidak(x,y)
                if (bxy > 0):
                    p = (bxy // 100) - 1
                    self.screen.blit(self.pieces[p], (MARGIN_BOARD + x*62, 60 + y*62))

    # mulai main 2 pemain
    def tampilAwal(self, model):
        super().tampilAwal(model)
        
        # Clear the screen
        self.screen.fill(black)
        
        self.gambarPapan()
        self.gambarBidak(model)

        # Draw Graph Axis
        self.graphComponents = []
        # Y Axis
        pygame.draw.line(self.statisticsBoard, black, (30, 130), (30, 255))
        component = textBox(30, 120, 50, 15, black, white, white, self.fontSmallBold)
        component.updateText("Time(s)")
        self.graphComponents.append(component)
        for waktu in range (4):
            component = textBox(25, STATISTICS_BOARD_HEIGHT-3*MARGIN_TEXT-round((round(waktu, 3)/5)*175), 15, 1, black, dark_grey, white, self.fontSmallBold)
            component.updateText(waktu)
            self.graphComponents.append(component)

            self.playersNames.append(model.getPemain(waktu).nama)

        # X Axis
        pygame.draw.line(self.statisticsBoard, black, (30, 255), (500, 255))
        component = textBox(530, 255, 50, 15, black, white, white, self.fontSmallBold)
        component.updateText("Giliran")
        self.graphComponents.append(component)
        for giliran in range (20):
            component = textBox(3*MARGIN_TEXT+giliran*5*5, 265, 1, 15, black, dark_grey, white, self.fontSmallBold)
            component.updateText(giliran*5)
            self.graphComponents.append(component)

    # tampilkan pemain yang aktif
    def tampilMulai(self, model, statisticData):
        super().tampilMulai(model, statisticData)
        
        ## PLAYER INFORMATION
        self.playersComponents = []
        self.movesBoardlabelsComponents = []
        movesBoardComponentsLabel = ['PLAYERS', 'LAST MOVE', 'MOVE LENGTH', 'LONGEST MOVE']

        playerComponentsTexts = ['BALIK', 'PAUSE', 'LANJUT']
        for i in range(3):
            component = textBox((BOARD_SIZE-SQUARE_SIZE)*(i+1)/4, STATISTICS_BOARD_HEIGHT-(BUTTON_HEIGHT)/2 + (FONT_BIG+FONT_SMALL)/2*5, 100, FONT_BIG+10, black, grey, dark_grey, self.fontBold)
            component.updateText(playerComponentsTexts[i])
            self.playersComponents.append(component)

        component = textBox((BOARD_SIZE-SQUARE_SIZE)*2/4, MARGIN_TEXT + (FONT_BIG+FONT_SMALL)/2, 60, FONT_BIG, black, white, white, self.fontBold)
        component.updateText("VERSUS")
        self.playersComponents.append(component) 
     
        # Set the Player Turn
        langkah = (model.getLangkah() // 4 + (model.getLangkah() % 4 > 0))
        g = model.getGiliran()
        p = model.getPemain(g)
        self.tPlayerTurn = self.font.render('LANGKAH '+ str(langkah)+ " : " + p.nama, True, pcolors[g], black)
        self.tPlayerTurnR = self.tPlayerTurn.get_rect()        
        self.tPlayerTurnR.center = (SCREEN_WIDTH/2, FONT_BIG/2 + MARGIN_TEXT)

        self.screen.blit(self.tPlayerTurn, self.tPlayerTurnR)

        self.screen.blit(self.playersBoard, (BOARD_SIZE+2*MARGIN_BOARD, 2*MARGIN_BOARD))
        for component in self.playersComponents:
            component.draw(self.playersBoard)

        self.screen.blit(self.movesBoard, (BOARD_SIZE+2*MARGIN_BOARD, 2*MARGIN_BOARD + 6*FONT_SMALL))

        self.screen.blit(self.statisticsBoard, (BOARD_SIZE+2*MARGIN_BOARD, 400))

        component = textBox((BOARD_SIZE-SQUARE_SIZE)*1/4, MARGIN_TEXT, 60, FONT_SMALL, red, black, white, self.fontSmallBold)
        component.updateText("PLAYER 1")
        self.playersComponents.append(component)
        component = textBox((BOARD_SIZE-SQUARE_SIZE)*1/4, MARGIN_TEXT + (FONT_BIG+FONT_SMALL)/2, 60, FONT_SMALL, red, black, white, self.fontSmallBold)
        component.updateText(model.getPemain(0).nama)
        self.playersComponents.append(component)

        component = textBox((BOARD_SIZE-SQUARE_SIZE)*3/4, MARGIN_TEXT, 60, FONT_SMALL, blue, black, white, self.fontSmallBold)
        component.updateText("PLAYER 2")
        self.playersComponents.append(component)
        component = textBox((BOARD_SIZE-SQUARE_SIZE)*3/4, MARGIN_TEXT + (FONT_BIG+FONT_SMALL)/2, 60, FONT_SMALL, blue, black, white, self.fontSmallBold)
        component.updateText(model.getPemain(1).nama)
        self.playersComponents.append(component)

        component = textBox((BOARD_SIZE-SQUARE_SIZE)*1/4, MARGIN_TEXT + FONT_SMALL + FONT_BIG, 60, FONT_SMALL, green, black, white, self.fontSmallBold)
        component.updateText("PLAYER 3")
        self.playersComponents.append(component)
        component = textBox((BOARD_SIZE-SQUARE_SIZE)*1/4, MARGIN_TEXT + (FONT_BIG+FONT_SMALL)/2*3, 60, FONT_SMALL, green, black, white, self.fontSmallBold)
        component.updateText(model.getPemain(2).nama)
        self.playersComponents.append(component)

        component = textBox((BOARD_SIZE-SQUARE_SIZE)*3/4, MARGIN_TEXT + FONT_SMALL + FONT_BIG, 60, FONT_SMALL, yellow, black, white, self.fontSmallBold)
        component.updateText("PLAYER 4")
        self.playersComponents.append(component)
        component = textBox((BOARD_SIZE-SQUARE_SIZE)*3/4, MARGIN_TEXT + (FONT_BIG+FONT_SMALL)/2*3, 60, FONT_SMALL, yellow, black, white, self.fontSmallBold)
        component.updateText(model.getPemain(3).nama)
        self.playersComponents.append(component) 

        for playerIndex in range(4):
            # Player Names
            component = textBox(30+MARGIN_TEXT, 30+(MOVE_HEIGHT+MARGIN_TEXT)*(playerIndex+1), MOVE_WIDTH/2, MOVE_HEIGHT, black, yellow, black, self.fontSmallBold)
            component.updateText(self.playersNames[playerIndex])
            self.movesBoardlabelsComponents.append(component)

            # Label
            component = textBox(30+playerIndex*MOVE_WIDTH+MARGIN_TEXT, 30, MOVE_WIDTH*5/4, MOVE_HEIGHT, black, yellowIn, black, self.fontSmallBold)
            component.updateText(movesBoardComponentsLabel[playerIndex])
            self.movesBoardlabelsComponents.append(component)

        for component in self.movesBoardlabelsComponents:
            component.draw(self.movesBoard)

        for component in self.playersComponents:
            component.draw(self.playersBoard)
            
        for index in range(4):

            self.statisticsBoardVComponents[index].draw(self.statisticsBoard)
            self.statisticsBoardHComponents[index].draw(self.statisticsBoard)

            self.totalGeserComponents[index].updateText(statisticData.totalGeser[index])
            self.totalGeserComponents[index].draw(self.statisticsBoard)

            self.totalJumpComponents[index].updateText(statisticData.totalJump[index])
            self.totalJumpComponents[index].draw(self.statisticsBoard)

            self.totalTimeComponents[index].updateText(round(statisticData.totalTime[index], 3))
            self.totalTimeComponents[index].draw(self.statisticsBoard)

            self.averageTimeComponents[index].updateText(round(statisticData.averageTime[index], 3))
            self.averageTimeComponents[index].draw(self.statisticsBoard)

            ## Graph 
            pygame.draw.circle(self.statisticsBoard, pcolorsIn[index], (3*MARGIN_TEXT+langkah*5, STATISTICS_BOARD_HEIGHT-3*MARGIN_TEXT-round((round(statisticData.averageTime[index], 3)/5)*175)), 3)

        for component in self.graphComponents:
            component.draw(self.statisticsBoard)

        pygame.display.update()

    # tampilkan geser
    def tampilGeser(self, model, x1, y1, x2, y2):
        super().tampilGeser(model, x1, y1, x2, y2)
        self.gambarPapan()
        self.gambarBidak(model)
        pygame.display.update()

    # tampilkan loncat
    def tampilLoncat(self, model, x1, y1, x3, y3):
        super().tampilLoncat(model, x1, y1, x3, y3)
        self.gambarPapan()
        self.gambarBidak(model)
        pygame.display.update()

    # tampilkan pemain selesai aktif        
    # dan sisa waktu
    def tampilHenti(self, model):
        super().tampilHenti(model)

    # tampilkan pergantian pemain        
    def tampilGanti(self, model, moveContainer):
        super().tampilGanti(model)
        print(f'GILIRAN PLAYER KE - {model.getGiliran()}')
        moveContainer.analyzeMoveSet(model.getGiliran())
        print(f'LEN OF MOVESBOARD COMPONENT     {len(self.movesBoardComponents)}')
        for moveIndex in range(len(self.movesBoardComponents)):
            print(f"MOVE CONTAINER MOVESET   {moveContainer.getMove(moveIndex)}")
            self.movesBoardComponents[moveIndex].updateText(moveContainer.getMove(moveIndex))
            self.movesBoardComponents[moveIndex].draw(self.movesBoard)

        pygame.display.update()

    # tampilkan game selesai
    def tampilAkhir(self, model, status):
        super().tampilAkhir(model, status)
    
