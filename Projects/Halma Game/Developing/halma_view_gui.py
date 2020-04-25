# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 07:23:50 2020

@author: Mursito
@author: Toro

"""

import pygame
import time

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

pcolors=[red, blue, green, yellow]
pcolorsIn=[redIn, blueIn, greenIn, yellowIn]

class HalmaViewGui(HalmaView):

    # Constructor
    def __init__(self, title):
        super().__init__(title)

        self.totalGeser = []
        self.totalJumps = []
                
        ### ----- INITILIAZE pygame ----- ###
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(title)
    
        ## Create font objects
        self.font = pygame.font.Font('freesansbold.ttf', FONT_BIG) # (font file, size)
        self.fontSmall = pygame.font.Font('freesansbold.ttf', FONT_SMALL)

        # UI Variables
        ### ----- CREATE GAME OBJECTS ----- ###
        # Create board with gridlines
        self.board = pygame.Surface((BOARD_SIZE, BOARD_SIZE))
        self.board.fill(dark_grey)
        for i in range(1, 10):
            pygame.draw.rect(self.board, grey, (0, i*SQUARE_SIZE + (i-1)*4, BOARD_SIZE, 4)) # (surface, color, (posisi x, posisi y, lebar, tinggi))
            pygame.draw.rect(self.board, grey, (i*SQUARE_SIZE + (i-1)*4, 0, 4, BOARD_SIZE))

        # CREATE PIECES
        ## Create First Player Pieces (Red)
        self.pieces=[]
        for i in range(4):
            s = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
            s.fill(dark_grey)
            pygame.draw.circle(s, pcolors[i], (29, 29), 25)
            pygame.draw.circle(s, pcolorsIn[i], (29, 29), 20)
            self.pieces.append(s)
            
        ## PLAYER INFORMATION
        self.playersInformation = []
        component = textBox(BOARD_SIZE+2*MARGIN_BOARD+(BOARD_SIZE-SQUARE_SIZE)*1/4, 2*MARGIN_BOARD+MARGIN_TEXT, 60, FONT_SMALL, red, black, white, self.fontSmall)
        component.updateText("PLAYER 1")
        self.playersInformation.append(component)
        component = textBox(BOARD_SIZE+2*MARGIN_BOARD+(BOARD_SIZE-SQUARE_SIZE)*1/4, 2*MARGIN_BOARD+MARGIN_TEXT + (FONT_BIG+FONT_SMALL)/2, 60, FONT_SMALL, red, black, white, self.fontSmall)
        # component.updateText(model.getPemain(0).nama)
        self.playersInformation.append(component)

        component = textBox(BOARD_SIZE+2*MARGIN_BOARD+(BOARD_SIZE-SQUARE_SIZE)*3/4, 2*MARGIN_BOARD+MARGIN_TEXT, 60, FONT_SMALL, blue, black, white, self.fontSmall)
        component.updateText("PLAYER 2")
        self.playersInformation.append(component)
        component = textBox(BOARD_SIZE+2*MARGIN_BOARD+(BOARD_SIZE-SQUARE_SIZE)*3/4, 2*MARGIN_BOARD+MARGIN_TEXT + (FONT_BIG+FONT_SMALL)/2, 60, FONT_SMALL, blue, black, white, self.fontSmall)
        # component.updateText(model.getPemain(1).nama)
        self.playersInformation.append(component)

        component = textBox(BOARD_SIZE+2*MARGIN_BOARD+(BOARD_SIZE-SQUARE_SIZE)*1/4, 2*MARGIN_BOARD+MARGIN_TEXT + FONT_SMALL + FONT_BIG, 60, FONT_SMALL, green, black, white, self.fontSmall)
        component.updateText("PLAYER 3")
        self.playersInformation.append(component)
        component = textBox(BOARD_SIZE+2*MARGIN_BOARD+(BOARD_SIZE-SQUARE_SIZE)*1/4, 2*MARGIN_BOARD+MARGIN_TEXT + (FONT_BIG+FONT_SMALL)/2*3, 60, FONT_SMALL, green, black, white, self.fontSmall)
        # component.updateText(model.getPemain(2).nama)
        self.playersInformation.append(component)

        component = textBox(BOARD_SIZE+2*MARGIN_BOARD+(BOARD_SIZE-SQUARE_SIZE)*3/4, 2*MARGIN_BOARD+MARGIN_TEXT + FONT_SMALL + FONT_BIG, 60, FONT_SMALL, yellow, black, white, self.fontSmall)
        component.updateText("PLAYER 4")
        self.playersInformation.append(component)
        component = textBox(BOARD_SIZE+2*MARGIN_BOARD+(BOARD_SIZE-SQUARE_SIZE)*3/4, 2*MARGIN_BOARD+MARGIN_TEXT + (FONT_BIG+FONT_SMALL)/2*3, 60, FONT_SMALL, yellow, black, white, self.fontSmall)
        # component.updateText(model.getPemain(3).nama)
        self.playersInformation.append(component)

        component = textBox(BOARD_SIZE+2*MARGIN_BOARD+(BOARD_SIZE-SQUARE_SIZE)*2/4, 2*MARGIN_BOARD+MARGIN_TEXT + (FONT_BIG+FONT_SMALL)/2, 60, FONT_BIG, black, white, white, self.font)
        component.updateText("VERSUS")
        self.playersInformation.append(component)


        # PAUSE/START BUTTON
        component = textBox(BOARD_SIZE+2*MARGIN_BOARD+(BOARD_SIZE-SQUARE_SIZE)*2/4, 2*MARGIN_BOARD+MARGIN_TEXT + (FONT_BIG+FONT_SMALL)/2*5, 100, FONT_BIG+10, black, grey, dark_grey, self.font)
        component.updateText("PAUSE")
        self.playersInformation.append(component)

        # BACK/NEXT BUTTON
        component = textBox(BOARD_SIZE+2*MARGIN_BOARD+(BOARD_SIZE-SQUARE_SIZE)*3/4, 2*MARGIN_BOARD+MARGIN_TEXT + (FONT_BIG+FONT_SMALL)/2*5, 100, FONT_BIG+10, black, grey, dark_grey, self.font)
        component.updateText("NEXT")
        self.playersInformation.append(component)

        component = textBox(BOARD_SIZE+2*MARGIN_BOARD+(BOARD_SIZE-SQUARE_SIZE)*1/4, 2*MARGIN_BOARD+MARGIN_TEXT + (FONT_BIG+FONT_SMALL)/2*5, 100, FONT_BIG+10, black, grey, dark_grey, self.font)
        component.updateText("BACK")
        self.playersInformation.append(component)

        # Statistics Board
        self.statisticsBoard = pygame.Surface((BOARD_SIZE-SQUARE_SIZE, 275))
        self.statisticsBoard.fill(grey)

        self.statisticsBoardComponents = []

        component = textBox((BOARD_SIZE-MARGIN_BOARD)/5+(BOARD_SIZE-MARGIN_BOARD)/10, FONT_SMALL, 100, FONT_SMALL+MARGIN_TEXT, black, grey, grey, self.fontSmall)
        component.updateText("PLAYER 1")
        self.statisticsBoardComponents.append(component)
        component = textBox((BOARD_SIZE-MARGIN_BOARD)/5*2+(BOARD_SIZE-MARGIN_BOARD)/10, FONT_SMALL, 100, FONT_SMALL+MARGIN_TEXT, black, grey, grey, self.fontSmall)
        component.updateText("PLAYER 2")
        self.statisticsBoardComponents.append(component)
        component = textBox((BOARD_SIZE-MARGIN_BOARD)/5*3+(BOARD_SIZE-MARGIN_BOARD)/10, FONT_SMALL, 100, FONT_SMALL+MARGIN_TEXT, black, grey, grey, self.fontSmall)
        component.updateText("PLAYER 3")
        self.statisticsBoardComponents.append(component)
        component = textBox((BOARD_SIZE-MARGIN_BOARD)/5*4+(BOARD_SIZE-MARGIN_BOARD)/10, FONT_SMALL, 100, FONT_SMALL+MARGIN_TEXT, black, grey, grey, self.fontSmall)
        component.updateText("PLAYER 4")
        self.statisticsBoardComponents.append(component)

        component = textBox((BOARD_SIZE-MARGIN_BOARD)/5-(BOARD_SIZE-MARGIN_BOARD)/10, 2*FONT_SMALL+MARGIN_TEXT, 100, FONT_SMALL+MARGIN_TEXT, black, grey, grey, self.fontSmall)
        component.updateText("JUMLAH GESER")
        self.statisticsBoardComponents.append(component)

        self.totalGeserComponents = []
        component = textBox((BOARD_SIZE-MARGIN_BOARD)/5+(BOARD_SIZE-MARGIN_BOARD)/10, 2*FONT_SMALL+MARGIN_TEXT, 100, FONT_SMALL+MARGIN_TEXT, black, grey, grey, self.fontSmall)
        self.totalGeserComponents.append(component)

        component = textBox((BOARD_SIZE-MARGIN_BOARD)/5*2+(BOARD_SIZE-MARGIN_BOARD)/10, 2*FONT_SMALL+MARGIN_TEXT, 100, FONT_SMALL+MARGIN_TEXT, black, grey, grey, self.fontSmall)
        self.totalGeserComponents.append(component)

        component = textBox((BOARD_SIZE-MARGIN_BOARD)/5*3+(BOARD_SIZE-MARGIN_BOARD)/10, 2*FONT_SMALL+MARGIN_TEXT, 100, FONT_SMALL+MARGIN_TEXT, black, grey, grey, self.fontSmall)
        self.totalGeserComponents.append(component)

        component = textBox((BOARD_SIZE-MARGIN_BOARD)/5*4+(BOARD_SIZE-MARGIN_BOARD)/10, 2*FONT_SMALL+MARGIN_TEXT, 100, FONT_SMALL+MARGIN_TEXT, black, grey, grey, self.fontSmall)
        self.totalGeserComponents.append(component)

        component = textBox((BOARD_SIZE-MARGIN_BOARD)/5-(BOARD_SIZE-MARGIN_BOARD)/10, 3*FONT_SMALL+2*MARGIN_TEXT, 100, FONT_SMALL+MARGIN_TEXT, black, grey, grey, self.fontSmall)
        component.updateText("JUMLAH LONCAT")
        self.statisticsBoardComponents.append(component)

        self.totalJumpComponents = []
        component = textBox((BOARD_SIZE-MARGIN_BOARD)/5+(BOARD_SIZE-MARGIN_BOARD)/10, 3*FONT_SMALL+2*MARGIN_TEXT, 100, FONT_SMALL+MARGIN_TEXT, black, grey, grey, self.fontSmall)
        self.totalJumpComponents.append(component)

        component = textBox((BOARD_SIZE-MARGIN_BOARD)/5*2+(BOARD_SIZE-MARGIN_BOARD)/10, 3*FONT_SMALL+2*MARGIN_TEXT, 100, FONT_SMALL+MARGIN_TEXT, black, grey, grey, self.fontSmall)
        self.totalJumpComponents.append(component)

        component = textBox((BOARD_SIZE-MARGIN_BOARD)/5*3+(BOARD_SIZE-MARGIN_BOARD)/10, 3*FONT_SMALL+2*MARGIN_TEXT, 100, FONT_SMALL+MARGIN_TEXT, black, grey, grey, self.fontSmall)
        self.totalJumpComponents.append(component)

        component = textBox((BOARD_SIZE-MARGIN_BOARD)/5*4+(BOARD_SIZE-MARGIN_BOARD)/10, 3*FONT_SMALL+2*MARGIN_TEXT, 100, FONT_SMALL+MARGIN_TEXT, black, grey, grey, self.fontSmall)
        self.totalJumpComponents.append(component)

        component = textBox((BOARD_SIZE-MARGIN_BOARD)/5-(BOARD_SIZE-MARGIN_BOARD)/10, 4*FONT_SMALL+3*MARGIN_TEXT, 100, FONT_SMALL+MARGIN_TEXT, black, grey, grey, self.fontSmall)
        component.updateText("AVERAGE TIME")
        self.statisticsBoardComponents.append(component)

        component = textBox((BOARD_SIZE-MARGIN_BOARD)/5-(BOARD_SIZE-MARGIN_BOARD)/10, 5*FONT_SMALL+4*MARGIN_TEXT, 100, FONT_SMALL+MARGIN_TEXT, black, grey, grey, self.fontSmall)
        component.updateText("TOTAL TIME")
        self.statisticsBoardComponents.append(component)
        
        self.totalTimeComponents = []
        self.averageTimeComponents = []
        for i in range(4):
            component = textBox((BOARD_SIZE-MARGIN_BOARD)/5*(i+1)+(BOARD_SIZE-MARGIN_BOARD)/10, 5*FONT_SMALL+4*MARGIN_TEXT, 100, FONT_SMALL+MARGIN_TEXT, pcolors[i], grey, grey, self.fontSmall)
            self.totalTimeComponents.append(component)

            component = textBox((BOARD_SIZE-MARGIN_BOARD)/5*(i+1)+(BOARD_SIZE-MARGIN_BOARD)/10, 4*FONT_SMALL+3*MARGIN_TEXT, 100, FONT_SMALL+MARGIN_TEXT, pcolors[i], grey, grey, self.fontSmall)
            self.averageTimeComponents.append(component)

        


    def gambarPapan(self):
        self.screen.blit(self.board, (MARGIN_BOARD, 60))       

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
        
        # CREATE PLAYER INFORMATION
        self.playerInformation = pygame.Surface((BOARD_SIZE-SQUARE_SIZE, BOARD_SIZE))
        self.playerInformation.fill(white)
        
        # Set the Player Turn
        langkah = (model.getLangkah() // 4 + (model.getLangkah() % 4 > 0))
        g = model.getGiliran()
        p = model.getPemain(g)
        self.tPlayerTurn = self.font.render('LANGKAH '+ str(langkah)+ " : " + p.nama, True, pcolors[g], black)
        self.tPlayerTurnR = self.tPlayerTurn.get_rect()        
        self.tPlayerTurnR.center = (SCREEN_WIDTH/2, FONT_BIG/2 + MARGIN_TEXT)

        # RENDER THE GAME
        # Clear the screen
        self.screen.fill(black)
        
        self.gambarPapan()
        self.gambarBidak(model)

        # Render Player Information
        self.screen.blit(self.playerInformation, (BOARD_SIZE+2*MARGIN_BOARD, 2*MARGIN_BOARD))
        self.screen.blit(self.statisticsBoard, (BOARD_SIZE+2*MARGIN_BOARD, 400))

    # tampilkan pemain yang aktif
    def tampilMulai(self, model, statisticData):
        super().tampilMulai(model, statisticData)       
        ip = model.getGiliran()
        p = model.getPemain(ip)
        langkah = model.getLangkah()       
        self.screen.blit(self.tPlayerTurn, self.tPlayerTurnR)

        for component in self.playersInformation:
            component.draw(self.screen)
        
        self.screen.blit(self.statisticsBoard, (BOARD_SIZE+2*MARGIN_BOARD, 400))
        for component in self.statisticsBoardComponents:
            component.draw(self.statisticsBoard)

        for index in range(len(self.totalGeserComponents)):
            self.totalGeserComponents[index].updateText(statisticData.totalGeser[index])
            self.totalGeserComponents[index].draw(self.statisticsBoard)

        for index in range(len(self.totalJumpComponents)):
            self.totalJumpComponents[index].updateText(statisticData.totalJump[index])
            self.totalJumpComponents[index].draw(self.statisticsBoard)

        for index in range(len(self.totalTimeComponents)):
            self.totalTimeComponents[index].updateText(round(statisticData.totalTime[index], 3))
            self.totalTimeComponents[index].draw(self.statisticsBoard)

        for index in range(len(self.averageTimeComponents)):
            self.averageTimeComponents[index].updateText(round(statisticData.averageTime[index], 3))
            self.averageTimeComponents[index].draw(self.statisticsBoard)

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
    def tampilGanti(self, model):
        super().tampilGanti(model)
        self.screen.blit(self15.tPlayerTurn, self.tPlayerTurnR)
        pygame.display.update()

    # tampilkan game selesai
    def tampilAkhir(self, model, status):
        super().tampilAkhir(model, status)
    
